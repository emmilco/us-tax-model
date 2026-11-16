# Lane A4-lows-older: the older-ny, older-scha and older-credits lows, the closure candidates, and the old question-review lows

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16, round 4. Read only on xint. Nothing was run except
`patch` on scratch copies, `git diff --no-index` and small read-only Python (YAML parse, word counts). No engine, walk,
fixture or model call was made.
Labels: **[C path:line]** = checked against that file in xint (or in the scratch copy of xint plus the v2 patch, named
"base"); **[U]** = the entry's own claim, relayed, not reproduced; **[I]** = inferred.
Word counts use the engine's rule (whitespace tokens holding a letter or digit), computed by script on the parsed YAML
(`scratch/round4-lows-older/count.py`).

## Summary

- **Three add-on patches in `patches/v3/`**, each written against xint plus its own v2 patch:
  - `older-ny-lows.patch` (13 hunks, 2 files): fixes BUG-0853, 0854, 0855, 0856, 0858, 0859 and 0860.
  - `older-scha-lows.patch` (11 hunks, 3 files; adds `forms/2025/gift.yaml` to the round): fixes BUG-0458, 0924,
    0801, 0807, 0816, 0818, 0819 and 0820.
  - `older-credits-lows.patch` (18 hunks, 1 file, bank only): fixes BUG-0554, 0794, 0798, 0863, 0864 and 0869. It fixes
    BUG-0555 and 0867 in part.
- **How they were checked.** Each applies cleanly after its own v2 patch. All seven (v2 ny, credits, scha, 0817b,
  then the three v3) apply in sequence on one copy, and every touched YAML file parses. `older-scha-lows` also applies
  after `older-scha` plus **0817a** (dry run). I checked `patches/v3/int-lows.patch` against them: its federal
  `questions.yaml` hunks fail on plain xint as well, so they rest on a different base, and that failure is not caused
  by these patches.
- **BUG-0857 is left to lane int-lows.** `patches/v3/int-lows.patch` already rewrites the gate
  (`ny_it201.has_tax_exempt`) and the `out_of_state_bond_interest` help, with a fixture and a coverage row. I drafted
  the help sentence too, then dropped it to avoid a clash.
- **Correction to lows.md.** The 0817b patch does **not** edit `sa.excluded_income`. It edits the entry just above it,
  `sa.charity_limited` [C patches/v2/older-scha-0817b.patch]. The 0458/0924 fix here is therefore a new hunk, placed
  next to the 0817 hunk. It applies after either 0817a or 0817b.
- **BUG-0458 was half-fixed by the redraft.** The bank prompt no longer says "bona fide resident" [C base
  questions.yaml:1279]. Only the form source still said it [C forms/2025/sa.yaml:180,183], and this patch fixes that.
- **Closure drafts:** 21 fixed by the v3 patches (3 of them in part), plus the 7 candidates. Of those, 6 are fixed or
  done and 1 is obsolete; 0647 is left to the owner. Section 4 has the commands.
- **Old question-review lows (section 3).** Four were partly fixed by the redraft: 0515, 0530, 0559 and 0575
  [C current bank]. None can close yet. 0558, 0560 and 0565 are unchanged.
- **Deferred:** 0852, 0762, 0763, 0750, 0424 (NY), 0768, 0802, 0774 (Schedule A), 0508 and 0568 (credits), and the
  residual parts of 0555 and 0867. Reasons are in section 5. Two need owner decisions: 0762 and 0774. 0867's
  residual is held by the registered owner decision amb.2025.ira_age50.
- **N10 overruns introduced.** These are listed per low. The worst are `person.edu_over` (prompt 42 → 57),
  `gift.special` (a refusing list, 92 → 141) and `household.married_dec31` help (64 → 72). Each is kept for a named
  wrong answer. The owner may cut them.

## 1. Per low: older-ny (`patches/v3/older-ny-lows.patch`, after `v2/older-ny.patch`)

Format: verdict | change (verbatim) | who would answer wrongly before | sources | words before → after | reviews due.

**BUG-0853 (estimated tax gate; late-installment question).** Real [C base forms/ny/2025/ny_it201.yaml:2410 source;
interview/ny/2025/questions.yaml:345 prompt]. Fixed.
- `ny_it201.ask.est_any`, form source (it is the shown prompt; no bank prompt): "Apart from tax taken out of your pay,
  did you (or, on a joint return, your spouse) pay New York income tax for 2025 ahead of time, have a 2024 New York
  refund applied to it, or have estimated tax passed to you by an estate or trust?" (37 → 48). Help: "Count estimated
  payments of State, City or commuter (MCTMT) tax (the last one may be paid in January 2026), a 2024 New York refund
  you asked to have applied to 2025, and a payment made with a request for more time to file." (37 → 43).
- `ny_it201.ask.est_late` bank prompt: "Was any 2025 New York estimated installment skipped, or any of your (or, on a
  joint return, your spouse's) 2025 New York estimated payments made late or smaller than a quarter of what was due
  for the year?" (23 → 38). Source and label: "installment skipped, paid late, or smaller ...".
