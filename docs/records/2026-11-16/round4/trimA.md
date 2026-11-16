# Lane T-trimA: N10 trims for the sa, gift, asset, rental, rprop, royalty, household, dependent, person, k1p and k1s overruns

claude-opus-5-5, judgment, year 2025, us. Written 2026-11-16. Read only on the work tree
`P/scratch/b-chain/work/` (never edited). No build, walk, test, review or paid call. Scratch: `P/scratch/round4-trimA/`
(`extract.py` pulls the current texts, `build.py` writes the JSON, `q.py` greps the sources, `rows.txt` and
`counts.txt` are their output).
**[C]** = checked in this session against the named file; **[I]** = my inference.

## Summary

- **My share of fix-round.md section 7: 54 rows** (us only; no `sche.` or `f8582.` row is in the table). 51 rows get
  a trim. 3 rows are kept as they are: `gift.special`, `sa.line1` and the `dependent.ptc_files` prompt.
- **Two R5 fixes** for jr's texts: the `household.spouse_cp_domicile` help and the f1040 `cp_marriage_ended` remedy.
- **`P/round4/trimA.json`** has 52 edits. `build.py` reads every `"old"` from the work tree [C], so each matches exactly.
  - `"old"` is the **parsed YAML scalar**, not the raw file text, because many values are folded across lines. Apply the
    edits with a YAML-aware script, or match on the parsed value.
  - `field` is `prompt` or `help` for the bank (`interview/2025/questions.yaml`); `source` for a form line's
    `expr.source`; and `remedy` for the f1040.line1a refusal whose `when` is `household.cp_marriage_ended`.
  - `words_old` and `words_new` count prompts and sources **as shown**, frame first, with the engine rule that
    n10.py uses. Help is counted raw.
- **After the trims, 42 of the 51 trimmed rows are at or under the limit.**
  - The 9 rows still over, and the 3 rows left unchanged, are listed under "Kept overruns", each with the wrong
    answer that cutting further would cause.
  - Eight of the 9 are per-entry parents or tick members, whose limit is still open (section 7 caveats; owner plan
    item 5). Five of them (31, 31, 37, 30 and 27 words) would pass at 40.
- **No model change was made.** Six restructurings that would need one are listed as proposed follow-ups.
- **Two changes go beyond trimming. Both are flagged in the "why" field:**
  - `household.married_dec31` gains "and not remarried". The current "If your husband or wife died in 2025, answer
    No" is wrong for a widow or widower who remarried in 2025: "If you remarried before the end of the tax year, you
    can file a joint return with your new spouse" [C p501.cols.txt:236].
  - `k1p.t6` writes the spouse clause as "you or your spouse, filing jointly or not" so that it fits in 40 words.
    BUG-0886's standard wording is "(or your spouse, whether or not you file jointly)". Keeping that wording verbatim
    costs 41 words. The owner or the reviewer should pick one.

## 1. Table

Limits: a parent prompt is 25, a child prompt 40 and help 40. Per-entry and tick-member parents are marked, because
their limit is open.

