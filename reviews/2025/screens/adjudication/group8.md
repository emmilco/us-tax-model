# Screen adjudication, group 8 (2026-11-03, refresh round)

Brief: `.transcription/proposed/fixr2/BRIEF.md`, "Refresh round (2026-11-03)". Screens: 7, rerun after the refresh fixes
BUG-0391 to BUG-0401 changed their questions, gated lines or cited pages (`check_screens.py` reported them as `rerun`).
Rulings are in `rulings.json` under `unruled:<screen>` with each review's `prompt_sha`; earlier rulings were reused
where the finding repeats group 7, after checking the current lines.

Findings: 29. Classes: accepted WIDE 10, covered 8, low 6, accepted (minor UNCLEAR, leans WIDE) 3, model error 1, out of scope / presentation 1. No defect of medium or higher.
Lows are batched as BUG-0402 and listed in `.transcription/proposed/rf/lows.md`.

## Refresh round

| screen | findings (n: class) | disposition |
| --- | --- | --- |
| `f4952.unsupported` | 0: low; 1: low; 2: accepted WIDE; 3: accepted (minor UNCLEAR, leans WIDE); 4: accepted (minor UNCLEAR, leans WIDE) | Low only. The two NARROW findings are a definition gap in f4952.line1 (investment interest is not defined), BUG-0402; the rest WIDE or minor UNCLEAR leaning WIDE. |
| `f8960.refund` | 0: covered; 1: accepted WIDE; 2: accepted WIDE; 3: accepted (minor UNCLEAR, leans WIDE) | No defect; as group 7 (rechecked): the section 1411 NOL case is screened by f8960.unsupported; the rest WIDE or leans WIDE. |
| `f8960.unsupported` | 0: covered; 1: covered; 2: low; 3: low; 4: covered; 5: accepted WIDE; 6: accepted WIDE | No medium. Findings 0, 1 and 4 covered by siblings as in group 7; finding 2 partly covered, with the life insurance surrender gain low (BUG-0402); finding 3 low (BUG-0402); WIDE accepted. |
| `retirement.special` | 0: covered; 1: low; 2: model error; 3: accepted WIDE | No medium. BUG-0393's additions (qualified disaster recovery distribution and repayment) introduced no error. Finding 1 (a disaster-canceled home-purchase recontribution) is low, BUG-0402, the same point as completeness scope#1; finding 2 is a model error. |
| `s8812.puerto_rico` | 0: accepted WIDE; 1: accepted WIDE; 2: out of scope / presentation | No defect; as group 7 (rechecked): WIDE accepted; the residency-term doubt can only lower the credit. |
| `sales.special` | 0: accepted WIDE; 1: accepted WIDE; 2: low | No medium. WIDE accepted as group 7; the UNCLEAR on a home with past depreciation is low (BUG-0402). |
| `scope.other_income` | 0: covered; 1: covered; 2: covered | No defect: each NARROW or UNCLEAR item has its own refusal on scope.ready, s1.line9 or the EIC. |

## Errors introduced by the refresh fixes

None found. BUG-0393's new `retirement.special` items (a qualified disaster recovery distribution or its repayment) and
BUG-0401's reach change for the Form 8960 screens drew no finding against the new wording. BUG-0393 stated the
conditions of exceptions 01 to 04 only; the remaining exceptions are completeness retirement#4 (low).
