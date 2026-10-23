# Second-family review comparison — 2025

Summary: 2 form-kind pair(s) with logs from Claude and deepseek; agreement floor overall 97.9% (46/47 lines judged by both); 1 pair(s) at or above the 90% floor, 1 below; independence yield 0 line(s); both families disputed 0

Written by `tools/transcription/compare_families.py` on 2026-10-22 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

- **Agreement floor**: the share of lines judged by both on which the two families' verdicts agree and neither disputes the project (transcription and class M: both AGREE; render: both MATCH). The integrity plan (item 1.3) sets a provisional floor of 90%; a run below it does not count as a second-family assertion. A denominator of a few lines is marked as such: the floor on one line is one verdict.
- **Independence yield**: lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where the Claude log agreed or matched, with the second family's reason. Zero is a visible result.
- **Both disputed**: lines both families disputed; **Claude only**: lines only the Claude run disputed.
- **Not judged by both**: lines one log has and the other does not, or that either marked MISSING; left out of the floor.
- **Stale**: a log whose recorded subject hash is not the current subject (subjects.py); its verdicts describe an earlier form or rendering.

## Transcription agreement

| form | second family (model) | lines judged by both | both agree | floor | 90% floor | yield | both disputed | Claude only | not judged by both | stale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tcw | deepseek (deepseek-v4-pro) | 1 | 0 | 0.0% | below (1 line) | 0 | 0 | 1 | 0 | - |
| **all** | | 1 | 0 | 0.0% | | 0 | 0 | 1 | 0 | |

### Independence yield

None: every line the second family disputed, the Claude run disputed too.

### Lines both families disputed

None.

## Render comparison

| form | second family (model) | lines judged by both | both agree | floor | 90% floor | yield | both disputed | Claude only | not judged by both | stale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tcw | deepseek (deepseek-v4-pro) | 46 | 46 | 100.0% | pass | 0 | 0 | 0 | 0 | - |
| **all** | | 46 | 46 | 100.0% | | 0 | 0 | 0 | 0 | |

### Independence yield

None: every line the second family disputed, the Claude run disputed too.

### Lines both families disputed

None.

## Class M hand-work

No form has a second family's log of this kind.
