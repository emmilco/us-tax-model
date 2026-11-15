# Lane land3-consumers: the 25 open consumer pairs

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Worktree `.claude/worktrees/land3-consumers`
(detached at `refs/scratch/land3-base`, `57b00992`). No commit, no paid review call, no model call from code.
Context: `docs/provisional/lanes/landing.md` section 3, "Consumer rulings"; the prior agents' reasoning is in
`landing_work/consumers/cfindings_*.md`.

## Result

- `python3 tools/check_consumers.py`: 664 findings; 0 new; 219 in the baseline; 445 ruled; 0 stale (was 25 new).
- `python3 tools/check_consumers.py --jurisdiction ny`: 9 findings; 0 new; 9 ruled; 0 stale. The 3 New York pairs
  were already ruled in this base tree (0 new before any change of mine); nothing was done for New York.
- Every ruling added or re-quoted (48) was checked mechanically: the question phrase is a verbatim substring of the
  built question (`canonical/2025`) and the source phrase a verbatim substring of the archived page text.

## Per pair

(a) the question already matches; (b) a small wording, help or cite fix made here, then ruled `same`; (c) too large,
ruled `differs` with `fixed_by` naming the pending entry (the check accepts any `BUG-` prefix, and `new_bug.py
--assign` rewrites the placeholder at the merge).

| Pair | Decision | Why |
|---|---|---|
| `dependent.eic_ssn@i1040gi:p18` | b (cite) | The reader `dependent.eic_ssn_known` carried its sibling's child tax credit cite (p. 18 Step 3 q. 4; p. 22). It now cites the EIC rule, pp. 44–45. The pair is gone; the stale `eic_ssn@p22` ruling is removed; the two new pairs `dependent.citizen_ssn@i1040gi:p44/p45` are ruled `same`. |
| `person.ira_owner@f5329:p1` | b | Present tense ("Do you have an IRA") missed an IRA held in 2025 and closed in early 2026; it now asks "at any time in 2025, or ... now". |
| `s1.digital_income@i1040gi:p92` | b (bank) | The page names forks; the prompt, tick and help now do too. The source already matched. |
| `s1.ltc_payout@i1040gi:p91` | b | The question is line 26 (LTC, accelerated death benefits). Lines 8 and 12 (Archer and Medicare Advantage MSA distributions) were asked nowhere; `scope.archer_msa` now asks about money put into or taken out of either account, and refuses at the same reader. |
| `s2.amt_owed@i6251:p1` | b (bank) | The source said "required to file Form 6251", but the prompt asked only "owe AMT". The prompt now asks both. |
| `s2.iso@i6251:p1`, `@p4` | c (landing-08) | The line 2i adjustment falls when the stock vests. ISO stock exercised earlier that vests in 2025 is missed. The fix needs a new question beneath the options parent. |
| `s2.options_any@i6251:p1`, `@p4` | c (landing-08) | The same case one level up: the parent asks about 2025 exercises and sales only. |
| `s3.adoption_any@i1040gi:p24` | b | A code T benefit with no cost paid by the filer answered No. The parent now says "pay (or have an employer pay)", so the filer reaches `scope.adoption_benefits` (refuses). |
| `sa.mortgage_over_limit@i1040sca:p8` | b (bank help) | The draft defect (married filing separately limits) cannot arise: MFS is refused at `scope.ready_credits` (`s3.mfs`), which the full profile requires. A real gap remained: "the loans on your home" vs the limit on the main and second home together. The help now says to count a second home. |
| `sa.personal_property_tax_any@i1040sca:p3` | b (bank help) | The page counts territory taxes with state and local; the help now says so. |
| `scope.business_before@i1040gi:p91` | c (landing-05) | An NOL from a personal casualty with no business is gated out of `scope.nol`. The fix is a gate change. |
| `scope.church_exempt_wages@i1040sse:p1` | b | Spouse phrase added. |
| `scope.education_recapture@i1040gi:p34` | b | It asked whether you were refunded; the page's trigger is a refund or aid "for the student". It now asks about any student the credit was claimed for, and about fees as well as tuition. |
| `scope.f8978@i1040gi:p34` | b | Spouse phrase added. |
| `scope.medicaid_waiver@i1040gi:p24` | b (bank help) | The question is the in-home (excludable) case. Taxable pay for care elsewhere with no W-2 is wages not on a W-2: `scope.pay_no_w2` asks it on the same tick screen, and it refuses at the same reader (`scope.other_income`). The help now says so. The question was not widened: that would refuse W-2-paid caregivers who get a correct return today (N9). |
| `scope.passive@i8582:p1` | b | Spouse phrase added; the help counts a loss held back from an earlier year. |
| `scope.pfic@i1040gi:p34`, `@p114` | b | "A foreign investment fund" is now "a fund, or a company whose income or assets are mostly investments". |
| `scope.reforestation@i1040gi:p99` | b | "own" is now "own or lease"; the page has no ownership condition. That leased land qualifies is my reading of section 194 / Reg. 1.194-3, not text in the archive. The change only widens a refusal. |
| `scope.religious_work@i1040sse:p1` | b (bank help) | The help names a Christian Science practitioner, whom `scope.clergy` beneath already names. |
| `scope.reservist_repaid@i1040gi:p95` | b | Spouse phrase added. |
| `scope.se_plan_other@i1040gi:p93` | b | "In 2025, did you put money" is now "... for 2025", with help counting money put in after the year, as the SEP/SIMPLE sibling does. |
| `sd.sold_other@i1040sd:p6` | b | "Paid over more than one year" is now "any payment ... in a year after the year of the sale". The child `sd.installment` is reworded the same way. |