- Who answered No wrongly: a beneficiary whose estimated tax an estate or trust allocated to them (line 75
  understated); a filer who skipped an installment, or whose spouse made the short one (line 81 refusal missed).
- Source: ny_it201i p. 22 line 75 and "Beneficiaries of an estate or trust"; p. 23 line 81 [U, as quoted in the entry].
- Due: transcription of the two `ny_it201` lines; question reviews of `est_any` and `est_late`. The `est_any`
  prompt is a parent at 48 words (aim 25; the base was already 37). The estate/trust clause is kept in the prompt
  because a beneficiary who reads only the prompt would answer No.

**BUG-0854 (use tax: spouse, services, reservation).** Real [C base questions.yaml:242]. Fixed.
- Prompt: "In 2025, did you (or, on a joint return, your spouse) buy goods or services taxable in New York without
  paying New York sales tax on them (for example online, by mail, or in another state)? Leave out a vehicle or boat
  whose tax you pay at the DMV." (40 → 49).
- Help: "Count a purchase taxed at a lower rate than New York City's, and an untaxed purchase on an Indian
  reservation (unless Oneida Nation tax was paid). ..." (40 → 53).
- Source: ny_it201i line 59, "purchased an item or service", "on an Indian reservation (except for purchases subject
  to Oneida Nation taxes)" [C sources/ny/2025/ny_it201i.txt:1157-1158].
- The reservation example went to help, not the prompt, to hold the prompt length. Due: one question review.

**BUG-0855 (special accrual).** Real [C base questions.yaml:68]. Fixed.
- Prompt: "Did you (or, on a joint return, your spouse) have income fixed in one year but reported federally in
  another, such as a 2025 bonus paid in 2026, or deferred pay or an installment-sale gain from before 2025 reported
  for 2025?" (32 → 41).
- A Yes refuses, so the wider reading can only over-refuse [I]. It follows the form source's "fixed and determinable
  in one tax year but reported federally in another" [C ny_it201.yaml:41]. Due: one question review.

**BUG-0856 (real property credit).** Real [C base questions.yaml:203]. Fixed.
- Prompt: "In 2025, was the rent you (or, on a joint return, your spouse) paid yourselves $450 a month or less on
  average, not counting heat, gas, electricity, furnishings or meals? Or was all the real estate either of you owned
  in 2025 worth $85,000 or less?" (27 → 46).
- Help gains a first sentence: "Leave out any part of the rent paid by a subsidy, such as Section 8." (44 → 59).
- Source: [C sources/ny/2025/ny_it214i.cols.txt:11,13] ("you or your spouse (if married filing jointly) paid",
  "heat, gas, electricity, furnishings, or board"); [C ny_it214.cols.txt:68] ("Do not include any subsidized ...
  part of your rental charge"); [C ny_it214.txt:33] ("own real property ... during 2025").
- The entry's co-op clause was not added. I found no IT-214 text naming co-ops in the quick grep.
- Asked only at AGI of $18,000 or less, and a Yes refuses, so the length costs few filers. Due: one question review.

**BUG-0858 (U.S. obligations; heading without the spouse).** Real [C base questions.yaml:15,104-106]. Fixed.
- Heading: "Did any of your (or, on a joint return, your spouse's) interest or dividends come from these?" (10 → 17).
- Tick: "U.S. government bonds, notes or bills, or a fund holding them" (10 → 11, within the 12-word limit).
- Prompt: "Was any of your (or, on a joint return, your spouse's) interest or dividends from U.S. government
  obligations, such as Treasury bills, notes or bonds, savings bonds, bonds of a U.S. government agency, or a fund that
  holds them?" (23 → 39).
- Who answered No wrongly before: a holder of federal agency obligations reading the list as complete. A Yes refuses
  (line 28), so naming agencies whose interest New York taxes can only over-refuse [I].
- Due: a question review; the **screen review** of the `ny_interest` group (tick and heading changed); `tick-groups`.

**BUG-0859 (inflation check gate and prompt).** Real [C base ny_it201.yaml:747-750 reads only `s1.line9`]. Fixed.
- `ny_it201.has_other_income` expression: `any[s1.line1 > 0, s1.line9 ≠ 0]`, with the label updated, and the
  label of `ny_it201.inflation_if_other_income` updated to match.
- Prompt: "Did you (or, on a joint return, your spouse) include a New York State inflation refund check in your federal
  income, as a state tax refund or as other income?" (19 → 30).
- Value effect: none on any fixture [I]. `ny_it201.ask.inflation_check` has a NY default (false) [C
  fixtures/ny/2025/defaults.json:116], so NY cases with Schedule 1 line 1 now reach the question and answer No, and
  line 25 stays $0.
- Not covered: a line 9 that nets to zero (a line 8a NOL against line 8z items). That is rare and left in the entry's
  residual.
- Due: transcription review of the two `ny_it201` lines (gate change); a question review; `test-fixtures --ny`;
  a coverage row (state refund on line 1, the check answered Yes, expect refused `ny_it201.gate.line25`), which is not
  drafted (see the section 6 list).

**BUG-0860 (public job asked by work, not by Form W-2).** Real [C base ny_it201.yaml:655]. Fixed.
- Source (the shown prompt): "Did you (or, on a joint return, your spouse) get a 2025 Form W-2 from New York State, a
  New York local government or another New York public employer?" (27 → 29). Label: "A Form W-2 from a New York
  public employer".
- Help: "Count the State, a city, county, town or village, a school district, SUNY or CUNY, and public bodies such as
  the MTA, a public hospital or library, or a fire district. A federal job does not count here." (29 → 38).
- The gate already asks this only with a W-2 (`ny_it201.public_job_if_w2`) [C ny_it201.yaml:657].
- Who answered No wrongly before: a retiree paid arrears on a 2025 W-2, a remote worker outside the State, and a
  worker at a public benefit corporation.
- Due: transcription of the line; a question review.

## 2. Per low: older-scha (`patches/v3/older-scha-lows.patch`, after `v2/older-scha.patch` and 0817a or 0817b)

**BUG-0458 and BUG-0924 (`sa.excluded_income`).** Both real. 0458 is fixed in the prompt by the redraft; the source
still said "bona fide resident" [C forms/2025/sa.yaml:180,183]. 0924's help steers a filer with 2024 foreign pay to No
[C base questions.yaml:1282]. Both fixed.
- Prompt: "Do you (or, on a joint return, your spouse) leave out of this 2025 return any income earned abroad, in
  Puerto Rico or in American Samoa?" (33 → 26).
- Help: "Pay received in 2025 for work done abroad in 2024 counts. These are the exclusions of Form 2555 (foreign earned
  income), Form 4563 (American Samoa) and Puerto Rico. A Yes ends the interview here." (36 → 34). The "50 states"
  sentence is dropped, which also clears 0924's District of Columbia point.
