# Lane notes: 4b (saving for retirement, and the person facts)

Branch `lane/l4b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call. Form files owned: `person`, `ira`, `f5329`, `f8606`, `f8880`. Read with `NORMS.md` and `MAP.md` (Part 3,
lane 4b).

**For a successor:** the steps below are in the order done; each "Done" step is committed and passed
`tools/draft_check.sh --quick` unless it says otherwise. "Not done" at the foot is the ranked remainder. Scratch
scripts used for the mechanical rewrites are in `docs/provisional/lanes/l4b_work/` (they are one-shot; kept so the
rewrite of the fixtures can be read and repeated).

## Steps

### Step A (done): order numbers and `seq` for the lane's bank entries; boilerplate help deleted

| Order | Questions, in `seq` order |
|---|---|
| 144 | `person.eligible_educator`, `person.educator_expenses` |
| 177 | `person.x_prior09`, `person.x_births` (the caps of two early-withdrawal exceptions; they belong with the Form 1099-R questions) |
| 180 | `person.sav_trad`, `ira_trad`, `ira_age50`, `ira_work_plan`, `ira_excess`, `ira_basis`, `ira_basis_adjusted`, `ira_dist` |
| 181 | `ira.special`, `ira.se_capital`, `ira.deduct_less` (once per return, so a block of their own: a block that mixes per-person and per-return questions is asked person by person first) |
| 182 | `person.x_other` |
| 315 | `person.sav_born`, `sav_student`, `sav_claimed`, `sav_roth`, `sav_voluntary`, `sav_able`, `sav_excess`, `sav_prior_joint`, `sav_prior_other` |

The help "Married filing separately and unsupported items are refused with citations." is gone from every entry
above that carried it.

### Step B (done): a person's birth year asked once; the seven birth-date questions derived from it (N8)

**What a filer sees.** One question per person, "In what year were you born?" (`person.birth_year`, a whole number),
in place of `person.under16` and `person.age65` (both asked of everyone), `person.died_before_65` (asked of everyone
65 or older), and, where a credit reached them, `person.sav_born`, `person.edu_born_2007`, `person.edu_born_2002`,
`person.born_after_1960`, `person.born_before_2001` and `person.ira_age50`. Four narrow questions remain, each asked
only of a person whose birth year leaves the fact open:

| Question | Asked only of a person born in | Why the year does not settle it |
|---|---|---|
| `person.born_jan1` "Were you born on January 1?" | 1961, 2001, 2002, 2007, 2008, and only when a line that needs it is reached | The instructions' birth-date tests are "born before January 2" (the day-before-the-birthday rule) |
| `person.under16_at_year_end` (the old `under16` wording) | 2010 | `amb.2025.filer_under_16` states no birth-date rule; the owner's reading asks the age |
| `person.age50_at_year_end` (the old `ira_age50` wording) | 1976, with an IRA contribution | `amb.2025.ira_age50`: the owner's decision is to ask the age at the end of 2025, not to apply a birth-date cut |
| `person.died_at_64` (the old `died_before_65` without its two dates) | 1960, or January 1, 1961 | Only such a person can have died in 2025 before reaching 65 |

**The model (all in `forms/2025/person.yaml`; no other form file changed).** The nine old ids are kept as derived
lines of the same type, so every reader in `eic`, `sa`, `s3`, `s1a`, `household`, `ira` and `person` reads what it read
(MAP Part 4.1; the technique works, the build accepts it).

| Old id (now derived) | Expression |
|---|---|
| `person.age65`, `born_before_2001`, `edu_born_2002`, `edu_born_2007`, `sav_born` | born in an earlier year than the cut, or in the cut year on January 1 (`person.born_jan1_if_cut_year`) |
| `person.born_after_1960` | birth year 1961 or later (the earned income credit's own wording counts a person born on January 1, 1961 as under 65; the fixture `stage9.eic.no_child.born_jan1_1961` holds this case and passes) |
| `person.under16` | birth year 2011 or later, or 2010 with the stated answer (`person.under16_at_year_end_if_born_2010`) |
| `person.ira_age50` | birth year 1975 or earlier, or 1976 with the stated answer (`person.age50_at_year_end_if_born_1976`) |
| `person.died_before_65` | itself the gate line of `person.died_at_64`: the stated answer for a person born in 1960 or on January 1, 1961 (`person.turned_65_in_2025`), otherwise no |

New inputs: `person.birth_year` (Count), `person.born_jan1`, `person.under16_at_year_end`, `person.age50_at_year_end`,
`person.died_at_64` (Bool, each `gated_by` its gate line). New helper lines: `person.birth_cut_year`,
`person.born_jan1_if_cut_year`, `person.born_2010`, `person.under16_at_year_end_if_born_2010`, `person.born_1976`,
`person.age50_at_year_end_if_born_1976`, `person.turned_65_in_2025`. Inputs removed (ids kept as lines): the nine above.
The cut years are constants in the form (`const: 1961` and so on), not parameters; at adoption they belong in
`params/2025.yaml` with the other year literals (`tools/year_ids.json` still lists four of the old ids as inputs).

**Fixtures.** Every case that stated one of the nine old answers now states a birth year (and the answer a cut year
needs) that gives the same nine facts: 949 person entries in 25 files, rewritten by
`l4b_work/fx.py` + `migrate.py` (first satisfying year of a fixed list: 1980, 1970, 1950, 1960, 1961 on January 1,
2001, 2004, 2007, 2009, 2012, ...). A case that withheld `age65` (`null`) withholds the year. No expected value or
refusal was edited. Four cases needed a year other than the first candidate, because they relied on defaults that no
one birth date satisfies together; `l4b_work/search.mjs` tried every candidate year against each case's expected
values and I chose among the passing ones the year the case's own description names:
`stage9.eic.no_child.born_jan1_1961` (1961, January 1), `stage19.blind.e6` and
`stage19.mut.aoc_student_18_half_support` (2007: the 18-year-old the old defaults `sav_born` yes, `edu_born_2007` no
described), `stage19.blind.e7` (2004).
**Found, not fixed:** 18 person entries in `classm*.json` and `mutation.json` state birth facts no date satisfies
(for example `age65: true` with `ira_age50: false`; `sav_born: false` with `born_before_2001: true`; ids in
`l4b_work/report.json`). They were given the year that satisfies most of their stated answers and all pass, so the
contradictory answer was not one their expected values depend on. The three consistency rules of
`fixtures/2025/defaults.json` about the birth questions are deleted (one year cannot contradict itself), and the nine
defaults are replaced by five (`person.birth_year` 1980).

**Engine changes** (three small ones): `interview-rules.ts`, the minimal return's closed answer to a number is zero,
which for a birth year is a person born in year 0; `CLOSED_NUMBER` gives `person.birth_year` 1980 (the background of
the coverage rows and of `draft-walk`). `generate.ts`: the generated returns still draw the old birth facts as working
answers and `putBirthYear` turns them into a year at the end (the random stream shifts, as with any added input).
Nothing checks the year typed: 0, 80 or 2030 is accepted and read as a very old or a very young person. A
consistency check (a year from 1900 to 2025) is the right guard and is **not built**.

**Order.** `person.birth_year`, `born_jan1` and `under16_at_year_end` carry today's order 2 and `died_at_64` order 10
(no `seq`): **they are not placed.** They belong at the head of topic 110 (lane 1's block). I tried 119: seven
`stage4` fixtures (`stage4.standard.mfj`, `stage4.medicare.mfj.*`, `stage4.niit.mfj.*`,
`stage4.official.medicare_example5`) then fail the build's walk with "missing or repeated question s1a.carloan",
because they withhold the Schedule 1-A answers. I infer (not traced) that their walk ends on the age answer before
those questions are asked, which holds only while the age question comes before order 10; with the year at order 2
the build passes. Once lane 3 moves `s1a.*` to 150 the four can take 110.

**Review debt.** `person.yaml` transcription, render, class M and screen reviews are stale for every line named here;
the five new gates have had no false-no review; `mutate.ts` pins that hash `person.age65`'s expression will not match.

### Step C (done): `person.x_other` taken apart; an IRA parent; the educator pair turned round; `person.ira_excess` in two; plain words (ranked items 1, 2, 3 and part of 4 and 5)

**`person.x_other` (136 words, asked of every person, refuses at Form 5329).** It stays as a derived line, true when
any of six new item lines is true, so the two `refuses: when: person.x_other` entries of `f5329.yaml` are unchanged and
the refusal is the same gate with the same text (MAP 4.1). Its five bullets became:

| Old bullet | New question(s) | Asked of | Topic (order, seq) |
|---|---|---|---|
| 1 taxable distribution from a Coverdell ESA, 529 plan or ABLE account | parent `person.x_edu_account`; child `person.x_edu_taxable` (refuses) | everyone; child only after Yes | 247 (1, 2) |
| 3 excess contributions to a Coverdell ESA or an ABLE account | child `person.x_edu_excess` (refuses) of the same parent | after Yes | 247 (3) |
| 3 excess contributions to an Archer MSA | `person.x_archer_excess` (refuses), no parent | everyone | 192 (2) |
| 2 an earlier year's excess IRA contribution still in the IRA | child `person.x_ira_prior_excess` (refuses) of the new `person.ira_owner` | people with an IRA | 180 (8) |
| 4 an earlier year's excess HSA contribution | `person.x_hsa_prior_excess` (refuses) | only a person who listed a health savings account (`person.has_hsa`, from `person.hsa_forms`, MAP 4.6) | 192 (1) |
| 5 a required minimum distribution not received in full | `person.rmd_missed` (refuses), asked directly of a person born in 1952 or earlier (`person.rmd_age`, from the birth year, N8), and of a younger person only after `person.inherited_account` Yes | everyone under 73 is asked `inherited_account`; everyone 73 or older `rmd_missed` | 177 (1, 2) |

**Ids changed from the map.** The map's `person.rmd_due` ("Did you have to take a minimum yearly withdrawal ...: aged
73 or over, or an inherited account?") is not built: the age half is settled by the birth year, so the parent asks
only the other half and is named `person.inherited_account`. `person.x_archer_excess` is new (the map sends Archer
MSAs to lane 9's `scope.archer_msa`, which does not exist on this branch; when it does, this question is asked only
after its Yes, or dropped if that question refuses every Archer MSA).

**`person.ira_owner`, a parent for the whole of topic 180.** "Do you have an IRA (an individual retirement account)
of any kind?" A No now also skips `person.sav_trad` (which everyone was asked, 52 words) and the Roth contribution
amount `person.sav_roth` (asked in the saver's credit block), through `person.sav_trad_if_ira_owner` and
`person.sav_roth_if_ira_owner`. So a person with no IRA answers one 11-word question about IRAs.

**The educator pair.** `person.eligible_educator` is asked first, in plain words with the 900 hours kept (it is part
of the definition and a wrong Yes gives a deduction); the amount `person.educator_expenses` is asked only after a Yes
(`person.educator_expenses_if_educator`). Before, every person read 104 words about classroom expenses.

**`person.ira_excess`** stays as a derived line (either of two new inputs), read as before by
`person.ira_excess_gate`: `person.ira_extra_left` (over the limit and not taken back) and `person.ira_recharacterized`.
Its third bullet (an earlier year's excess) is `person.x_ira_prior_excess`, asked once (2.7).

**Model changes (all in `person.yaml`; `ira.yaml` one reference).** New inputs: `person.ira_owner`,
`person.x_edu_account`, `x_edu_taxable`, `x_edu_excess`, `x_archer_excess`, `x_ira_prior_excess`,
`x_hsa_prior_excess`, `inherited_account`, `rmd_missed`, `ira_extra_left`, `ira_recharacterized`. Inputs that became
derived lines: `person.x_other`, `person.ira_excess`. Inputs newly gated (`gated_by`): `person.sav_trad`,
`person.sav_roth`, `person.educator_expenses`, and the gated new ones. New gate and helper lines:
`person.sav_trad_if_ira_owner`, `sav_roth_if_ira_owner`, `x_edu_taxable_if_account`, `x_edu_excess_if_account`,
`x_ira_prior_excess_if_ira_owner`, `has_hsa`, `x_hsa_prior_excess_if_hsa`, `rmd_age`,
`inherited_account_if_under_73`, `rmd_possible`, `rmd_missed_if_possible`, `educator_expenses_if_educator`.
`ira.yaml`: the one `sum_over` of `person.sav_roth` reads the gate line. The form lines keep the source's words
(`label`, `source`); the plain words are bank `prompt`s.

**Fixtures.** `l4b_work/migrate_c.py`: `x_other: true` (one case) is stated as a 529 account with a taxable
distribution; `x_other: false` as No to each new question (stated in full only in the files that take no defaults);
`ira_excess` as `ira_extra_left` (true stays true; two cases); `ira_owner` is Yes wherever a traditional or Roth
contribution is stated (and where `sav_trad` is withheld, so that it stays unknown); `eligible_educator: false` is
added in the files without defaults where only a zero amount was stated. No expected value or refusal was edited.

**Wording (bank only, no model change):** `person.sav_trad`, `ira_trad`, `ira_work_plan` (the fact first, then box
13 of the W-2), `sav_student`, `sav_roth`, `sav_voluntary`, `sav_able`, `sav_excess`, `sav_claimed` (help).

**Cost and share (my estimates on the owner's scale unless marked gf, `gate_frequencies.yaml`).**

| Question | Asked of | Share answering yes | Cost of No | Cost of Yes | Before |
|---|---|---|---|---|---|
| `person.birth_year` | every person | n/a (a year) | 1 | 1 | `under16` 1 + `age65` 2 ("born before January 2, 1961") + for 19% (gf `age65`) `died_before_65` 5 |
| `person.eligible_educator` | every person | 2.4% (gf `educator`) | 1 (leaves at "work in a school") | 2 (the 900 hours) | 5: 104 words to enter zero |
| `person.educator_expenses` | 2.4% | n/a | n/a | 5 (add up receipts) | asked of 100% |
| `person.ira_owner` | every person | 33% (map, gf) | 1 | 1 | none; replaces `sav_trad` (2) for the 67% |
| `person.sav_trad` | 33% | 8% of all (gf `ira_contributions`), about a quarter of owners | 1 | 1 | 2 (52 words) of 100% |
| `person.x_ira_prior_excess` | 33% | under 0.2% (judgment) | 2 | 5 | part of `x_other` (15) |
| `person.x_edu_account` | every person | 8% (judgment: 529 owners and beneficiaries) | 1 | 1 | part of `x_other` |
| `person.x_edu_taxable`, `x_edu_excess` | 8% | under 0.3% (judgment) | 3 each | 5 | part of `x_other` |
| `person.inherited_account` | every person under 73 | 2% (judgment) | 1 | 1 | part of `x_other` |
| `person.rmd_missed` | 73 or older (about 9% of people, judgment) and inheritors | under 0.5% (judgment; gf `form5329_other` 0.6% for all of `x_other`) | 2 | 5 | part of `x_other` |
| `person.x_hsa_prior_excess` | 11% (gf `hsa`) | under 0.2% (judgment) | 2 | 5 | part of `x_other` |
| `person.x_archer_excess` | every person | about 0 | 2 (an unknown term, but "of yours" lets a person without one leave) | 5 | part of `x_other` |

N3 for the parents: `ira_owner` costs 1 and 67% leave before children costing about 4 (0.67 x 4 > 1);
`x_edu_account` costs 1 and 92% leave before two children costing 6 (5.5 > 1); `inherited_account` costs 1 and 98%
leave before one child costing 2 (1.96 > 1, by little: it is kept because the child's term, "required yearly
minimum", costs a person who has never heard it more than 2).

**Who could answer No wrongly, and the guard.**

- `ira_owner`: a person whose only IRA came through work (a SEP or SIMPLE IRA) or was inherited, and a person who
  opened one in 2026 for 2025. The help names all three and says Not sure is Yes. This is help, not a child (N2 asks
  for a child); the false-no review of this gate is debt.
- `x_edu_account`: a student whose parent's 529 plan paid the school, who does not know of it. The help gives the
  paper (Form 1099-Q). The old question had the same exposure. A second question ("Did you get a Form 1099-Q or
  1099-QA for 2025?") would be the N2 guard; not built.
- `inherited_account`: a person who treats a late husband's or wife's IRA as their own may say No; such an account has
  no beneficiary minimum, so the No is harmless.
- `person.has_hsa` as the gate of `x_hsa_prior_excess`: a person with an old excess in an account they answered No
  to at `$f8889`. That question's help says Yes "even if nothing went in or came out in 2025"; an account closed
  before 2025 holds no excess. Debt: false-no review.
- `person.rmd_age` (born 1952 or earlier): a person born in 1952 has no deadline in 2025 and is asked one question
  too many, by design (the cut is the year, not the day).

**Unsure.**
- The gloss of "taxable" in `x_edu_taxable` ("more than the education costs, or for an ABLE account the disability
  costs, that it paid for") is from my knowledge of the rules, not from the archived instructions.
- `educator_expenses` and `ira_trad` keep their exclusions in help (40 and 44 words) rather than in children: N10 says
  children, N3 says not for a deduction capped at $300 or for exclusions almost nobody meets. The owner may differ.
- `eligible_educator` is 29 words for a parent (the 900 hours).
- `rmd_missed` drops no words of the source's meaning that I can see, but "by its deadline" asks the filer to know the deadline.

**`ira.special` (93 words, one sentence of four items; asked once per return when a traditional IRA contribution is
entered; refuses through `ira.special_gate`).** It stays as a derived line (any of four new inputs of `ira.yaml`), so
`ira.special_gate` and the refusal on it are unchanged: `ira.deferred_comp` (by the paper: W-2 box 11, box 12 code Z,
Form 1099-MISC box 15), `ira.fellowship`, `ira.reservist_repaid`, `ira.care_payments`. They are four flat questions
with no parent (see the tick-list candidates). `ira.deduct_less` is reworded as the wish it is, with "To go on with
the full deduction, answer No." `person.sav_roth` moved from the saver's credit block (315) into the IRA block (180,
after the traditional amount): beneath `ira_owner` it is an IRA question, and the IRA limit reads it as soon as a
traditional contribution is entered. The map expected lane 9's `scope.reservist_repaid` to replace the reservist item
here (2.7); on this branch that question does not exist, so `ira.reservist_repaid` is asked; at the stitch one of the
two goes.

## Topic 180 and its neighbours as built (order, seq)

| Order | Questions |
|---|---|
| 2, 10 (not placed; belong at 110) | `person.birth_year`, `born_jan1`, `under16_at_year_end`; `died_at_64` |
| 144 | `person.eligible_educator` (1), `educator_expenses` (2) |
| 177 | `person.inherited_account` (1), `rmd_missed` (2), `x_prior09` (3), `x_births` (4) |
| 180 | `person.ira_owner` (1), `sav_trad` (2), `ira_trad` (3), `sav_roth` (4), `age50_at_year_end` (5), `ira_work_plan` (6), `ira_extra_left` (7), `ira_recharacterized` (8), `x_ira_prior_excess` (9), `ira_basis` (10), `ira_basis_adjusted` (11), `ira_dist` (12) |
| 181 | `ira.deferred_comp` (1), `fellowship` (2), `reservist_repaid` (3), `care_payments` (4), `se_capital` (5), `deduct_less` (6) |
| 192 | `person.x_hsa_prior_excess` (1), `x_archer_excess` (2) |
| 247 | `person.x_edu_account` (1), `x_edu_taxable` (2), `x_edu_excess` (3) |
| 315 | `person.sav_student` (1), `sav_claimed` (2), `sav_voluntary` (3), `sav_able` (4), `sav_excess` (5), `sav_prior_joint` (6), `sav_prior_other` (7) |

## Before and after, from the persona walks

Before: `docs/provisional/walks/before/`. After: `draft-walk` on this branch (written to a scratch directory, not
committed: `walks/after/` is for the merged interview). "This lane's questions" are the `person.*` questions of the
lane (birth, educator, IRA, saver's credit, Form 5329) and `ira.*`; other lanes' `person.*` questions (`blind`,
`rrta`, `work_ssn`, the education block) are not counted.

| Filer | This lane's questions, before | After | Whole walk, before | After |
|---|---|---|---|---|
| `01_single_w2`: nothing in the topic | 5 questions, 309 prompt words (`under16` 10, `age65` 7, `educator_expenses` 104, `x_other` 136, `sav_trad` 52) | 6 questions, 117 words (`birth_year` 6, `eligible_educator` 30, `inherited_account` 18, `ira_owner` 12, `x_archer_excess` 25, `x_edu_account` 26) | 86 questions, 6,777 words, 2,376 help words | 87, 6,585, 2,319 |
| `04_retired_couple` (71 and 69) | 12 questions, 742 words | 12 questions, 271 words | 122, 9,030 | 122, 8,559 |
| `07_college_student` (24) | 11 questions, 356 words (seven of them about his date of birth) | 8 questions, 135 words (the year, and "born on January 1?" because 2001 is a cut year) | 110, 7,747 | 107, 7,526 |
| `08_hsa_marketplace` | 5 questions, 309 words | 7 questions, 145 words (adds `x_hsa_prior_excess`) | 150, 10,384 | 152, 10,220 |
| `13_ira_saver` (new persona: $4,000 into a traditional IRA, a 401(k) at work): the ordinary case | not walked (no baseline). Inferred from the old texts of the same questions: 12 questions, about 700 words (`under16`, `age65`, `educator_expenses` 104, `x_other` 136, `sav_trad` 52, `ira_trad` 73, `ira_age50`, `ira_work_plan` 32, `ira_excess` 113, `sav_roth` 33, `ira.special` 93, `ira.deduct_less` 39) | 18 questions, 429 words; the longest is 43 | | 100, 6,917 |

The count of questions rises by one for the filer with nothing (six one-line questions for five, two of which were
104 and 136 words) and by six for the IRA contributor (three catch-alls became eleven one-fact questions); the reading
falls by about 60% and 40%.

## Candidates for one tick-list

1. **"Did any of these happen with your IRA or your pay in 2025?"** (asked once per return, only when a traditional
   IRA contribution is entered): `ira.deferred_comp`, `ira.fellowship`, `ira.reservist_repaid`, `ira.care_payments`.
   Four short facts, each refusing, same theme (what counts as pay for the IRA limit).
2. **"Accounts with their own penalties"** (asked of every person): `person.x_edu_account`, `person.inherited_account`,
   `person.x_archer_excess`. Three one-line facts with no common parent; each is "do you have this kind of account".
   They sit in three topics (247, 177, 192) because each belongs with its subject (N5); a tick-list would have to
   choose one place. I would leave them where they are unless the count of flat questions matters more.

## Requests to other lanes and the coordinator

- **Lane 1 (bank entries `person.under16`, `age65`, `died_before_65`):** those three entries are gone from the bank
  (the ids are derived lines now). Any rewording of them on `lane/l1` has no question to attach to: delete the three
  entries at the merge. Place `person.birth_year`, `born_jan1`, `under16_at_year_end`, `died_at_64` at the head of 110,
  in that order, once `s1a.*` has left order 10 (see "Order" in step B).
- **Lane 2b (bank entries `person.born_after_1960`, `born_before_2001`):** both entries are gone (derived). Delete at
  the merge. The earned income credit's two birth questions are no longer asked; a person born in 2001 is asked
  `born_jan1` instead.
- **Lane 8b (bank entries `person.edu_born_2007`, `edu_born_2002`):** gone (derived; they are one-sided in
  `reviews/2025/twins.json`, which still lists them and still passes because the lines exist). Delete the two bank
  entries at the merge. `person.x_edu_account` and its two children sit at 247 as the map says.
- **Lane 8a (`interview/2025/coverage/hsa.yaml`, row `hsa.prior_year_excess`):** I rewrote its answers (the old
  `person.x_other` answer no longer exists): an account with payroll deposits, then `person.x_hsa_prior_excess` Yes.
  If lane 8a also edits that row, take this one. `f8889.age55` could read `person.birth_year` (55 or older: born
  1970 or earlier, 1971 being the open year); `f8889.yaml` has no owner, so this is for the coordinator.
- **Lane 6a (bank only `person.simple_age`):** the three-way age choice for a SIMPLE plan can be derived from
  `person.birth_year` with a stated answer for the open years (1962, 1966, 1976); not built (the input is an enum
  with its own owner decision, `amb.2025.ira_age50`'s sibling). It is the one age question of `person.yaml` left.
- **Lane 2a (`dependent.age`)** already asks an age once; nothing needed.
- **Lane 9:** `scope.archer_msa` and `scope.reservist_repaid`, when they exist, overlap `person.x_archer_excess` and
  `ira.reservist_repaid` (above). The excess 401(k) deferral question the map mentions for 180 was not handed over
  on this branch; `person.sav_excess` (315) asks the same fact for the saver's credit only.
- **Order agent:** in the walk of `13_ira_saver` the IRA topic is asked together (questions 83 to 96) but for two
  things. `person.sav_roth` (180, seq 4) is asked after `ira_recharacterized` (seq 8): I think it becomes reachable
  only when the IRA limit is figured, after the screens before it. And `s8812.combat_pay` is asked between
  `ira.care_payments` and `ira.deduct_less` (both 181): I think the IRA deduction's effect on income makes it
  reachable there; it still carries today's order. `person.x_hsa_prior_excess` (192) is asked 130 questions after
  the HSA block in my branch only because the block is still at order 9.
- **Walk lane:** persona `13_ira_saver` added (the map's ordinary case for this topic; the baseline has no persona
  with an IRA, so there is no "before" transcript for it).
- **Coordinator:** `tools/year_ids.json` lists `person.born_after_1960`, `born_before_2001`, `edu_born_2002`,
  `edu_born_2007` as inputs (they are lines now); `interview/2025/gate_frequencies.yaml` refs name `person.age65`,
  `person.under16`, `person.sav_trad`, `person.educator_expenses`, `person.x_other` (all still exist as line ids).

## Not done, in rank order

1. **The Form 8606 questions** (`person.ira_basis` 47 words, `ira_basis_adjusted` 82 words, `ira_dist` 50 words;
   ranked item 4): untouched but for their place. The map's plan: a parent "Have you ever filed Form 8606?" with the
   four items of `ira_basis_adjusted` as children (two of them apply only to earlier filers, two to anyone).
2. **The saver's credit's two prior-distribution amounts** (`person.sav_prior_joint` 143 words, `sav_prior_other` 157
   words; ranked item 5): untouched. Plan: a parent `person.sav_prior_any` ("Did you take money out of a retirement
   account in 2023, 2024, or in 2026 before the deadline for this return?") gating both amounts; each input line
   carries a `refuses` on `person.sav_able`, which must move to the gate lines with it; readers are three `sum_over`
   in `f8880.yaml`. The nine exclusions as children of Yes. `retirement.sav_*` are lane 4a's file.
3. **`ira.se_capital`** (34 words, asked only with a business) and **`person.x_prior09`, `x_births`** (the caps of two
   early-withdrawal exceptions): not reworded.
4. **A check on the birth year typed** (1900 to 2025).
5. **`person.simple_age`** from the birth year (see the request to lane 6a).
6. **Help texts** of `ira_basis`, `ira_basis_adjusted`, `ira_dist`, `sav_prior_*` still say "this tool" or name form lines.


## What I ran and saw, and what I infer

Ran and saw (this worktree, 2026-11-13): `tools/draft_check.sh --quick` green after step A and after step B;
the full `tools/draft_check.sh` green after step C with all thirteen steps ok (build; fixtures 1854/1854;
interview-rules 0 problems over 177 walks; coverage rows 0 problems; person wording current; the spouse-wording,
check, draft-walk self-tests; integration 695 invocations; properties; test-serve; twins; render check), on index
tree `4e43801f9e74`; the commit adds to that tree only the reports the check itself rewrote and these notes. New York
fixtures 338/338 (run by hand; not part of the draft check). `interview-coverage --rows` on `saving.yaml` (19 rows)
and `hsa.yaml` (23 rows): 0 problems. `draft-walk` over thirteen personas: 0 problems, ends as each persona states.
I read the shown forms (one person, the spouse's entry) of every new or reworded framed question in
`reports/2025/person_wording.md`.

Inferred, not checked: that no return's values changed beyond what the fixtures hold (the fixtures' expected values
are the evidence; the Lean comparison, the differential engines and mutation testing were not run); every share
marked judgment and every cost in the tables; the "before" of the IRA persona; why `sav_roth`, `s8812.combat_pay` and
the seven `stage4` fixtures behave as described under the order notes; that a filer in each coverage row's situation
would give the row's answers (the rows test the tree, not the wording). I did not open the Form 5329, Form 8606 or
Pub. 590-A instructions: the new questions' sources are the old questions' own words and citations, split.
