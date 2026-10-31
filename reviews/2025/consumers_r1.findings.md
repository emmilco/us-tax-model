# New-consumer definition check, round 1: findings

Scope: the 40 open pairs from `tools/check_consumers.py` (2 new, 38 whose question changed since the baseline).
All 40 are ruled "same" in `reviews/2025/consumers.json`. The 2 stale baseline keys
(`scope.other_line16@i1040gi:p36` and `scope.schedule1@i1040gi:p43`) are removed.

## "differs" verdicts

None.

## Close calls (ruled "same"; recorded for adjudication)

1. `person.itin_applied@i8863:p3` and `dependent.tin@i8863:p2`. The page requires a TIN *issued* by the due date
   ("Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)").
   The questions also count an ITIN or ATIN *applied for* by then. The ruling is "same" because Pub. 970 says
   "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues
   an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due
   date of the return." That sentence is the only one of its kind in the archived Pub. 970, and it is in the American
   opportunity credit chapter. The line also serves the lifetime learning credit. For that credit, the TIN-by-the-due-date
   rule comes only from i8863 Table 1, and the archived Pub. 970 lifetime learning credit text never mentions a TIN. If
   the deeming does not extend to the lifetime learning credit, these pairs differ for that credit. Witness shape: a student with
   `person.tin` false, `person.itin_applied` true, paid expenses and a Form 1098-T, who is allowed the lifetime
   learning credit.
2. `person.itin_applied@i1040gi:p17`. p. 17 says the credit for other dependents needs an SSN or ITIN "issued on or
   before the due date". The ruling relies on the deeming sentence on p. 22, which `amb.2025.ctc_spouse_itin_application`
   already applies to the credit for other dependents.
3. `scope.schedule1@i1040gi:p40` (`eic.step2_other`). EIC Step 2, question 4 also names "income or loss from a
   passive activity". That is not asked by `scope.schedule1` or `scope.other_line16`, the two inputs this line reads. It is
   asked by `scope.other_income`, which refuses the return. The line is correct only because that other gate exists.
4. `f5695.joint_occupancy@i5695:p7`. Line 32a applies to joint occupants "who are claiming the energy efficient home
   improvement credit", but `f5695.line32a` tests joint occupancy alone. The input matches the page's meaning of
   "joint occupants", and line 30 refuses joint occupancy, so no return this tool completes has the box checked.
