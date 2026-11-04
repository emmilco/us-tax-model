# Screen adjudication, group 7 (2026-11-03, backlog round)

Brief: `BRIEF.md`, with `.transcription/proposed/fixr2/BRIEF.md` ("Backlog round (2026-11-03)"). Screens: 15, re-reviewed
after the income, credits-misc, ptc-sa and person-dep packages changed their questions, gated lines or cited pages
(`check_screens.py` reported them as `rerun`). Rulings are in `rulings.json` under `unruled:<screen>` with each review's
`prompt_sha`. The stale `unruled:household.credit_disallowed` was removed: T-101 replaced that screen with
`household.ctc_disallowed_claim` and `household.eic_disallowed_claim`.

Findings: 53. Classes: accepted WIDE 26, covered 16, accepted (minor UNCLEAR) 3, out of scope / presentation 3,
defect 3, model error 1, accepted (minor UNCLEAR, leans WIDE) 1. PENDING defects: PENDING-7-1, PENDING-7-2 and
PENDING-7-3, all medium. They are written up in `.transcription/proposed/bklg/screens.findings.md`, which also lists the
low items.

## Package changes: wider or narrower than the source

| screen | package change | effect | ruling |
| --- | --- | --- | --- |
| `s1.alimony_unsupported` | income PENDING-1: a part continuing after death | wider; matches p504 p. 15 | closes PENDING-4-8 |
| `s1.uc_unsupported` | income PENDING-2: self-employed payments counted | wider | closes PENDING-4-9 |
| `retirement.special` | income PENDING-4: survivor annuities and full in-kind rollovers carved out | narrower; matches i1040gi p. 30 and p575 pp. 23, 34. A survivor whose retiree used the General Rule, or whose annuity started before November 19, 1996, is still refused by the last item | correct |
| `sales.special` | income PENDING-6: entity-held collectibles named | wider | closes PENDING-4-10 |
| `gift.special` | credits-misc PENDING-4: publicly traded defined | the exception now matches i8283 p. 9 word for word | closes PENDING-4-5 |
| `refund.not_2024` | credits-misc PENDING-5: tax paid before 2024 | wider | closes PENDING-4-7 |
| `f5695.joint_occupancy` | credits-misc PENDING-1: any home with Part II costs | wider | closes PENDING-4-2 |
| `f8960.unsupported` | credits-misc PENDING-3: section 404(k) dividends | wider | closes PENDING-4-3 |
| `f4952.*` | credits-misc PENDING-6: reached only when `f4952.used` | narrower in reach only (returns that file no Form 4952, f4952 p. 3) | correct |
| `scope.schedule1` | person-dep PENDING-5: qualified church-controlled organizations | wider | closes PENDING-4-11 |
| `f8962.premium_adjust`, `.alloc`, `.other` | ptc-sa PENDING-1: `b_zero` added to the line 24/25 refusals | gated lines only; questions unchanged | BUG-0327's unpaid-share part is covered by `f8962.other` |
| `scope.other_line16` | prompt changed through the scope.yaml cited pages only | none | as group 4 |

No package change made a screen narrower than its source.

## Per screen

| screen | findings (n: class) | disposition |
| --- | --- | --- |
| `f8962.premium_adjust` | 0 covered; 1 accepted WIDE | Unpaid premium: `f8962.other` gates lines 24 and 25. A refund already netted in column A is refused, which is safe. |
| `gift.special` | 0, 1 accepted WIDE | Reduced deduction of $5,000 or less, and Section A vehicles, are refused. |
| `refund.not_2024` | 0 accepted WIDE | A non-itemizer is refused though line 1 would be zero. |
| `retirement.special` | 0 covered (`retirement.bad_code`); 1 **defect** PENDING-7-1; 2 **defect** PENDING-7-2; 3 model error (`retirement.plan_excluded`); 4 accepted WIDE | See the findings file. |
| `s1.alimony_unsupported` | 0, 1 covered (amount questions, cash only); 2 **defect** PENDING-7-3; 3, 4 accepted WIDE; 5 covered (`s1.alimony` counts only payments before a post-2018 change) | See the findings file. |
| `s1.uc_unsupported` | 0, 1, 2 accepted WIDE; 3 out of scope / presentation | Paystub labels are a question about the filer's records. |
| `sales.special` | 0, 1 accepted WIDE; 2 accepted (minor UNCLEAR) | Tiered look-through is low. |
| `scope.other_line16` | 0 out of scope (opening clause); 1 covered (`s1.line8_other` line 8d, `sa.excluded_income`); 2 out of scope (Schedule J elective); 3, 4 accepted WIDE | As group 4. |
| `scope.schedule1` | 0 covered (`sc.passive`, `scope.other_income`); 1 covered (`s1.sc_1a`); 2 covered (Schedule E, `scope.other_income`); 3 accepted WIDE | As group 4. |
| `f4952.alternative_allocation` | 0, 1 covered (`f4952.unsupported`); 2 accepted WIDE | As group 4. |
| `f4952.unsupported` | 0, 1, 2 accepted WIDE; 3 accepted (minor UNCLEAR) | At-risk wording is low. |
| `f5695.joint_occupancy` | 0 accepted WIDE; 1 accepted (minor UNCLEAR) | The parenthetical settles the reading. |
| `f8960.unsupported` | 0 covered (`f8960.refund`); 1 covered (`scope.other_line16`, Form 8814); 2 covered (`oi8z` refuses other kinds); 3 covered (`sa.unsupported`); 4 accepted WIDE; 5 covered (`scope.schedule1`) | As group 4. |
| `f8962.alloc` | 0 accepted WIDE | `f8962.other` refuses APTC for someone in no one's tax family in any case. |
| `f8962.other` | 0 to 3 accepted WIDE; 4 accepted (minor UNCLEAR, leans WIDE) | Every reading that matters gives Yes. |

Not evaluated: no case needed the engine. Every sibling gate named above was checked in the current YAML (the gate exists,
its question has the quoted text, and it gates the same lines or `scope.ready`).