- Source and label: "... file Form 2555 or Form 4563, or exclude income from sources within Puerto Rico?" (i1040gi
  p. 98 wording, as cited in the entry [U]).
- Tick unchanged ("Leaving out income earned abroad, in Puerto Rico or in American Samoa"). It already covers pay
  earned abroad in 2024, so no screen review falls due for the tick.
- Due: transcription of `sa.excluded_income`; a question review. The entry asks for its screen review to be rerun, and
  the prompt is what changed, so a **screen review** is due too.

**BUG-0801 (medical costs of a would-be dependent when the filer is claimable).** Real [C base questions.yaml:1443].
Fixed.
- Bank list item: "those of a person who would be your dependent but for having income of $5,200 or more, filing a
  joint return, or your (or, on a joint return, your spouse's) being someone else's dependent".
- Form source item: "... or filed a joint return, or that you (or your spouse, if filing jointly) can be claimed as a
  dependent on someone else's 2025 return".
- Source [C sources/2025/i1040sca.cols.txt:59]. Due: transcription of `sa.line1`; a question review.

**BUG-0807 (land contract).** Real [C base questions.yaml:1327]. Fixed.
- `sa.home_owner` help: "... even if you sold it during the year, and a home you are buying on a land contract while the
  seller holds the deed. A home you rent does not count." (31 → 47).
- Residual [I]: the tick ("Owned a home, condo or land at any time in the year") is unchanged, so a buyer who reads
  only the tick may still answer No. The help is reached from the tick.
- Due: a question review (help only, so no screen review).

**BUG-0816 (mixed value and weight fee).** Real [C base questions.yaml:1504]. Fixed.
- Help: "... If any part of the yearly charge is based on value, answer Yes; a charge wholly flat or by weight does not
  count." (30 → 42).
- Source: i1040sca line 5c, relayed [U]. Due: a question review.

**BUG-0818 (charitable property reductions; gift of use).** Real [C base questions.yaml:874-911]. Fixed by refusing,
not by computing.
- `gift.special` (a Yes refuses) gains three items:
  - "it went to a private foundation that is not an operating foundation, and it is not publicly traded stock";
  - "it is art or other belongings the charity will not use for its charitable purpose";
  - "you gave only the use of it, such as a stay in your vacation home".
- `forms/2025/gift.yaml` `gift.special` label and source gain the first two, with a p526 cite added to the locator.
  The third is already in the source's "conservation or partial interests", since p526 says the right to use property
  "is a contribution of less than your entire interest".
- Sources [C sources/2025/p526.cols.txt:375, 555, 560].
- Prompt 92 → 141 words, and it is a refusing list, so this is the catch-all pattern. **Alternative:** state the
  reductions in the `gift.deduction` help. That keeps the bank-only change, but the computed value would then depend on
  the filer applying a basis rule. I chose refusal because no wrong value can come from it.
- Due: transcription of `gift.special` (**gift.yaml is new to the round**); a question review.

**BUG-0819 (estate-paid medical costs).** Real [C base questions.yaml:1582-1583]. Fixed.
- `sa.medical_any` help: "Count what you paid yourselves for doctors, dentists, hospitals, prescriptions and
  insurance, less what insurance paid back. On $60,000 of income, 7.5% is $4,500. On the final return of a person who
  died in 2025, count costs their estate paid within a year after the death. If not sure, answer Yes." (32 → 51).
- Due: a question review. The help is shown with a tick, but the tick text is unchanged, so no screen review falls due.

**BUG-0820 (`sa.spouse_extra`).** Real [C base questions.yaml:1293-1294]. Fixed.
- Prompt: "Did your husband or wife have no income in 2025, with no 2025 return filed for them, and were they born before
  January 2, 1961, or blind at the end of 2025?" (32 → 32).
- Help gains "Blind means seeing no better than 20/200 in the better eye with glasses, or a field of vision of 20
  degrees or less." (20 → 43).
- The entry's "spouse who died after 65" clause is **not** added. A spouse who died after turning 65 was born before
  January 2, 1961, so they already answer Yes. One who died at 64 also answers Yes and is over-refused (a Yes refuses)
  [I, from i1040gi p. 33 as quoted in the entry].
- Due: a question review.

## 3. Per low: older-credits (`patches/v3/older-credits-lows.patch`, after `v2/older-credits.patch`) and the old lows

**BUG-0554 (Form 5695 "other" and "such" questions).** Real [C base questions.yaml:6107-6330]. Fixed.
- Fourteen amount prompts now name what counts:
  - doors: "Energy Star", in 19d_i, 19d_ii and 19e;
  - windows and skylights: "Energy Star Most Efficient", in 20a_ii to 20a_iv and 20b;
  - "that meet(s) the same efficiency tier", in 22b, 23a_ii, 23b, 29b and 29d;
  - furnaces (24b): "that meet the same standard";
  - biomass (29f): "with the same 75% rating".
- Example, 19e: "What did all the other Energy Star doors cost together, on the same basis?" Each prompt is 14 to
  19 words.
- The entry named eight; the six siblings with the same pattern (19d_ii, 20a_ii to iv, 22b, 23a_ii) are included.
- Due: 14 question reviews, which is the price of the sibling set. The owner may cut the sibling six and leave them
  for the next f5695 change.

**BUG-0555 (Part II residuals).** Partly fixed earlier: line 21a tense (v2), the heat-pump tick's "(not geothermal)"
[C base questions.yaml:5969], and the audit tick "paid for in 2025" [C :5964]. This patch adds:
- 23b help: "Leave out heat pump water heaters; they were asked earlier." (`seq` 56 is before 63 [C]);
- 26b prompt: "... Count only audits with such a report."
- **Left open:** the line 19a door ranking (gross or net) and `qmid_enabling` for 2024-installed enabling property,
  where a No only refuses. **Closure in part.**

**BUG-0794 (line 18a structural and finished-surface parts).** Real [C base questions.yaml:6097]. Fixed in the prompt,
not the help: "... after any rebate or utility subsidy? Leave out siding, drywall and anything else that also holds up
the house or is a finished surface." (17 → 35).
- The help was already about 60 words.
- Not changed: the form source of `f5695.line18a` (the entry asks for it too). f5695.yaml is in v2 older-credits, so
  it can be added there if the lane wants transcription parity.
- Due: a question review.

**BUG-0798 (f8962 "immigrant"; abuse list).** Real [C base questions.yaml:3101,3491]. Fixed.
- `alien_below` prompt: "... a noncitizen lawfully present in the United States (green card and visa holders
  included) who could not get Medicaid in any month of 2025 because of their immigration status?" (26 → 41).
