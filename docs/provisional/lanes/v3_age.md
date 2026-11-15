# Lane notes: v3 age (three age questions asked after the birth year is known)

Branch `draft/v3` (worktree `.claude/worktrees/provisional-v3`, cut from `draft/v2` at `709fee40`). Agent:
`claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no model call.

The defect: after giving his year of birth, the owner was asked "Were you 55 or older on December 31, 2025?" in the
health savings account questions (`person[taxpayer].f8889[hsa].age55`). N8: never ask what an earlier answer settles.
Three age facts were still asked after `person.birth_year`: `f8889.age55`, `scope.under24`, `person.simple_age`. Each is
made a derived line of the same id where the form allows it, so no reader changes, with a narrow question kept only for
a birth year that leaves the fact open (the pattern of lane 4b, `l4b.md` step B).

Scripts: `v3_age_work/age.py` restates the fixtures (one phase per input; reports in `v3_age_work/<phase>_report.json`).

## 1. `f8889.age55` (the one the owner met)

**Source.** i8889 p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older and unmarried or married with
self-only HDHP coverage for the entire year, you can increase the amount ... by $1,000"; p. 6, Line 3 Limitation Chart,
"If you were age 55 or older at the end of 2025". The instructions give no birth-date rule (no January 1 rule) and
`ambiguities/2025.yaml` has no entry for this age. The day-before-the-birthday rule is stated only for age 65 (the
reason recorded in `amb.2025.ira_age50`).

**Years.** Born 1970 or earlier: 55 or older at the end of 2025, whatever the day. Born 1972 or later: not. Born 1971:
55 at the end of 2025 only on the day-before reading (a January 1, 1971 birthday); the project has no reading, so the
plain question is asked of a person born in 1971 only, as `person.age50_at_year_end` is for 1976. Nothing is invented.

**Model.** `f8889.age55` is a derived line (same id, same type), so `f8889.age55_line3`, `age55_unmarried` and
`line7_applies` read what they read. Form 8889 is a collection under the person; its lines read the enclosing
person's lines by id (as `sc.rrta` copies `person.rrta`). New in `person.yaml` (after the 1976 lines): `person.born_1971`
(helper), `person.age55_at_year_end` (input, Bool, `gated_by` the gate), `person.age55_at_year_end_if_born_1971`
(gate: the stated answer for a person born in 1971, otherwise no). The question is asked once per person, not once per
Form 8889 entry. Input removed: `f8889.age55`.

**Bank.** The `f8889.age55` entry is replaced by `person.age55_at_year_end` at its place (order 190, seq 17) with the
old prompt ("Were you 55 or older on December 31, 2025?"). Profiles `sales.yaml` and `stage4.yaml` list the new id in
place of the old.

**Fixtures.** `fixtures/2025/defaults.json`: the default of `f8889.age55` (false) is replaced by one for
`person.age55_at_year_end` (false). See the table of restated cases below.

**Generator** (`engine/src/generate.ts`): the taxpayer's HSA age is no longer drawn (it is not an input; the random
stream shifts, as with any removed input); a generated person whose working answers say 50 or older is born in 1970
and so is 55 or older. The spouse's drawn HSA age (`age55`, a rare yes) is now a working answer that makes a 25-to-64
spouse born in 1970 instead of 1980. No generated person is born in 1971.

**Fixtures restated** (`v3_age_work/age.py age55 --override v3_age_work/age55_override.json`; report in
`age55_report.json`): 277 person entries in 268 cases of 7 files (`classm.json` 125, `classm.deepseek.json` 76,
`mutation.json` 55, `f8889.json` 13, `classm.gpt.json` 5, `sd.json` 2, `ira.json` 1). No expected value or refusal was
edited.

- 237 entries: the case's own year (stated, or the default 1980) already gives the stated answer; the answer is removed.
- 25 entries stated 55 or older with the default year 1980: now born in 1970 (the nearest year that settles it without
  the 1971 question). This also turns `person.ira_age50` from no to yes; every one of these cases passes.
- 2 entries (`sd.json`: `stage21.f1.special_withheld`, `stage21.f1.special_null`, the spouse): stated born in 2001 and
  55 or older; now born in 1970 (`born_before_2001` and `ira_age50` change); both pass.
- 10 entries state a person 65 or older (born 1950, or on January 1, 1961) who is **not** 55 or older: no birth year
  gives both. Moving them to 1972 passed for eight but changed `age65` for all ten, and failed
  `mutation.t2.s1a.hoh_senior_decedent` and `mutation.t2.s1a.qss_senior_decedent` (their refusal reads the age-65
  facts; `search.mjs` found only 1960 and January 1, 1961 passing). So all ten keep their stated birth (and so are now
  55 or older), and all ten pass: the contradictory "under 55" answer was not one their expected values depend on, as
  with lane 4b's eighteen. **Found, not fixed** (impossible persons in the class M and mutation files):
  `classm.sd.2.deepseek`, `classm.otjob.1` (spouse), `classm.sd.2`, `classm.se.3` (spouse), `classm.sli.5`,
  `classm.w2.1`, `mutation.t2.no_carloan_part4_b`, `mutation.t2.s1a.mfs_ssn_unanswered`,
  `mutation.t2.s1a.hoh_senior_decedent`, `mutation.t2.s1a.qss_senior_decedent`.
- 1 entry withheld the answer (`redesign.hsa.testing_kept_age_unanswered`, "the age question is left unanswered"): the
  year is withheld instead (`birth_year: null`), as lane 4b did for a withheld `age65`; it passes.
- 2 entries in files without defaults (`classm.f8889.2.deepseek`, `mutation.t2.single_no_edu_no_spouse_col`, a person
  named `sample`) stated the HSA age but no birth year: they now state 1980, which also makes that person's other age
  facts known where they were unknown; both pass.

`tools/defaults_guard.mjs` was not run by hand: no existing default's value changed (one removed with its input, one
added for a new input).

**Coverage and personas.** The three answers `f8889[hsa].age55: false` in `coverage/hsa.yaml` and the one in persona
`08_hsa_marketplace` are removed (the background year 1980 and the persona's 1991 give the same). Two new rows in
`hsa.yaml`: `hsa.age55_settled_by_birth_year` (born 1968: not asked, the return is prepared) and
`hsa.age55_asked_born_1971` (born 1971: asked). The `same_plan` set's description no longer says "under 55" (it no
longer answers the age).

**Review debt.** f8889 transcription, render, class M and screen reviews are stale for `f8889.age55`; the new gate has
had no false-no review; the mutation pins in `engine/src/mutate.ts` that list `f8889.age55` hash expressions that
changed (mutation testing is not run here).

**Check.** `tools/draft_check.sh --quick` green on the tree of this change (`fffa532c5da0`): build; fixtures 1854/1854;
interview-rules 0 problems over 177 walks (baseline untouched); coverage rows 0 problems (450 rows, with the two new
ones); tick-groups passed.

## 2. `scope.under24`

**What it means.** A tick-box of `about_you` (order 113), asked once per return and hidden on a joint return
(`scope.under24_if_not_joint`: the answer on single, head of household, qualifying surviving spouse and separate
returns, no on a joint one). It is about "you", the taxpayer. Its Yes opens `scope.unearned_2700` and then `scope.f8615`
(the Form 8615 refusal). Its own citation is the generic Form 1040 locator; the age is Form 8615's condition 3, "under
age 24 at the end of 2025".

**Years.** i8615 p. 1, "Certain January 1 birthdays. Use the following chart to determine whether certain children
with January 1 birthdays meet condition 3 under Who Must File": a child born on January 1, 2002 is considered 24 at the
end of 2025 ("Don’t use Form 8615 for this child."). So the source settles the cut: under 24 is born in 2003 or later,
or in 2002 on a day other than January 1. 2002 is already a year of `person.born_jan1` (asked only of a person born in
1961, 2001, 2002, 2007 or 2008), with the same day-before reading, so no new question is needed.

**Model.** `person.under24` (new derived line in `person.yaml`, after `person.age65`). `scope.under24` is a derived line
of the same id: `scope.under24_count` sums `person.one` over the person whose `role` is taxpayer and who is under 24 (as
`household.taxpayer_work_ssn_count` reaches the taxpayer's line from a return-level form), and `scope.under24` is that
count above zero. The gates `under24_if_not_joint`, `unearned_2700_if_under24` and `f8615_if_unearned_2700` are
unchanged. Input removed: `scope.under24`.

**Bank and tick group.** The entry (order 113, seq 2, group `about_you`, tick "Under 24 at the end of 2025") is
removed; `about_you` keeps four members (`sa.excluded_income`, `scope.noncitizen`, `scope.chapter11`,
`scope.armed_forces`); `tick-groups` passed. Removed from the profiles `sales.yaml` and `stage4.yaml`, and its default
from `defaults.json`.

**Fixtures restated** (`age.py under24 --override v3_age_work/under24_override.json`; `under24_report.json`): 725
taxpayer entries in 15 files (federal 529, New York 196); every one stated No. 706: the case's year already gives No.
8 (`f1040.json` three, `s3.json` five) withhold the birth year (`null`) and stated No: the answer is removed and the
year stays withheld, so the fact is unknown on those cases; all pass. **Found, not fixed** (impossible persons, 11): a
taxpayer born in 2004 or 2009 who states not under 24. Moving them to January 1, 2002 changed their education-credit
age facts and failed `classm.f8863.3` and `classm.f8863.3.deepseek`; so all eleven keep their stated year (now under 24)
and all pass: `classm.clcw.4.deepseek`, `classm.f8863.3.deepseek`, `classm.eic.7.deepseek`, `classm.person.4`,
`classm.person.12`, `classm.person.16`, `classm.clcw.4`, `classm.f8863.3`, `mutation.t2.no_carloan_part4`,
`mutation.t2.hoh_s1a_tips_ot`, `mutation.t2.s1a.line21_magi_first`.

**Coverage rows** (`scope.yaml`). `scope.f8615` ("a 20-year-old") answers `person[taxpayer].birth_year: 2005` and
`scope.under24_small_income` ("a 22-year-old") 2003 in place of the tick. `scope.couple_not_asked_age` named
`scope.under24` under `not_asked`, which the coverage check refuses for an id that is no longer a question: it now
names `scope.unearned_2700`, the question the age opens (its end, a refusal at `scope.other_income`, is unchanged; the
situation sentence says so). This is the one `expect` entry touched, and not the end. Whether that question would come
before the refusal at all on that row I have not checked, so the check may be vacuous there.

**Generator.** Nothing named `scope.under24`; as a root input it was drawn by `declaredInputs` and now is not (the
random stream shifts).

**Check.** `tools/draft_check.sh --quick` green (tree `b3c37ad808ee`): build; fixtures 1854/1854; interview-rules 0
problems over 177 walks; coverage rows 0 problems; tick-groups passed. New York fixtures 338/338 by hand
(`node engine/dist/main.js --ny test-fixtures`).

## 3. `person.simple_age`

**Source.** Pub. 560 p. 16, chapter 3, Catch-up contributions: a participant "age 50 or over at the end of the calendar
year" may make catch-up contributions, and a higher limit applies "in a tax year in which they attain age 60, 61, 62,
or 63". The three choices are under 50, 50 to 59 or 64 and over, and 60 to 63.

**Years** (a birthday in 2025 decides the age attained in 2025; a January 1 birthday is the only open case, and the
project has no reading for it outside age 65, the reason recorded in `amb.2025.ira_age50`):

| Born | Band | Why |
|---|---|---|
| 1961 or earlier | 50 to 59 or 64 and over | attains 64 or more in 2025 |
| 1962 | asked | attains 63 in 2025, or 64 on the day-before reading of a January 1 birthday |
| 1963 to 1965 | 60 to 63 | attains 62, 61 or 60 (or one more on a January 1 birthday): inside the band either way |
| 1966 | asked | attains 59, or 60 on the day-before reading of a January 1 birthday |
| 1967 to 1975 | 50 to 59 or 64 and over | 50 to 58 (or one more) |
| 1976 | from `person.age50_at_year_end` | 49, or 50 on a January 1 birthday: the same fact the IRA asks, the owner's decision `amb.2025.ira_age50` to ask the age; asked once, not twice |
| 1977 or later | under 50 | |

**Model** (`person.yaml`; `params/2025.yaml`). `person.simple_age` is a derived line of the same id and type
(`Enum(catchup_age)`), a choose over the birth year (an interval tiling: the build's guard analyser accepts intervals,
not equality with a number), so `person.catchup_limit` reads what it read. New: `person.simple_open_year` (born 1962
or 1966), `person.simple_age_at_year_end` (input, the old three-way question, `gated_by`
`person.simple_age_if_open_year`), `person.simple_age_if_open_year` (gate; otherwise the band 50, read only for those
years), `person.simple_age_1976` (50 or under 50 from `person.age50_at_year_end_if_born_1976`), and three constant
lines `person.catchup_under50`, `catchup_age50`, `catchup_age60_63` from new parameters `ret.catchup_under50`,
`ret.catchup_age50`, `ret.catchup_age60_63`. Input removed: `person.simple_age`. (`v3_age_work/simple_model.py` wrote
the first form; the guards were then rewritten by hand as the tiling described.)

**Bank.** The `person.simple_age` entry (order 260, seq 6, prompt and labels) now names
`person.simple_age_at_year_end`. The help of `person.age50_at_year_end` now names SIMPLE catch-up contributions as well
as the IRA. Profiles `sales.yaml`, `stage4.yaml`: the new id in place of the old. Default:
`person.simple_age_at_year_end` "age50" in place of `person.simple_age` "under50" (a scenario that reaches it states it).

**Generator.** The drawn SIMPLE age is now a working answer, only for a person with a SIMPLE plan: 60 to 63 gives a
25-to-64 person the year 1964, 50 to 59 gives 1970; no generated person is born in 1962 or 1966.

**Fixtures restated** (`age.py simple --override v3_age_work/simple_override.json`; `simple_report.json`): 175 person
entries in 146 cases of 6 files (`classm.json` 65, `classm.deepseek.json` 52, `mutation.json` 47, `classm.gpt.json` 6,
`person.json` 4, `sd.json` 1). 66 kept their year. 88 moved: 44 from 1980 to 1965 (60 to 63; `ira_age50` and `age55`
become yes), 41 from 1980 to 1975 (50; `ira_age50` becomes yes), 3 from 1970 to 1965 (no other fact changes). All pass,
including the eight `stage14.simple.*` cases, the ones whose values depend on the band. **Found, not fixed**
(impossible persons, 21 entries; they keep their year and pass, so the stated band is not one their values depend on,
in each case a class M or mutation person with no SIMPLE plan): a person 65 or older stated 60 to 63 or under 50
(`classm.w2.1.deepseek` both, `classm.sd.2.deepseek`, `classm.sd.2`, `classm.se.1` spouse, `classm.w2.1` spouse,
`mutation.t2.f8962_months_asset3` spouse, `mutation.t2.no_carloan_part4_b`, `mutation.t2.no_5695_part1_s3_5a` both,
`mutation.t3.roth_excess_screen` both); a person born in 1970 (55 or older) stated under 50 (`classm.eic.6.deepseek`,
`classm.f5329.3.deepseek`, `classm.f5329.3`, `mutation.t2.mfj_no_overtime_part3`, `mutation.t2.f8880.inherited_ira`,
`mutation.t2.s1a.line13_magi_first`); a person born in 2009 stated 50 or 60 to 63 (`classm.eic.7.deepseek`,
`classm.f5329.1.deepseek` spouse, `classm.f5329.1` spouse).

**Coverage rows** (`business.yaml`, new): `business.simple_age_settled_by_birth_year` (born 1964, SIMPLE, $20,000 of
deferrals: the age band is not asked; the walk reaches `simple_employer`) and `business.simple_age_asked_born_1966`
(born 1966: asked). `interview-coverage --rows business.yaml`: 0 problems. No existing row or persona answered
`person.simple_age`.

**Check.** `tools/draft_check.sh --quick` green (tree `7ec44fcbfefb`): build; fixtures 1854/1854; interview-rules 0
problems over 177 walks; coverage rows 0 problems; tick-groups passed.

## Whole check and walks

`tools/draft_check.sh` (whole), run once after the three commits: every step ok (build; fixtures 1854/1854;
interview-rules 0 problems; coverage rows 0 problems; tick-groups; person wording current; spouse-wording, check,
draft-walk, order and tick-groups self-tests; integration 1021 invocations; properties; test-serve 512 checks; twins
0 problems) but `render_check`: `rendered/2025/` was stale for f8889, person, scope, params and the index (the
rendered forms are generated from the model and no earlier step rewrites them). `node engine/dist/main.js render`
rewrote them and `render --check` then passes; the regenerated pages and the reports the check rewrote
(`person_wording.md`, `properties.md`) are committed with the walks, and the whole check is run again on that commit
(result below).

`draft-walk --out docs/provisional/walks/after`: 14 personas, 0 problems, each at its stated end (twelve complete,
`11_refused_rental` refused at `scope.schedule1`, `12_refused_nonresident` at `scope.other_income`). No transcript
asks `f8889[hsa].age55`, `scope.under24` or `person.simple_age`.

Scratch walks (not committed; persona `08_hsa_marketplace` with only the birth year changed, in a temporary
directory): born 1968, the Form 8889 questions go from `last_month` (73) straight to `ira_prior` (74); nothing is asked
in place of the old question, 198 questions, complete, 0 problems. Born 1971: question 74 is
`person[taxpayer].age55_at_year_end`, "Were you 55 or older on December 31, 2025?", between `last_month` and
`ira_prior` (the walk flags it as opened and unanswered only because the persona file has no answer for it). The walk
labels it a topic switch to the person topic and back (it is a person's line placed in the HSA block, order 190).

