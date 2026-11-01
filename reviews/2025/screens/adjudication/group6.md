# Screen adjudication, group 6 (2026-10-31, T-091 round)

Brief: `BRIEF.md`, with `.transcription/proposed/fixr2/BRIEF.md` ("T-091 round"). Screens: 2 (`dependent.married`,
`dependent.multiple_support`), re-reviewed because T-091 added the refusal `dependent.qr_kidnapped` to
`dependent.qualifying_relative`, a line both screens gate (the prompts now include p501 p. 18). Neither question was
reworded by T-091. Findings: 6. Classes: accepted WIDE 5, out of scope 1. No PENDING defect.

Evaluation: `node engine/dist/main.js eval` on `stage8.hoh.child.ctc` and `stage8.hoh.parent.test1`
(`fixtures/2025/stage8.json`), filed single, with the one screen changed; scratch in
`/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091-completeness-screens/w/`.

## `dependent.married`

Prompt hash: `53ffe965f12475e84ec4c3d10e3405d8ae5346695a8ed40b1138bb6194612d84`. Gates `dependent.qualifying_child`,
`dependent.qualifying_relative`, `dependent.eic_child`. Round 1 PENDING-0-2 (BUG-0229) remains closed.

| # | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi pp. 21, 44 | A married person with no joint return, or a refund-only one, is refused on qualifying_child and qualifying_relative though computable; the refusal is still needed on eic_child (Married child). Eval: Yes refuses lines 19 and 24 at `dependent[child].married`; No gives line 19 $2,200. As rounds 1 and 4. |
| 1 | WIDE | accepted WIDE | i1040gi pp. 17, 44 | A person widowed in 2025 on a refund-only joint return is refused though `dependent.joint_return` carves that return out. As rounds 1 and 4. |
| 2 | UNCLEAR | out of scope | i1040gi p. 17, "Who isn't filing a joint return for 2025" | New. "Is a joint return being filed" follows the source's tense. The case needs a person widowed in 2025 (a person married at year end answers Yes on the first clause) and a filer who does not know that person's filing plans. `dependent.joint_return` asks the identical clause and computes, so no rewording of the screen changes the outcome; a later joint return disallows the claim by amendment, as under the source. No EIC exposure (p. 44 reaches only a person married at year end). |

## `dependent.multiple_support`

Prompt hash: `ffe43ba7497e64b5adf3e654eaf31be9315950c28532eac04023c39ae3bb5331`. Gates `dependent.qualifying_relative`.

| # | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi p. 19, Step 4 | A contributor whom another contributor claims answers Yes and is refused, though `supported` No would give no qualifying relative. Eval (`supported` No): Yes refuses lines 19 and 24 at `dependent[parent].multiple_support`; No gives line 19 $0, line 24 $17,867. As group 3 finding 4. |
| 1 | WIDE | accepted WIDE | i1040gi p. 21, "special rules may apply" | A filer the multiple support rule cannot help is refused where the computed result would be right. As group 3 finding 5. |
| 2 | UNCLEAR | accepted WIDE | i1040gi p. 21, "you and another person(s) provided more than half" | Counting the person's own funds or public assistance among "others" only turns No into Yes (refusal). The source's contributors are persons who could claim the dependent, so a true multiple support situation is Yes on either reading; where the state or the person provided over half there is none, and No computes correctly. As group 3 finding 6. |

## T-091 interaction

`dependent.qr_kidnapped` (age under 19 and kidnapped) sits beside `dependent.married` and `dependent.multiple_support`
on `dependent.qualifying_relative`; the three refuse independently, and neither model raised a finding on the new gate.
`dependent.hoh_test2`'s qualifying-child branch still reads `dependent.married` = false, so a married qualifying child
cannot reach head of household without passing through the refusal on `dependent.qualifying_child`.

Note: `check_screens.py` asks for both screens to be ruled again with the hashes above, and also prints "no longer fails;
remove it from rulings.json" for their existing `unruled:` keys. The entries in `group6.json` (same keys) are meant to
replace those keys; `reviews/2025/screens/rulings.json` was not edited.