- `mfs_exception` help: "Abuse includes physical, psychological, sexual or emotional abuse, and efforts to control,
  isolate, humiliate or intimidate you; abuse of your child or another family member living with you can count too.
  ..." (34 → 50).
- Due: 2 question reviews.

**BUG-0863 (marriage definitions).** Real [C base questions.yaml:2690-2694, 2373]. Fixed.
- `household.married_dec31` help: "Living apart, or a divorce not final on December 31, leaves you married; a final
  decree of divorce, legal separation or annulment does not, unless you divorced only to file as unmarried and remarried
  in 2026. A common-law marriage, or one made abroad or under tribal law, counts where a U.S. state recognizes it; a
  domestic partnership or civil union does not. If your husband or wife died in 2025, answer No." (64 → 72).
- `dependent.ever_married` help: "Count a marriage that has since ended, a common-law marriage, and a marriage abroad or
  under tribal law that a U.S. state would recognize." (7 → 24).
- Kept out of the prompt: this is the second question of every interview, so a longer prompt costs every filer.
- Due: 2 question reviews, and a screen review for `dependent.ever_married`, since its help is shown with its tick [I].

**BUG-0864 (`other_only_spouse`).** Real [C base questions.yaml:2385]. Fixed: "... or a parent of the child other than
you and your husband or wife also lived with the child ..." (35 → 43). Due: a question review.

**BUG-0867 (January 1 birthday).** Real.
- Fixed for `dependent.age` only. Help: "Enter 0 for a baby born in 2025. A person born on January 1 counts as a year
  older on the December 31 before (born January 1, 2007: enter 19)." (8 → 30). Source: i1040gi, as quoted in the
  entry [U].
- **Not** changed: `person.age50_at_year_end`, `age55_at_year_end` and `simple_age_at_year_end`. amb.2025.ira_age50
  records the owner's choice to ask the age with no birth-date rule, because "the archived text states the day-before
  rule only for age 65" [C ambiguities/2025.yaml:1231-1240]. Stating the convention there would decide a registered
  ambiguity.