| Entry | Field | Old | New | Limit | Result |
|---|---|---|---|---|---|
| k1p.upe | source | 26 | 23 | 25 (tick, per-entry) | in |
| k1p.interest_buy | source | 29 | 25 | 25 (tick, per-entry) | in |
| k1p.t6 | source | 44 | 39 | 40 | in |
| k1p.basis_carry | source | 26 | 24 | 25 (tick, per-entry) | in |
| k1p.fuel_2024 | source | 27 | 25 | 25 (tick, per-entry) | in |
| gift.special | prompt | 141 | — | 25 | **kept** |
| sa.charity_limited | help | 42 | 30 | 40 | in |
| sa.excluded_income | prompt | 26 | 25 | 25 (tick) | in |
| sa.dependent | help | 56 | 40 | 40 | in |
| sa.spouse_extra | help | 43 | 29 | 40 | in |
| sa.home_owner | help | 47 | 40 | 40 | in |
| sa.mortgage_interest | help | 78 | 39 | 40 | in |
| sa.mortgage_other_use | help | 41 | 39 | 40 | in |
| sa.line1 | prompt | 325 | — | 40 | **kept** |
| sa.personal_property_tax_any | help | 42 | 40 | 40 | in |
| sa.line5b | help | 52 | 39 | 40 | in |
| sa.state_tax_other_any | prompt | 49 | 43 | 25 (tick) | **over** |
| sa.state_tax_other_any | help | 43 | 36 | 40 | in |
| sa.medical_any | help | 51 | 40 | 40 | in |
| sa.line11 | prompt | 48 | 40 | 40 | in |
| sa.line11 | help | 67 | 40 | 40 | in |
| person.household_wages | source | 47 | 40 | 40 | in |
| dependent.other_only_spouse | help | 43 | 38 | 40 | in |
| household.married_dec31 | help | 72 | 60 | 40 | **over** |
| household.community_property | prompt | 26 | 25 | 25 | in |
| household.spouse_cp_domicile | help | 41 | 19 | 40 | in (R5) |
| f1040.line1a (cp_marriage_ended) | remedy | 50 | 47 | — | R5 |
| household.credit_disallowed | prompt | 43 | 37 | 40 | in |
| person.edu_over | prompt | 57 | 39 | 40 | in |
| person.edu_over | help | 46 | 40 | 40 | in |
| dependent.edu_over | prompt | 46 | 28 | 40 | in |
| dependent.edu_over | help | 46 | 40 | 40 | in |
| dependent.ptc_files | prompt | 40 | — | 25 | **kept** |
| dependent.ptc_files | help | 44 | 38 | 40 | in |
| asset.listed | prompt | 60 | 54 | 25 (per-entry) | **over** |
| k1s.mp_other | source | 43 | 40 | 40 | in |
| k1s.not_at_risk | prompt | 41 | 36 | 40 | in |
| k1s.interest_buy | source | 29 | 25 | 25 (tick, per-entry) | in |
| rental.days_fair | prompt | 35 | 31 | 25 (per-entry) | **over** (in at 40) |
| rental.personal_any | help | 45 | 40 | 40 | in |
| rental.days_personal | prompt | 48 | 43 | 25 (per-entry) | **over** |
| rental.services | source | 27 | 24 | 25 (tick, per-entry) | in |
| rental.part_home | prompt | 28 | 25 | 25 (tick, per-entry) | in |
| rental.amt12 | help | 49 | 40 | 40 | in |
| rental.amt16 | help | 49 | 40 | 40 | in |
| rental.prior_any | source | 33 | 31 | 25 (per-entry) | **over** (in at 40) |
| rental.prior_not_active | source | 44 | 39 | 40 | in |
| rprop.basis | prompt | 43 | 37 | 25 (per-entry) | **over** (in at 40) |
| rprop.disposed | source | 26 | 25 | 25 (tick, per-entry) | in |
| rprop.fast | source | 32 | 30 | 25 (tick, per-entry) | **over** (in at 40) |
| rprop.ads | source | 26 | 25 | 25 (tick, per-entry) | in |
| rprop.basis_changed | source | 32 | 25 | 25 (tick, per-entry) | in |
| rprop.credit | source | 31 | 25 | 25 (tick, per-entry) | in |
| rental.not_at_risk | source | 42 | 40 | 40 | in |
| royalty.expenses_any | source | 30 | 27 | 25 (per-entry) | **over** (in at 40) |

## 2. Kept overruns: the wrong answer a further cut would cause

