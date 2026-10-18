# Screen review (T-008) — adjudication

One-time review by `tools/transcription/screen_review.py`, 2026-10-17: an isolated model judged each of the 34 screens (yes/no inputs that refuse lines) against the archived instruction pages of every line the screen gates. NARROW (a truthful no lets an unsupported case compute as zero) is the dangerous direction; WIDE (a yes refuses a case the tool computes) is safe and accepted; UNCLEAR is wording a filer could read either way.

## Rounds

1. All 34 screens: 123 findings (27 NARROW verdicts). Adjudicated: 25 screens reworded (form source, label and every interview prompt); findings covered by a sibling screen gating the same lines, or by a derived refusal, were not changed.
2. The 25 reworded screens again: four more rewordings (gift.special, sales.special, f8959.unsupported, scope.other_income), one of them repairing a narrowing introduced in round 1 (gift.special had lost the single-item case).
3. The four, then gift.special once more; final clarifications to scope.schedule1, qbi.unsupported, sd.other_forms, dependent.married and dependent.multiple_support, and the value-based appraisal trigger for gift.special, were applied from the findings without a further run.

Raw responses are in `.transcription/screens/` (git-ignored); `screen_review.json` holds the last run of each screen. Total cost about $8 by the CLI estimate.

## Final state, per screen

| screen | last verdict | findings left | disposition |
| --- | --- | --- | --- |
| `dependent.divorced_rule` | UNCLEAR | 3 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `dependent.married` | WIDE | 3 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `dependent.multiple_support` | WIDE | 2 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `dependent.other_claimant` | NARROW | 3 | reworded; a Form 8332 release is screened by dependent.divorced_rule. |
| `f4952.alternative_allocation` | NARROW | 3 | carryover and line 5 expenses are screened by f4952.carryover and f4952.unsupported (all three gate the same lines). |
| `f4952.carryover` | NARROW | 2 | line 5 expenses are screened by f4952.unsupported; 'carryover' means the 2024 Form 4952 line 7 amount. |
| `f4952.unsupported` | NARROW | 3 | reworded; a carryover is screened by f4952.carryover; expenses that are not deductible (miscellaneous itemized, passive) are not line 5 amounts. |
| `f8959.unsupported` | WIDE | 2 | reworded; WIDE only (a self-employment loss; territory forms other than 499R-2). |
| `f8960.refund` | NARROW | 3 | reworded; a section 1411 NOL is screened by f8960.unsupported. |
| `f8960.unsupported` | NARROW | 2 | reworded; a state or local tax refund is screened by f8960.refund. |
| `gift.special` | NARROW | 4 | reworded; the value-based appraisal trigger (i8283: 'a qualified appraisal is required for any gift of property valued in excess of $5,000') was added after this run. |
| `person.rrta` | WIDE | 1 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `qbi.unsupported` | UNCLEAR | 3 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `s2.amt` | NARROW | 5 | the other Schedule 2 amounts are screened by s2.other, which gates the same lines. |
| `s2.other` | WIDE | 2 | reworded; Form 8919 tax falls under 'any amount on Schedule 2'. |
| `s8812.combat_pay` | WIDE | 1 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `s8812.puerto_rico` | WIDE | 2 | WIDE only. |
| `sa.charity_limited` | NARROW | 6 | other itemized items are screened by sa.unsupported and sa.excluded_income, which gate the same lines. |
| `sa.dependent` | NARROW | 1 | reworded; the not-required-to-file exception is part of when someone can claim you (i1040gi p. 19, Step 4 question 5), not an EIC-only rule. |
| `sa.excluded_income` | COVERS | 0 | reworded; other itemized items are screened by sa.unsupported and sa.charity_limited. |
| `sa.spouse_extra` | COVERS | 0 | remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `sa.unsupported` | NARROW | 2 | reworded; a charitable carryover is screened by sa.charity_limited; territory taxes answered yes refuse a case the tool computes (safe). |
| `sales.special` | WIDE | 3 | reworded; WIDE only. |
| `sb.fbar_required` | NARROW | 4 | nominee, accrued interest, OID, premium and savings-bond items are screened by sb.unsupported (all four Schedule B screens gate the same lines); FBAR wording is the form's. |
| `sb.form8938` | NARROW | 6 | as sb.fbar_required. |
| `sb.line8` | NARROW | 6 | as sb.fbar_required; the foreign-trust question is Schedule B line 8's own wording. |
| `sb.unsupported` | WIDE | 3 | reworded; remaining items are WIDE or catch-all wording. |
| `scope.credits` | UNCLEAR | 1 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `scope.other_income` | NARROW | 3 | reworded; an NOL deduction and the foreign earned income exclusion are Schedule 1 items (scope.schedule1). |
| `scope.other_line16` | NARROW | 2 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `scope.schedule1` | NARROW | 4 | reworded; Schedule 2 lines 5, 6 and 13 for Schedule 8812 line 22 are also gated by s2.other. |
| `scope.schedule1a` | WIDE | 3 | reworded; remaining findings are WIDE (accepted) or minor UNCLEAR wording (accepted). |
| `sd.carryover` | NARROW | 3 | reworded; form-sourced and K-1 amounts are screened by sd.other_forms (both gate the same lines). |
| `sd.other_forms` | NARROW | 4 | reworded; a carryover is screened by sd.carryover. |

## Accepted as known limits

- `scope.schedule1a` asks whether the filer qualifies for a Schedule 1-A deduction, so a filer born before January 2, 1961 is refused even where the senior deduction phases out to zero at high income; the phase-out amounts are not in the archive (Schedule 1-A and its instructions are not fetched).
- WIDE findings throughout: each refuses a case the tool could compute; refusing is the safe direction and costs coverage only.