- **Owner check:** that reason sits uneasily with the i1040gi child-age sentence this fix relies on.
- **Closure in part.**

**BUG-0869 (`edu_over`).** Real [C base questions.yaml:3270-3275, 3360-3366]. Fixed in both `person.edu_over` and its
sibling `dependent.edu_over`.
- Prompt suffix: "(for the lifetime learning credit, only materials that had to be bought from the school)".
- Help: "A term beginning January to March 2026 and paid for in 2025 counts as a 2025 term. With only one such term,
  answer by that term alone. Count help and refunds received in 2025 or in 2026 before you file. A Yes ends the
  interview here."
- Words: person 42 → 57 and 37 → 46; dependent 31 → 46 and 37 → 46. **N10 over** (child aim 40). Kept because a
  lifetime-learning student counting outside books answers No and the refusal is missed.
- Source: i8863 p. 4 and p. 9, relayed [U]. Due: 2 question reviews.

**Old question-review lows, checked against the current bank (no patch here unless named above):**

| Entry | Now | Evidence |
|---|---|---|
| BUG-0554 | fixed by this patch | above |
| BUG-0555 | in part (redraft, v2, this patch); 19a and qmid_enabling remain | above |
| BUG-0568 | **still open, mostly real**. `ptc_files` 65+/blind is fixed by v2 (0861) [C v2/older.md]. The other 13 items were not re-read one by one | defer |
| BUG-0515 | **partly fixed by the redraft** | `carloan.requirements` help covers a replaced loan and a loan taken over at a death; `carloan.refi_whole` help covers a chain [C xint questions.yaml, bank text]. A rebate in `carloan.down` and requirement 2 "originated by you" remain |
| BUG-0530 | **partly fixed** | `sc.passive` help counts the spouse's work [C]. `sc.at_risk` still does not except qualified nonrecourse real property financing (over-refusal), and the other items are unchecked [U] |
| BUG-0558 | real | `retirement.months` is a Count with no bound seen; `retirement.box5` has no bank help [C forms/2025/retirement.yaml:1481; bank] |
| BUG-0559 | **partly fixed** | `scveh.after_jan19` now states the written-binding-contract rule [C bank]; the other items are [U] |
| BUG-0560 | real | `f8960.prior_2i` help still says "Answer No if you did not figure net investment income tax for 2024" [C bank] |
| BUG-0565 | real | `asset.cost` help says "adjusted basis" only for converted property, `asset.pct` is a Count (whole percent) [C forms/2025/asset.yaml:1005], and `asset.not179` has no 521 cooperative exception [C bank] |
| BUG-0575 | **partly fixed** | `sales.reported_basis` now names "box 1e of Form 1099-B" [C bank]. `sales.wash_loss` has no securities futures sentence. The residual rides with int-p18 |

## 4. Closure-entry drafts (text for `tools/new_bug.py --pending`; not in any patch)

Run each on the branch that lands the patch. `<PREFIX>` is that branch's prefix. The text is in the conventions of
tools/README.md:784-788 [C]. A "fixed" closure is recorded only when its patch lands.

### Fixed by older-ny-lows