| Entry | Now | What stays, and who answers wrongly without it |
|---|---|---|
| gift.special (prompt) | 141 | Eleven refusing items, and each one names a gift that needs an appraisal or special treatment. Dropping any item computes a wrong deduction for its owner. For example, a donated car without Form 1098-C treatment, or art the charity will not use, which is limited to basis. The items have nothing in common, so wording cannot cut them; only the structure can (follow-up F1). |
| sa.line1 (prompt) | 325 | Each block is a rule the amount needs: whose costs count, seven leave-outs, Marketplace and long-term-care amounts, earlier-year reimbursements. Cut any one and the deduction is overstated or understated for its filer. For example, HSA-paid costs would be counted twice. The rules belong in children (F2); moving them to help would break N10's "rule goes into a child, not help". |
| dependent.ptc_files (prompt) | 40 | The thresholds are what the filer answers by. A teen with $9,000 of pay and no thresholds in view might say "had to file", which adds their income to household income and understates the PTC. "(a taxable scholarship is pay)" stops a student counting the scholarship as unearned, crossing $1,350 and answering Yes wrongly. The parent-plus-child split is F3. |
| household.married_dec31 (help) | 60 | Each guard prevents a wrong status. **Living apart** stops a separated filer answering No, then filing single or HOH without the tests [C p501.cols.txt:234 "married and living apart but not legally separated"]. **Not final by December 31** stops a filer whose divorce became final in early 2026 answering No. **Decree of separation** stops a legally separated filer answering Yes [C :222]. **Sham divorce** stops a filer answering No who must file as married [C :226]. **Common-law** stops a filer in a recognised common-law marriage answering No [C :233]. **Domestic partnership or civil union** stops a registered partner answering Yes and filing jointly [C :224]. **Widowed** stops a Yes that skips spouse_died_this_year. Dropped: annulment (an annulled filer answers No anyway) and "abroad or under tribal law" (it affirms a Yes those filers already give). F7. |
| asset.listed (prompt) | 54 | The entertainment-equipment item and the pre-2018-computer item have different exceptions [C i4562.cols.txt:50, exception 1 "used exclusively in a taxpayer’s trade or business or at the taxpayer’s regular business establishment"; exception 2, a computer "used exclusively at a regular business establishment"]. Merging them would let a computer used only for business at home answer No. F4. |
| sa.state_tax_other_any (prompt) | 43 | Tick member: the label carries the screen. Kept: "a past refund applied to 2025" (a filer who applied a state overpayment does not think of it as paying, would answer No, and loses the deduction), and the disability, unemployment or family leave fund (A7: NJ and PA SUI, [I, relayed from wording-redteam A7, i1040sca.cols.txt:85]). Settled by owner plan item 5. |
| rental.days_personal | 43 | Repair days [C p527.cols.txt:894], the 12-month main-home rule and its sale exception [C :897-901]. Each changes the personal-day count and so the vacation-home limit. F6. |
| rental.days_fair | 31 | "including days you also used it" is the model's overlap design (wording-redteam E). "Leave out days it was only offered for rent": a landlord counting vacant days inflates the rental ratio [C p527.cols.txt:844, "Any day that the unit is rented at a fair rental price"]. |
| rental.prior_any | 31 | "(or, on a joint return, your spouse's)": on a separate return the spouse's suspended loss is not the filer's. "even a separate one": on a joint return, a loss held back on either spouse's earlier separate return counts. "(not deducted)" glosses "held back". |
| rprop.basis | 37 | The converted-home rule (smaller of value and cost) is common among landlords who rented out a former home, and is needed without opening help. F5. |
| rprop.fast | 30 | The plain gloss before the official names (N6). Both items refuse. |
| royalty.expenses_any | 27 | "such as" keeps the list open. A closed list would make a filer whose payer withheld something unlisted answer No. |

## 3. Red team of every cut

Format: **cut** → who could now answer wrongly → source. "None" means that no answer depends on the cut text.

**k1p**
- `upe`: "yourself" dropped → none (the subject is "you"). Kept: not paid back, and required by the agreement [C
  i1040se.cols.txt:253 "unreimbursed … if you were required to pay these expenses under the partnership agreement"].
- `interest_buy`, `k1s.interest_buy`: "you borrowed" → "borrowed" → none ("Did you pay interest" anchors it). Both
  purposes are kept [C i1040se.cols.txt:231/243 "to buy an interest in, or make a contribution to the capital of"].
- `t6`:
  - "in any 3 years before 2025" → "in any 3 earlier years" → none [C i1065sk1.cols.txt:317 "any 3 tax years (whether or
    not consecutive) preceding the tax year"]. The list of fields is unchanged (same line).
  - The spouse clause is reworded (see Summary).
- `basis_carry`: "in it" dropped → none.
- `fuel_2024`: reworded only.

**sa**
- `charity_limited`: "outside what this tool prepares" dropped → none. The register forbids "this tool" (protocol 1.3),
  and "A Yes ends the interview here" stays.
- `excluded_income`: "2025" dropped from "this 2025 return" → none (the return is the 2025 return; the help keeps the
  2024-work-paid-2025 rule).
- `dependent`: every guard is kept.
  - Can, not do [C i1040gi.cols.txt:345 "Could you be claimed"].
  - Income test with the disability exception [C p501.cols.txt:755 "gross income for the year must be less than $5,200";
    :554 "Permanently and totally disabled at any time during the year, regardless of age"].
  - Refund-only filer: "to get back tax withheld" → "for a refund" → none. The source covers "a refund of withheld
    income tax or estimated tax paid" [C i1040gi.cols.txt:345], so "a refund" is if anything closer.
- `spouse_extra`: the explanatory sentence is dropped → none. The blindness test stays [C i1040gi.cols.txt:765].
- `home_owner`: articles and "apartment" dropped → none. The land contract and the seller's deed are kept.
- `mortgage_interest`:
  - Dropped: the Form 1098 gloss, the gloss of boxes 1 and 6, and "the rental part is asked with the rental" → none.
    The prompt says "Add boxes 1 and 6 of each Form 1098 from your lender".
  - Kept: the two-home limit [C i1040sca.cols.txt:270 "secured by your main home or second home"], box 4 [C
    i1098.cols.txt:125 "Box 4. Refund of Overpaid Interest"], and A1's rental split.
  - "for part of 2025" → "in 2025" → none ("for the rest of the year" carries it).
