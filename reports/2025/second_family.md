# Second-family review comparison — 2025

Summary: 2 form-kind pair(s) with logs from Claude and deepseek; agreement floor overall 55.3% (26/47 lines judged by both); 0 pair(s) at or above the 90% floor, 2 below; independence yield 20 line(s); both families disputed 1

Written by `tools/transcription/compare_families.py` on 2026-10-22 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

- **Agreement floor**: the share of lines judged by both on which the two families' verdicts agree and neither disputes the project (transcription and class M: both AGREE; render: both MATCH). The integrity plan (item 1.3) sets a provisional floor of 90%; a run below it does not count as a second-family assertion. A denominator of a few lines is marked as such: the floor on one line is one verdict.
- **Independence yield**: lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where the Claude log agreed or matched, with the second family's reason. Zero is a visible result.
- **Both disputed**: lines both families disputed; **Claude only**: lines only the Claude run disputed.
- **Not judged by both**: lines one log has and the other does not, or that either marked MISSING; left out of the floor.
- **Stale**: a log whose recorded subject hash is not the current subject (subjects.py); its verdicts describe an earlier form or rendering.

## Transcription agreement

| form | second family (model) | lines judged by both | both agree | floor | 90% floor | yield | both disputed | Claude only | not judged by both | stale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tcw | deepseek (deepseek-v4-pro) | 1 | 0 | 0.0% | below (1 line) | 0 | 1 | 0 | 0 | - |
| **all** | | 1 | 0 | 0.0% | | 0 | 1 | 0 | 0 | |

### Independence yield

None: every line the second family disputed, the Claude run disputed too.

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| tcw | deepseek | tax | DISAGREE | DISAGREE | This line serves as both the printed Tax result and the intermediate value `tax` referenced by other forms. |

## Render comparison

| form | second family (model) | lines judged by both | both agree | floor | 90% floor | yield | both disputed | Claude only | not judged by both | stale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tcw | deepseek (deepseek-v4-pro) | 46 | 26 | 56.5% | below | 20 | 0 | 0 | 0 | - |
| **all** | | 46 | 26 | 56.5% | | 20 | 0 | 0 | 0 | |

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| tcw | deepseek | (d) (hoh.row1.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $6,825.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (hoh.row2.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $8,892.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (hoh.row3.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $24,676.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (hoh.row4.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $32,191.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (hoh.row5.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $44,718.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfj.row1.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $10,172.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfj.row2.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $14,306.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfj.row3.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $45,874.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfj.row4.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $60,905.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfj.row5.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $75,937.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfs.row1.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfs.row2.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfs.row3.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfs.row4.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (mfs.row5.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $37,968.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (single.row1.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (single.row2.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (single.row3.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (single.row4.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |
| tcw | deepseek | (d) (single.row5.tax) | MISMATCH | The IRS line (d) is the 'Subtraction amount' of $42,979.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction. |

### Lines both families disputed

None.

## Class M hand-work

No form has a second family's log of this kind.