```
python3 tools/new_bug.py "Closure: BUG-0853 is fixed: the New York estimated-tax gate names estate or trust allocations and the late question a skipped installment" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0853" --field "Closure=fixed" \
  --field "Evidence=ny_it201.ask.est_any's source adds 'or have estimated tax passed to you by an estate or trust' and its help names State, City and MCTMT payments; ny_it201.ask.est_late's prompt asks whether any installment was skipped, or any payment of yours or your spouse's late or short, and its source and label add 'skipped' (ny_it201i p. 22 line 75, Beneficiaries of an estate or trust; p. 23 line 81). Wording and source only; no value changes." \
  --field "Fix lines=ny_it201.ask.est_any, ny_it201.ask.est_late" --field "Tags=closure; new-york; question-wording"
python3 tools/new_bug.py "Closure: BUG-0854 is fixed: the New York use-tax question names the spouse and services, and its help the reservation purchase" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0854" --field "Closure=fixed" \
  --field "Evidence=Prompt: 'did you (or, on a joint return, your spouse) buy goods or services taxable in New York without paying New York sales tax on them'; help adds an untaxed purchase on an Indian reservation unless Oneida Nation tax was paid (ny_it201i p. 18, Line 59). Bank only." \
  --field "Fix lines=ny_it201.ask.owes_use_tax" --field "Tags=closure; new-york; question-wording"
python3 tools/new_bug.py "Closure: BUG-0855 is fixed: the special accrual question asks about income fixed in one year and reported in another" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0855" --field "Closure=fixed" \
  --field "Evidence=Prompt now 'income fixed in one year but reported federally in another, such as a 2025 bonus paid in 2026, or deferred pay or an installment-sale gain from before 2025 reported for 2025', matching the input's source (fixed and determinable in one tax year, reported federally in another). A Yes refuses, so a wider reading only over-refuses. Bank only." \
  --field "Fix lines=ny_it201.ask.special_accrual" --field "Tags=closure; new-york; question-wording"
python3 tools/new_bug.py "Closure: BUG-0856 is fixed: the real property credit question names furnishings, the subsidized part, the spouse and property owned in 2025" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0856" --field "Closure=fixed" \
  --field "Evidence=Prompt: 'was the rent you (or, on a joint return, your spouse) paid yourselves $450 a month or less on average, not counting heat, gas, electricity, furnishings or meals? Or was all the real estate either of you owned in 2025 worth $85,000 or less?'; help: 'Leave out any part of the rent paid by a subsidy, such as Section 8.' (ny_it214i p. 1 conditions; IT-214 lines 3 and 11). The co-op apartment clause of the proposed fix was not added (no archived IT-214 text names it)." \
  --field "Fix lines=ny_it201.ask.real_property_credit" --field "Tags=closure; new-york; question-wording"
python3 tools/new_bug.py "Closure: BUG-0858 is fixed: the U.S.-obligation question names agency obligations and the heading names the spouse" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0858" --field "Closure=fixed" \
  --field "Evidence=Group ny_interest heading: 'Did any of your (or, on a joint return, your spouse's) interest or dividends come from these?'; tick 'U.S. government bonds, notes or bills, or a fund holding them'; prompt names 'U.S. government obligations, such as Treasury bills, notes or bonds, savings bonds, bonds of a U.S. government agency' (ny_it201i p. 9, Line 28). A Yes refuses. Screen review of ny_interest rerun with the change." \
  --field "Fix lines=ny_it201.ask.us_obligation_interest" --field "Tags=closure; new-york; question-wording"
python3 tools/new_bug.py "Closure: BUG-0859 is fixed: the inflation-check question is asked with a state refund on Schedule 1 line 1 as well as with line 9" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0859" --field "Closure=fixed" \
  --field "Evidence=ny_it201.has_other_income is any[s1.line1 > 0, s1.line9 not 0]; the prompt asks whether a New York State inflation refund check was included in federal income 'as a state tax refund or as other income' and names the spouse (ny_it201i p. 8, Line 25). A line 9 that nets to zero under a line 8a loss is left (rare)." \
  --field "Fix lines=ny_it201.has_other_income, ny_it201.inflation_if_other_income, ny_it201.ask.inflation_check" --field "Tags=closure; new-york; gate"
python3 tools/new_bug.py "Closure: BUG-0860 is fixed: the New York public-job question asks for a 2025 Form W-2 from a New York public employer" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0860" --field "Closure=fixed" \
  --field "Evidence=Source: 'Did you (or, on a joint return, your spouse) get a 2025 Form W-2 from New York State, a New York local government or another New York public employer?'; help adds a public hospital or library and a fire district (ny_it201i p. 8, Line 21: 414(h) contributions 'if shown on any federal Form W-2')." \
  --field "Fix lines=ny_it201.ask.public_job" --field "Tags=closure; new-york; question-wording"
```

Add "Siblings checked" fields when the commands are run. For each, name the sibling inputs read in this lane:
`line75_amount` (0853), `use_tax_st141` (0854), `moved_in`/`moved_out` (0855), `ny_interest` group (0858),
`gate.line25` (0859) and `414h` (0860).

### Fixed by older-scha-lows

Same field pattern for each. The "Evidence" texts:

- **BUG-0458 and BUG-0924** (one closure, `Closes=BUG-0458, BUG-0924`):
  - The bank prompt asks "Do you (or, on a joint return, your spouse) leave out of this 2025 return any income earned
    abroad, in Puerto Rico or in American Samoa?" The help says "Pay received in 2025 for work done abroad in 2024
    counts." The "50 states" sentence is dropped.
  - The form source and label read "or exclude income from sources within Puerto Rico" (i1040gi p. 98; i2555 p. 3,
    Income earned in prior year).
  - Screen review of `sa.excluded_income` rerun.
  - Fix lines: `sa.excluded_income`.
- **BUG-0801:** the `sa.line1` source and bank list add the fourth category of i1040sca p. 2 (would be a dependent
  except that you or your spouse can be claimed as a dependent). Fix lines: `sa.line1`.
- **BUG-0807:** the `sa.home_owner` help counts a home bought on a land contract while the seller holds the deed. The
  tick is unchanged. Fix lines: `sa.home_owner`.
- **BUG-0816:** the gate help says a charge with any value-based part is a Yes, and only a wholly flat or weight
  charge is not (i1040sca p. 6, Line 5c). Fix lines: `sa.personal_property_tax_any`.
- **BUG-0818:**
  - `gift.special` refuses property other than qualified appreciated stock given to a private nonoperating
    foundation, and tangible personal property put to an unrelated use (p526, Capital Gain Property, Exceptions 1 and
    3a).
  - The bank list names a gift of only the use of property, which p526 counts as a partial interest, already in the
    refusal.
  - Refused, not computed.
  - Fix lines: `gift.special`.
- **BUG-0819:** the `sa.medical_any` help counts costs an estate paid within a year after a death, for the final
  return (i1040sca p. 1; p502). Fix lines: `sa.medical_any`.
- **BUG-0820:** the `sa.spouse_extra` help defines blind (i1040gi p. 33), and the prompt reads "with no 2025 return
  filed for them". A spouse who died at 65 or older was born before January 2, 1961, so the death case needs no words.
  Fix lines: `sa.spouse_extra`.