- `mortgage_other_use`: reworded only. The source test is unchanged [C i1040sca.cols.txt:279 "used to buy, build, or
  substantially improve the home"].
- `personal_property_tax_any`: reworded only [C i1040sca.cols.txt:192-193, value only; the registration example].
- `line5b`:
  - "Zero if you paid none" dropped → none (an amount box takes 0).
  - The lender sentence keeps "what it paid in 2025", so escrow deposits are not counted [C i1098.cols.txt:149 "Box 10.
    Other … such as real estate taxes, insurance paid from escrow"].
- `state_tax_other_any`:
  - Prompt: "with a state return" dropped → none. It is tax not taken from pay, and the amount child itemises it.
    "made in 2025" moves to the amount child, which asks "estimated payments made in 2025" [C work questions.yaml
    sa.state_tax_other]. A filer whose only other payment was the January 2026 instalment now answers Yes, and then
    gives 0 at the child: one extra step, no wrong value.
  - Help: the fund wording moved into the prompt; SDI, SUI and FLI are kept.
- `medical_any`: "less what insurance paid back" dropped → none (the prompt says "after what insurance paid"). The
  decedent's one-year limit is kept [C p502.cols.txt:99 "paid within the 1-year period beginning with the day after the
  date of death"].
- `line11`:
  - "cash, checks, card payments" → covered by "money".
  - Moved up from the help: U.S. charities that work abroad count. "a charity abroad does not" is implied by "U.S.
    charities" [C p526.cols.txt:248 "certain contributions to a qualified organization for use in a program conducted by
    a foreign charity may be deductible"].
  - Every help exclusion is kept: quid pro quo, tuition, club dues, gifts to people, refunded gifts, state-credit part
    [C p526.cols.txt:100], and records.
  - Pre-existing, not changed: the treaty exceptions for Canadian, Israeli and Mexican charities [C p526.cols.txt:83].

**person, dependent, household**
- `person.household_wages`: "as a household employee" dropped → none. The plain definition follows it, and the parent
  `scope.household_pay` uses the same one [C work questions.yaml]. "for it" is dropped from the prompt and kept in the
  help. A household that gave a W-2 for only part of its pay is a residual [I, rare].
- `dependent.other_only_spouse`: reworded only. The relative list is whole.
- `household.married_dec31`: see section 2.
- `household.community_property`: one "in" dropped → none. "At any time" and the domicile clause are kept.
- `household.spouse_cp_domicile` (R5): dropped "Count a marriage that ended in 2025 …" and "Answer No if you were not
  married in 2025".
  - [C, by script over the work tree]: only `household.mfs_community_property` and `household.hoh_cp_married` read
    `household.cp_any`, and nothing else reads the gate line.
  - So only MFS filers and married HOH filers reach the question.
  - An MFS filer whose spouse died in 2025 is covered by the prompt's "while you were married".
  - A Yes refuses on both paths, so "A Yes ends the interview here" stays.
- `f1040.line1a` remedy (R5): "with either of you living in or having a permanent home in" → "and lived in, or had your
  permanent home in". `cp_marriage_ended` reaches the refusal only through `cp_not_joint` → `cp_unmarried` on the
  filer's own `community_property` [C work household.yaml, cp_not_joint, false → household.no]. jr's domicile
  widening is kept, because the parent asks about domicile.
- `household.credit_disallowed`: articles dropped; "to fix" → "for". All three credits and the exception are kept.
- `person.edu_over`, `dependent.edu_over`:
  - The lifetime-learning materials rule moves from the prompt to the help, which is pure wording [C
    i8863.cols.txt:59 "only if required to be paid to the institution as a condition of enrollment"]. Who could now
    answer wrongly: a lifetime-learning claimant who does not open the help and counts off-campus books. The term's
    expenses are then overstated, and a true Yes (refuse) becomes a No. This is the one cut that relies on help; F8
    proposes a child.
  - The early-2026 term is kept [C i8863.cols.txt:48 "treat an academic period beginning in the first 3 months of 2026
    as if it began in 2025"], and so is "in 2025 or 2026 before you file" [C :86-87].
  - Dropped: "With only one such term, answer by that term alone" → none. The prompt's "any school term … that term's"
    already compares term by term.
- `dependent.ptc_files` (help): every figure is kept [C i1040gi.cols.txt:165].

**asset, k1s**
- `asset.listed`: "you began using" → "first used" → none. See section 2.
- `k1s.mp_other`: "nearly all the work in it" → "almost all its work" → none [C i1120ssk.cols.txt:71 "substantially all
  the participation"]. The 100- and 500-hour tests are kept, and the spouse clause is verbatim.
- `k1s.not_at_risk`: "another owner, anyone else with a stake" → "anyone with a stake" → none, because an owner has a
  stake [C i6198.cols.txt:33 "a person having an interest in the activity other than as a creditor or who is related
  … to a person … having such an interest"]. Protection from loss is kept [C :34].

**rental, rprop, royalty**
- `rental.personal_any`: "brother or sister" → "sibling". This also brings in half siblings, which the old text missed
  [C p527.cols.txt:872 "your spouse, siblings, half siblings, ancestors … lineal descendants"]. The 12-month clause (A2)
  is kept. Pre-existing residual: great-grandparents are not named (ancestors).
- `rental.services`: "a manager or staff for you" → "someone for you" → none (the help still names them). A cleaning firm
  you hire is services for you as well [I].
- `rental.part_home`: the examples are folded into the noun phrase → none.
- `rental.amt12` and `amt16`: reworded. The condition ("not counted as days you used it") and the split are kept (A1).
- `rental.prior_not_active`: "a tenth" → "10%". The tests are the same [C i8582.cols.txt:78 "your interest (including
  your spouse's interest) in the activity was less than 10% (by value)"].
- `rental.not_at_risk`: "or other regular lender" → "or regular lender" → none (the help names banks, government and
  regular lenders) [C i6198.cols.txt:30, 34].
- `rprop.disposed`, `ads`, `basis_changed`: reworded only.
- `rprop.credit`: both examples are kept [C i4562.cols.txt:137 "Deduction for removal of barriers to the disabled and the
  elderly. • Disabled access credit"].
- `rprop.fast`: "any of its cost" → "any cost" → none.
- `royalty.expenses_any`: "did the payer take any out" → "were any taken out" → none.

## 4. Proposed follow-ups (model changes; not made)

- **F1. `gift.special`.** Split it into per-entry tick inputs: one `gift_special` group of at most 6, and a second
  group or children. Keep `gift.special` as a derived Bool (technique 3.1) so that the refusal and the fixtures stay.
  The 141-word screen read for every noncash group becomes one tick screen.
- **F2. `sa.line1`.** Split the amount into a short amount prompt plus children or tick screens:
  - whose costs (only when someone other than you, your spouse and your dependents is involved);
  - the HSA, MSA or employer pretax leave-outs;
  - Marketplace premiums (gate on a Form 1095-A, already asked);
  - long-term care premiums (gate on age).
- **F3. `dependent.ptc_files`.** A parent "Did this dependent have income of their own in 2025?" with the thresholds in
  a child. Most dependents leave at the parent.
- **F4. `asset.listed`.** Ask the computer item only when the asset kind allows a computer, or as its own child.
- **F5. `rprop.basis`.** A child, "Did you use it yourself before renting it?", carrying the smaller-of rule. The parent
  becomes "Your share of what it cost, not counting the land."
- **F6. `rental.days_personal`.** Move the 12-month main-home rule to a child of `personal_any`: "Was it your main home
  before or after 12 months in a row of renting it?"
- **F7. `household.married_dec31`.**
  - Ask `household.spouse_died_this_year` before `married_dec31` (a bank `seq` change; it changes walks). The widowed
    sentence can then go.
  - Possibly put the sham-divorce rule behind a refusing child, asked only of a filer whose divorce became final in
    December 2025.
- **F8. `edu_over`.** If the owner judges the help-only lifetime-learning materials rule unsafe, add a child for
  lifetime-learning claimants.

**Pre-existing findings (not trims; outside the brief, for the owner):**
- `sa.spouse_extra` prompt: the source adds "and can't be claimed as a dependent on another person's return" [C
  i1040gi.cols.txt:762, 843], and the prompt omits it. Whether another question asks it was not checked [I].
- `sa.line11`: there is no path for the treaty charities [C p526.cols.txt:83]. The wording-redteam's treaty-charity
  owner decision covers this.

## 5. What this makes due (no extra round)

- Every form touched here is already due this round (fix-round.md section 6): k1p, k1s, person, rental, rprop,
  royalty, f1040 and household. The form `source` edits add lines to those forms' line-scoped transcription and render
  reviews.
- The bank edits fall within the question reviews of changed entries.
- **Run after applying:**
  - tick-groups (tick members' prompts changed, though no label did);
  - interview-coverage (no expected end can change, because no model change was made [I]);
  - the build's wording check;
  - draft-walk of personas 03, 04, 07 and 08 (Schedule A, rental, dependents).
- **Not run:** any check, walk or review. All word counts are from `build.py` [C]. Every "who could answer wrongly" is
  my judgment [I].