## Changed lines (form line ids)

- `forms/2025/scope.yaml` (label and source): `scope.archer_msa`, `scope.education_recapture`, `scope.reservist_repaid`,
  `scope.church_exempt_wages`, `scope.f8978`, `scope.passive`, `scope.pfic`, `scope.reforestation`, `scope.se_plan_other`.
- `forms/2025/s3.yaml`: `s3.adoption_any`. `forms/2025/sd.yaml`: `sd.sold_other`, `sd.installment`.
  `forms/2025/person.yaml`: `person.ira_owner`. `forms/2025/dependent.yaml`: `dependent.eic_ssn_known` (cite only).
- `interview/2025/questions.yaml` (bank): prompt `person.ira_owner`, `s1.digital_income`, `s2.amt_owed`,
  `s3.adoption_any`; tick `s1.digital_income`, `scope.archer_msa`, `scope.education_recapture`, `sd.sold_other`,
  `s3.adoption_any`; help `s1.digital_income`, `scope.medicaid_waiver`, `scope.religious_work`, `scope.passive`,
  `scope.se_plan_other`, `scope.education_recapture`, `s3.adoption_any`, `sa.mortgage_over_limit`,
  `sa.personal_property_tax_any`.
- `reviews/2025/consumers.json`: 26 rulings added (21 `same`, 5 `differs`); the `dependent.eic_ssn@i1040gi:p22`
  ruling removed (stale). The question phrases of 22 existing rulings were re-quoted, because the question's text
  changed: `scope.archer_msa` (9), `scope.reforestation` (8), `person.ira_owner` (3), `scope.education_recapture`
  (2). Their verdicts and reasons are unchanged.
- Generated: `rendered/2025/*` (`asset.md` and `index.md` differed from the base after the first build, before any edit
  of mine), `reports/2025/{citations,consumers,false_no_currency,person_wording,question_currency,screen_currency}.md`.

No fixture input, expected value, refusal, check or baseline was edited.

## Pending bugs

- Open, cited by `differs` rulings: `BUG-0642` (casualty NOL), `BUG-0643` (ISO vesting).
- Fixed here: 02, 03, 04, 06, 07, 09, 10, 11, 12, 13, and 01 (as restated above).
- **For the coordinator:** `tools/check_bug_inventory.py` forbids changing a pending file committed at HEAD, so I could
  not add `Status`/`Fix` lines to the entries fixed here, nor correct landing-01. Its symptom (married filing
  separately limits) is wrong: that status is refused. The real defect is the second home. Before or at the
  `--assign` merge, decide whether to amend these entries (status fixed, with the fixes listed above) or drop
  landing-01.

## Doubts

- landing-08 and 05 were verified against the page (i6251 p. 4 Line 2i; i1040gi p. 91 with `scope.nol`'s own help);
  not fixed.
- The reforestation lease reading rests on the Code, not the archive (above).
- `s2.amt_owed`: the prompt now names Form 6251, but a filer still cannot know without the arithmetic whether
  statement 4 of Who Must File applies (negative adjustments). That is a design limit of asking, not of this pair.
- Review debt: every changed question is due for its question, screen and false-no reviews at the next pass. That is
  expected; these forms are about to be reviewed.

## Verification (run in this worktree, on the final tree)

- `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render`: build OK, 68 rendered.
- `python3 tools/check_consumers.py`: 0 new, 0 stale. `--jurisdiction ny`: 0 new, 0 stale.
- `node engine/dist/main.js test-fixtures`: 1987/1987 passed. `test-fixtures --ny`: 357/357 passed.
- `python3 tools/citations.py --strict`: 0 findings (input quotes 0 new); `--jurisdiction ny`: 0 findings.
- `check_questions.py`, `check_screens.py`, `check_false_no.py`: exit 0, 0 new each (changed questions are listed as
  due at the next pass, as expected).
- `node engine/dist/main.js spouse-wording --report --check`: current after regenerating the report (the IRA question's
  shown forms changed).
- `tick-groups`: passed. `interview-rules`: 0 problems. `interview-coverage`: 0 problems, 492 rows.
- `python3 tools/check_bug_inventory.py`: OK (13 pending, unchanged).
- `tools/check_all.sh --tier fast`: exit 1. Failed: `check_logs`, `ny_check_logs` (paid reviews pending; `ny_it201`,
  not touched here), `classm_skipped` (expected), and `bookkeeping_self_tests` (`green_self_test`: the tier-paths
  self-test says `engine/src/draft-walk.ts`, `tick-groups-check.ts` and `tick-groups.ts` refer to `docs/*` and are not
  in READERS. I changed no engine or tools file, so this comes from the base tree; for the coordinator). Every other
  step passed, consumers and ny_consumers included.

Not added: coverage rows for the two newly reached refusals (an Archer or Medicare Advantage MSA distribution at
`scope.archer_msa`; an employer-paid adoption cost reaching `scope.adoption_benefits`). The existing rows pass; the
protocol (3.7) asks for one row per refused situation, so these two are a follow-up.