Command form for each (shown for 0819):
```
python3 tools/new_bug.py "Closure: BUG-0819 is fixed: the medical gate help counts estate-paid costs on a final return" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0819" --field "Closure=fixed" --field "Evidence=<text above>" \
  --field "Fix lines=sa.medical_any" --field "Tags=closure; schedule-a; wording"
```

### Fixed by older-credits-lows

- **BUG-0554 fixed:**
  - Fourteen f5695 "other" or "such" amount prompts now name the criterion: Energy Star; Energy Star Most Efficient;
    the same efficiency tier; the same standard; the same 75% rating (i5695 pp. 6-7).
  - Fix lines: `f5695.line19d_i`, `19d_ii`, `19e`, `20a_ii`, `20a_iii`, `20a_iv`, `20b`, `22b`, `23a_ii`, `23b`,
    `24b`, `29b`, `29d`, `29f`.
- **BUG-0555 fixed in part** (`Closes=BUG-0555 in part`):
  - The 23b help excludes heat pump water heaters.
  - 26b counts only audits with the required report.
  - Earlier fixes: the 21a tense (v2 older-credits), and the heat-pump and audit ticks (redraft).
  - Left: the 19a ranking and `qmid_enabling` (refusal only).
- **BUG-0794 fixed:** the `f5695.line18a` prompt leaves out siding, drywall and anything that also holds up the house
  or is a finished surface (i5695 p. 5 Caution). The form source is unchanged; record that in the entry.
- **BUG-0798 fixed:** `f8962.alien_below` says "noncitizen lawfully present ... (green card and visa holders included)
  ... in any month of 2025". The `f8962.mfs_exception` help gives the i8962 p. 7 list and the household-member
  sentence.
- **BUG-0863 fixed:** the `household.married_dec31` and `dependent.ever_married` help carry common-law, foreign or
  tribal marriage, and say that living apart does not end a marriage (p501 p. 6).
- **BUG-0864 fixed:** "a parent of the child other than you and your husband or wife".
- **BUG-0867 fixed in part:**
  - `dependent.age` help states the January 1 rule.
  - The `person.*_at_year_end` questions are left as they are under amb.2025.ira_age50 (owner decision, Stage 16).
- **BUG-0869 fixed:** `person.edu_over` and `dependent.edu_over` limit course materials for the lifetime learning
  credit and count a January to March 2026 term paid in 2025 (i8863 pp. 4, 9).

### The closure candidates (bookkeeping; no patch needed)

```
python3 tools/new_bug.py "Closure: BUG-0465 is fixed: eic.eligible is a nested choose and no EIC input is held in early_completion" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16, checking stale open entries on the coverage-expansion tree." \
  --field "Closes=BUG-0465" --field "Closure=fixed" \
  --field "Evidence=forms/2025/eic.yaml eic.eligible (line 1206) is 'op: choose' with alternatives, the gate wave's pattern the entry asked for; tools/interview_rules_baseline.json early_completion lists only sa.elect_itemize and person.work_ssn, so none of the four EIC inputs is held. Not re-run here (no engine runs tonight); interview-rules at the next check-all confirms it." \
  --field "Tags=closure; record-drift"
python3 tools/new_bug.py "Closure: BUG-0532 is fixed: the Form 1095-A VOID question names a later CORRECTED form" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0532" --field "Closure=fixed" \
  --field "Evidence=interview/2025/questions.yaml f1095a.void prompt (line 2851): 'Is the VOID box at the top of this form ticked, or did the Marketplace later send another form, marked VOID or CORRECTED, for the same plan?', which covers an earlier CORRECTED form replaced by a second one (i8962 p. 2). Fixed by the interview redraft." \
  --field "Tags=closure; record-drift"
python3 tools/new_bug.py "Closure: BUG-0729 is fixed: dependent.us_half's military sentence names the spouse on a joint return" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0729" --field "Closure=fixed" \
  --field "Evidence=interview/2025/questions.yaml dependent.us_half help (line 2493): 'your home counts as there while you (or, on a joint return, your spouse) are abroad on military duty' (i1040gi p. 44). Fixed by the interview redraft; the source line in forms/2025/dependent.yaml was not re-read here." \
  --field "Tags=closure; record-drift"
python3 tools/new_bug.py "Closure: BUG-0893 is superseded: Schedule 1 line 8u and s1.inmate_amount no longer exist" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0893" --field "Closure=superseded" \
  --field "Evidence=forms/2025/s1.yaml has no s1.line8u and no s1.inmate_amount (0 matches); s1.inmate_wages is an operand of s1.line8_other (line 656), so inmate pay refuses at Schedule 1 line 8 (BUG-0766's fix). No amount is counted twice. Computing inmate wages is TASKS T-336." \
  --field "Tags=closure; obsolete"
python3 tools/new_bug.py "Closure: BUG-0757 is fixed: the slice profiles were retired" --pending <PREFIX> \
  --field "Caught by=lane A4-lows-older (claude-opus-5-5, judgment), 2026-11-16." \
  --field "Closes=BUG-0757" --field "Closure=fixed" \
  --field "Evidence=interview/2025/ holds no social-security.yaml, sales.yaml or stage4.yaml (listing: conflict_checks.yaml, coverage, full.yaml, gate_frequencies.yaml, personas, questions.yaml, refusal_notes.yaml). The entry's own Resolution field records the retirement; tools/bug_status.py reads Resolution as a proposal, so it stayed open." \
  --field "Tags=closure; record-drift"
```

- **BUG-0092:** use the draft in `patches/older-ny.md:135-150` unchanged. Its evidence was checked there; v2/older.md
  section 5 says it still stands.
- **BUG-0647:** owner's choice, not drafted as a command. The 2026 operation exists [C changes/2026/tcw.yaml:6
  `change: BUG-0647`]. Closing it now says "fixed" before 2026 is adopted. The alternative, which I recommend [I], is
  `Closure=fixed` with `Closes=BUG-0647 in part`, then full closure at the 2026 adoption.

## 5. Deferred (not in any v3 patch here)

| Entry | Why | Next step |
|---|---|---|
| BUG-0852 (SCRA, MFS civilian spouse, PHS, NOAA) | M: a new NY question at order 1000, or the active-duty gate widened to married filers, plus fixtures. The entry offers two designs | Owner or lane picks the design; the 0902 Coast Guard wording rides with it |
| BUG-0857 | Owned by lane int-lows (`patches/v3/int-lows.patch` rewrites `has_tax_exempt` and the help, with fixture `ny.refuse.line20_premium`) | Record its closure with int-lows |
| BUG-0762 (NY household credit MFS) | M, amount-affecting: a new question or the in-range test dropped. **Owner** chooses | Upgrade candidate, as lows.md says |
| BUG-0763 (IT-2 boxes shown $0) | `ny_it2.yaml` is in no patch, so it would start a new transcription and render round for presentation only | At ny_it2's next change |
| BUG-0750 (W-2c box) | Needs a federal W-2c fact that does not exist | Leave as a known presentation gap |
| BUG-0424 (first NY reviews umbrella) | Per item (T-244); not re-read item by item | At the NY forms' next change |
| BUG-0768 and BUG-0802 (Schedule A line 6) | M: a new refusing input on `sa.unsupported`. One input could serve both ("generation-skipping tax on a trust distribution, or foreign tax left out of the credit for holding period or related payments") | Draft with the next sa.yaml model change |
| BUG-0774 (ftc election for a Form 2555 filer) | M (new narrower input), and it rests on owner decision D3 (scout-form-1116). It is reachable only where `sa.excluded_income`'s readers do not refuse, for example a standard-deduction filer with no credits [I] | With D3 |
| BUG-0508 | `retirement.ben_shared` is asked only after a death (code 4) [C forms/2025/retirement.yaml:978-990], so a living retiree's joint and survivor annuity with two survivors is not reached. That is a gate change, not help | At retirement's next change |
| BUG-0568 | 14 items over several inputs; only `ptc_files` is fixed (v2) | Next change of the dependent questions |
| BUG-0555 residual, BUG-0867 residual | See section 3 | as stated |
| BUG-0386 f5695 items | #3 roof parts partly met by 0794 (the "holds up the house" sentence). #5 and #6 are met by the 26a help and prompt [C base questions.yaml:6269-6277]. #4 (dual-function storage) not checked | Umbrella stays open (T-211) |

## 6. What to run when the machine is free, and the reviews due

- `node engine/dist/main.js test-fixtures` and `test-fixtures --ny`. No expected value should change [I]. The NY gate
  change (0859) adds an asked question that takes its default (false).
- `interview-coverage --write`, then `--check`; `tick-groups` (`ny_interest` tick changed).
- `draft-walk` for:
  - an NY filer with a state tax refund on Schedule 1 line 1;
  - an NY public employee;
  - a Form 2555 filer with 2024 pay received in 2025;
  - an energy-credit filer with three doors.
- **Coverage rows to add (not drafted):**
  - 0859: state refund on line 1, check Yes, expect refused `ny_it201.gate.line25`;
  - 0818: a group given to a private nonoperating foundation, expect refused `gift.special`'s gate.
- **Reviews due:**
  - Question reviews: every input changed above, about 45, most of them short amount prompts.
  - Transcription: `ny_it201` (`est_any`, `est_late`, `public_job`, `has_other_income`,
    `inflation_if_other_income`); `sa` (`excluded_income`, `line1`); `gift` (`gift.special`, new to the round).
  - Screen reviews: `ny_interest` (tick and heading), `sa.excluded_income` (prompt; the entry asks for it), and
    `dependent.ever_married` [I, help shown with its tick].

## 7. Files

- Patches: `patches/v3/older-ny-lows.patch`, `older-scha-lows.patch`, `older-credits-lows.patch`.
- Scratch: `scratch/round4-lows-older/`:
  - `{ny,scha,cred}/a` (xint plus the v2 patch) and `/b`;
  - `edit_ny.py`, `edit_scha.py`, `edit_cred.py`, `trim.py`;
  - `count.py`;
  - `t/all` (all v2 and v3 patches applied in sequence), `t/s17a` (the 0817a path);
  - the entry extracts `*.txt`.
