# Second-family review comparison — 2025

Summary: 124 form-kind pair(s) with logs from Claude and deepseek; ruled model-error noise 9.8% (247/2518 second-family lines judged; pending reviews are provisional); 46 eligible, 78 pending; raw agreement 73.0% (diagnostic only); current independence yield 203 line(s); both families disputed 419

Written by `tools/transcription/compare_families.py` on 2026-10-27 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

- **Noise rule** (owner's decision 12, integrity plan item 1.3): second-family disputes ruled **model error**, divided by the lines that family judged, must be at most 10% for each form-kind run. Findings, representation differences, scope differences and ambiguities are not model noise. The threshold uses integer arithmetic; 1/10 passes and 1/9 does not. Rates for pending reviews are provisional: an unresolved objection has not yet been classified, and zero ruled model errors does not mean every objection was correct.
- **Eligibility** also requires current subjects/sources, the named second-family model, no missing or invalid verdicts, and no open or unclassified ruling. Empty reviews earn no assertion. Optional-family results can remain pending without becoming evidence.
- **Raw agreement** is retained as a diagnostic only. A correct objection must not disqualify an independent reader.
- **Current independence yield**: lines the second family disputed (DISAGREE, MISMATCH or UNCLEAR) where the Claude log agreed or matched, with the second family's reason. This describes current logs; findings fixed before a rerun remain in BUG_INVENTORY.md and are not erased by a current yield of zero.
- **Both disputed**: lines both families disputed; **Claude only**: lines only the Claude run disputed.
- **Not judged by both**: lines one log has and the other does not, or that either marked MISSING; left out of the floor.
- **Stale**: a log whose recorded subject hash is not the current subject (subjects.py); its verdicts describe an earlier form or rendering.

## Transcription agreement

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| asset | deepseek (deepseek-flash) | 16 | 2 | 12.5% | 10/16 (62.5%) | pending | 0 | 12 | 2 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 2/2 (100.0%) | pending | 0 | 2 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pass | 0 | 0 | 0 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 1/13 (7.7%) | pass | 1 | 0 | 0 | 0 |
| dcprov | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pending | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 14 | 3 | 21.4% | 6/14 (42.9%) | pending | 0 | 10 | 1 | 0 |
| div | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 18 | 8 | 44.4% | 9/18 (50.0%) | pending | 2 | 7 | 1 | 0 |
| f1040 | deepseek (deepseek-flash) | 52 | 25 | 48.1% | 25/52 (48.1%) | pending | 18 | 9 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 37 | 12 | 32.4% | 22/37 (59.5%) | pending | 15 | 7 | 3 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 1 | 6.7% | 0/15 (0.0%) | pending | 0 | 14 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 14 | 9 | 64.3% | 3/14 (21.4%) | pending | 1 | 4 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 33 | 12 | 36.4% | 0/33 (0.0%) | pending | 8 | 12 | 1 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 2 | 40.0% | 0/5 (0.0%) | pending | 0 | 3 | 0 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 15 | 71.4% | 0/21 (0.0%) | pending | 0 | 6 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 10 | 52.6% | 0/19 (0.0%) | pending | 1 | 8 | 0 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 22 | 91.7% | 0/24 (0.0%) | pending | 0 | 2 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 19 | 76.0% | 3/25 (12.0%) | pending | 3 | 3 | 0 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 7 | 43.8% | 0/16 (0.0%) | pending | 4 | 5 | 0 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 2 | 14.3% | 9/14 (64.3%) | pending | 7 | 5 | 0 | 0 |
| ftc | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 6 | 85.7% | 1/7 (14.3%) | pending | 0 | 1 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 11 | 4 | 36.4% | 5/11 (45.5%) | pending | 0 | 5 | 2 | 0 |
| interest | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 29 | 6 | 20.7% | 16/29 (55.2%) | pending | 0 | 22 | 1 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 0 | 1 | 0 | 0 |
| person | deepseek (deepseek-flash) | 74 | 26 | 35.1% | 25/74 (33.8%) | pending | 14 | 32 | 2 | 0 |
| qbi | deepseek (deepseek-flash) | 5 | 1 | 20.0% | 0/5 (0.0%) | pending | 2 | 2 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 26 | 23 | 88.5% | 0/26 (0.0%) | pass | 0 | 3 | 0 | 0 |
| refund | deepseek (deepseek-flash) | 11 | 3 | 27.3% | 5/11 (45.5%) | pending | 5 | 3 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 16 | 10 | 62.5% | 0/16 (0.0%) | pending | 2 | 4 | 0 | 0 |
| s1 | deepseek (deepseek-flash) | 27 | 19 | 70.4% | 6/27 (22.2%) | pending | 2 | 4 | 2 | 0 |
| s179 | deepseek (deepseek-flash) | 14 | 10 | 71.4% | 2/14 (14.3%) | pending | 1 | 2 | 1 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 8 | 18.6% | 34/43 (79.1%) | pending | 1 | 34 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 8 | 6 | 75.0% | 0/8 (0.0%) | pending | 1 | 1 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 9 | 5 | 55.6% | 4/9 (44.4%) | pending | 1 | 3 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 34 | 16 | 47.1% | 15/34 (44.1%) | pending | 12 | 6 | 0 | 0 |
| sa | deepseek (deepseek-flash) | 22 | 15 | 68.2% | 6/22 (27.3%) | pending | 2 | 5 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pass | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 4 | 3 | 75.0% | 0/4 (0.0%) | pending | 1 | 0 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 48 | 13 | 27.1% | 0/48 (0.0%) | pending | 19 | 15 | 1 | 7 |
| scope | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 21 | 2 | 9.5% | 0/21 (0.0%) | pending | 7 | 12 | 0 | 0 |
| sd | deepseek (deepseek-flash) | 55 | 7 | 12.7% | 4/55 (7.3%) | pending | 8 | 37 | 3 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 20 | 42.6% | 12/47 (25.5%) | pending | 2 | 19 | 6 | 0 |
| se | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 9 | 4 | 44.4% | 0/9 (0.0%) | pending | 0 | 5 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 19 | 12 | 63.2% | 1/19 (5.3%) | pending | 2 | 4 | 1 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 2 | 66.7% | 0/3 (0.0%) | pending | 0 | 0 | 1 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 6 | 33.3% | 7/18 (38.9%) | pending | 4 | 6 | 2 | 0 |
| w2 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 0 | 1 | 1 | 0 |
| **all** | | 934 | 415 | 44.4% | | | 146 | 342 | 31 | 7 |

Pending asset [deepseek]: model-error noise above 10%.
Pending carloan [deepseek]: model-error noise above 10%.
Pending dcprov [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending dependent [deepseek]: model-error noise above 10%; no passing current expression type validation: claude, deepseek; no verified current request context for claude: current expression/refusal validation fails; no verified current request context for deepseek: current expression/refusal validation fails; no passing current source-based partial-input checks: claude, deepseek.
Excluded internal adapters for div: div.screen. Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.
Pending div [deepseek]: no source-defined computed targets; internal adapter checks earn no tax-evidence credit; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending eic [deepseek]: model-error noise above 10%.
Pending f1040 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f2441 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f4562 [deepseek]: 14 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Excluded internal adapters for f4952: f4952.election. Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.
Pending f4952 [deepseek]: model-error noise above 10%.
Pending f5695 [deepseek]: 20 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8606 [deepseek]: 3 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8880 [deepseek]: 6 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8889 [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8959 [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8960 [deepseek]: model-error noise above 10%.
Pending f8995 [deepseek]: 9 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8995a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending ftc [deepseek]: model-error noise above 10%; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending g28 [deepseek]: model-error noise above 10%.
Pending gift [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending household [deepseek]: model-error noise above 10%.
Pending interest [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ira [deepseek]: model-error noise above 10%.
Pending mq [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending oi8z [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending otjob [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending person [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending qbi [deepseek]: 4 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending refund [deepseek]: model-error noise above 10%; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending retirement [deepseek]: 4 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s1 [deepseek]: model-error noise above 10%.
Pending s179 [deepseek]: model-error noise above 10%.
Pending s1a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending s2 [deepseek]: 2 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s3 [deepseek]: model-error noise above 10%.
Pending s8812 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending sa [deepseek]: 1 open, unclassified or interface-gap rulings; model-error noise above 10%.
Pending sb [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sc [deepseek]: 7 missing expected lines; 34 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending scope [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending scveh [deepseek]: 19 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sd [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending sdtw [deepseek]: model-error noise above 10%; no passing current expression type validation: claude; no verified current request context for claude: current expression/refusal validation fails.
Pending se [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sli [deepseek]: 5 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ssb [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tax_on_amount [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tcw [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tipjob [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending u1250 [deepseek]: model-error noise above 10%; no passing current expression type validation: claude, deepseek; no verified current request context for claude: current expression/refusal validation fails; no verified current request context for deepseek: current expression/refusal validation fails.
Pending w2 [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| clcw26 | deepseek | 3 | DISAGREE | (no reason given) |
| eic | deepseek | 1 | DISAGREE | (no reason given) |
| eic | deepseek | eic.self_employed | DISAGREE | (no reason given) |
| f1040 | deepseek | 11a | DISAGREE | (no reason given) |
| f1040 | deepseek | 11b | DISAGREE | (no reason given) |
| f1040 | deepseek | 15 | DISAGREE | (no reason given) |
| f1040 | deepseek | 18 | DISAGREE | (no reason given) |
| f1040 | deepseek | 1a | DISAGREE | (no reason given) |
| f1040 | deepseek | 22 | DISAGREE | (no reason given) |
| f1040 | deepseek | 24 | DISAGREE | (no reason given) |
| f1040 | deepseek | 25a | DISAGREE | (no reason given) |
| f1040 | deepseek | 25c | DISAGREE | (no reason given) |
| f1040 | deepseek | 27a | DISAGREE | (no reason given) |
| f1040 | deepseek | 28 (box) | DISAGREE | No input interface for the line 28 checkbox; assumed not checked (false). |
| f1040 | deepseek | 2a | DISAGREE | (no reason given) |
| f1040 | deepseek | 2b | DISAGREE | (no reason given) |
| f1040 | deepseek | 34 | DISAGREE | (no reason given) |
| f1040 | deepseek | 37 | DISAGREE | (no reason given) |
| f1040 | deepseek | 3b | DISAGREE | (no reason given) |
| f1040 | deepseek | 6d | DISAGREE | (no reason given) |
| f1040 | deepseek | 9 | DISAGREE | (no reason given) |
| f2441 | deepseek | 11 | DISAGREE | (no reason given) |
| f2441 | deepseek | 17 | DISAGREE | (no reason given) |
| f2441 | deepseek | 20 | DISAGREE | (no reason given) |
| f2441 | deepseek | 21 | DISAGREE | The $2,500 married-filing-separately amount is used whenever the filing status is married filing separately; the supplied interface has no separate considered-unmarried gate. |
| f2441 | deepseek | 22 | DISAGREE | No supplied input gives the amount of line 12 or 13 benefits from a sole proprietorship or partnership; this line is treated as zero. If nonzero, lines 24 through 26 are not determined. |
| f2441 | deepseek | 23 | DISAGREE | (no reason given) |
| f2441 | deepseek | 24 | DISAGREE | (no reason given) |
| f2441 | deepseek | 25 | DISAGREE | (no reason given) |
| f2441 | deepseek | 26 | DISAGREE | (no reason given) |
| f2441 | deepseek | 28 | DISAGREE | (no reason given) |
| f2441 | deepseek | 29 | DISAGREE | (no reason given) |
| f2441 | deepseek | 31 | DISAGREE | (no reason given) |
| f2441 | deepseek | 6 | DISAGREE | (no reason given) |
| f2441 | deepseek | 9a | DISAGREE | (no reason given) |
| f2441 | deepseek | 9c | DISAGREE | (no reason given) |
| f4952 | deepseek | 2 | DISAGREE | (no reason given) |
| f5695 | deepseek | 19f | DISAGREE | (no reason given) |
| f5695 | deepseek | 20c | DISAGREE | (no reason given) |
| f5695 | deepseek | 22c | DISAGREE | (no reason given) |
| f5695 | deepseek | 23c | DISAGREE | (no reason given) |
| f5695 | deepseek | 24c | DISAGREE | (no reason given) |
| f5695 | deepseek | 29g | DISAGREE | (no reason given) |
| f5695 | deepseek | 5b | DISAGREE | (no reason given) |
| f5695 | deepseek | 6a | DISAGREE | (no reason given) |
| f8889 | deepseek | 17b | DISAGREE | Uses subject_part when line 17a is true; otherwise uses all of line 16 when line 17a is false. If line 16 is zero, the tax is zero regardless of line 17a. |
| f8960 | deepseek | 10 | DISAGREE | (no reason given) |
| f8960 | deepseek | 9a | DISAGREE | (no reason given) |
| f8960 | deepseek | 9b | DISAGREE | (no reason given) |
| f8995 | deepseek | 11 | DISAGREE | Computed per the instructions as Form 1040 line 11a minus lines 12e and 13b; floored at zero because the line is NonNegDollars. |
| f8995 | deepseek | 12 | DISAGREE | Net capital gain is Form 1040 line 7a if no Schedule D, otherwise the smaller of Schedule D lines 15 and 16; it is floored at zero when zero or less, as the Schedule D instruction states and as the NonNegDollars type requires. |
| f8995 | deepseek | 2 | DISAGREE | The tool supports QBI from the Schedule C businesses entered; other QBI and PTP items are refused via qbi.unsupported. |
| f8995 | deepseek | 6 | DISAGREE | The tool supports only qualified section 199A dividends; PTP income or loss is refused via qbi.unsupported. |
| f8995a | deepseek | 27 | DISAGREE | Dividend-only computation: no qualified business income component is supplied, so the amount from line 16 is treated as zero. The supplied slice does not determine a nonzero QBI component. |
| f8995a | deepseek | 29 | DISAGREE | A prior-year REIT/PTP loss carryforward is outside the supported scope; qbi.unsupported refuses it. In the supported dividend-only case there is no carryforward. |
| f8995a | deepseek | 31 | DISAGREE | (no reason given) |
| f8995a | deepseek | 32 | DISAGREE | (no reason given) |
| f8995a | deepseek | 37 | DISAGREE | (no reason given) |
| f8995a | deepseek | 38 | DISAGREE | No patron DPAD is supplied; patron cases are refused by qbi.unsupported, so the supported amount is zero. |
| f8995a | deepseek | 39 | DISAGREE | (no reason given) |
| person | deepseek | Step 5 | DISAGREE | (no reason given) |
| person | deepseek | credit | DISAGREE | (no reason given) |
| person | deepseek | excess | DISAGREE | (no reason given) |
| person | deepseek | over | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_addtax | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_deduction | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_taxable | DISAGREE | (no reason given) |
| person | deepseek | person.income179 | DISAGREE | (no reason given) |
| person | deepseek | person.qbi | DISAGREE | (no reason given) |
| person | deepseek | person.s179_listed | DISAGREE | (no reason given) |
| person | deepseek | person.s179_nonlisted | DISAGREE | (no reason given) |
| person | deepseek | person.sc_1a | DISAGREE | (no reason given) |
| person | deepseek | person.tip_employers | DISAGREE | (no reason given) |
| person | deepseek | person.tip_reported | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.eligible | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.net_capital_gain | DISAGREE | (no reason given) |
| refund | deepseek | 1 | DISAGREE | The IRS says none of the refund is taxable if you did not itemize or elected general sales taxes; I set line 1 to zero in those cases so that line 9 is zero. |
| refund | deepseek | 2 | DISAGREE | (no reason given) |
| refund | deepseek | 4 | DISAGREE | If there were no 2024 itemized deductions, line 4 is set to zero because the worksheet is not used. |
| refund | deepseek | refund.has | DISAGREE | The IRS worksheet does not print a separate yes/no result; I encode has as true exactly when the taxable part on line 9 is greater than zero. |
| refund | deepseek | refund.taxable | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.is_ira | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.taxable | DISAGREE | (no reason given) |
| s1 | deepseek | 19a | DISAGREE | (no reason given) |
| s1 | deepseek | 2a | DISAGREE | (no reason given) |
| s179 | deepseek | s179.differs | DISAGREE | The IRS pages do not name this interface. Read here as whether the business income limitation reduces the deduction below the sum of lines 9 and 10, i.e. whether a carryover arises. |
| s1a | deepseek | 38 | DISAGREE | (no reason given) |
| s2 | deepseek | 11 | DISAGREE | (no reason given) |
| s3 | deepseek | 11 | DISAGREE | (no reason given) |
| s8812 | deepseek | 13 | DISAGREE | (no reason given) |
| s8812 | deepseek | 14 | DISAGREE | (no reason given) |
| s8812 | deepseek | 16a | DISAGREE | (no reason given) |
| s8812 | deepseek | 17 | DISAGREE | (no reason given) |
| s8812 | deepseek | 19 | DISAGREE | (no reason given) |
| s8812 | deepseek | 20 | DISAGREE | (no reason given) |
| s8812 | deepseek | 21 | DISAGREE | No root-level aggregate for Form W-2 boxes 4 and 6 is supplied, so the supported slice enters zero; RRTA and unsupported Additional Medicare situations refuse. |
| s8812 | deepseek | 22 | DISAGREE | Schedule 2 line 13 other taxes are outside this interface and are zero only when s2.other is false; line 5 is read from f8959.line24 and line 6 from f8960.line17. |
| s8812 | deepseek | 23 | DISAGREE | (no reason given) |
| s8812 | deepseek | 25 | DISAGREE | (no reason given) |
| s8812 | deepseek | 26 | DISAGREE | (no reason given) |
| s8812 | deepseek | s8812.clwb_complete | DISAGREE | (no reason given) |
| sa | deepseek | 12 | DISAGREE | No noncash charitable gift input is provided in this closed interface; entered as zero. |
| sa | deepseek | 9 | DISAGREE | The archived text only says attach Form 4952; the amount is taken from Form 4952 line 7 as the investment interest deduction. |
| sb | deepseek | 4 | DISAGREE | (no reason given) |
| sc | deepseek | 14 (sc.f7206_line14) | DISAGREE | (no reason given) |
| sc | deepseek | 28 | DISAGREE | (no reason given) |
| sc | deepseek | 29 | DISAGREE | (no reason given) |
| sc | deepseek | 30 | DISAGREE | (no reason given) |
| sc | deepseek | sc.cost179 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f14 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f17 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y10 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y15 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y15sl | DISAGREE | The supplied Form 4562 lines do not print a separate 15-year straight-line line. This helper totals asset entries whose MACRS period is y15sl and is not added again to Schedule C line 13 because line 19e already covers 15-year property. |
| sc | deepseek | sc.f19_y20 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y3 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y5 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f19_y7 | DISAGREE | (no reason given) |
| sc | deepseek | sc.f26h | DISAGREE | (no reason given) |
| sc | deepseek | sc.f6 | DISAGREE | (no reason given) |
| sc | deepseek | sc.mq_q4 | DISAGREE | (no reason given) |
| sc | deepseek | sc.mq_total | DISAGREE | (no reason given) |
| sc | deepseek | sc.rrta | DISAGREE | The supplied Schedule C text has no separate RRTA input for this business. The statutory-employee flag is the supplied flag that removes this business from Schedule SE, so it is used for this RRTA self-employment screening helper. |
| scveh | deepseek | 11 | DISAGREE | (no reason given) |
| scveh | deepseek | 15 | DISAGREE | (no reason given) |
| scveh | deepseek | 17 | DISAGREE | (no reason given) |
| scveh | deepseek | 18 | DISAGREE | (no reason given) |
| scveh | deepseek | 25 | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.bonus | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.s179_2025 | DISAGREE | (no reason given) |
| sd | deepseek | 11 | DISAGREE | (no reason given) |
| sd | deepseek | 12 | DISAGREE | (no reason given) |
| sd | deepseek | 21 | DISAGREE | (no reason given) |
| sd | deepseek | 4 | DISAGREE | (no reason given) |
| sd | deepseek | 5 | DISAGREE | (no reason given) |
| sd | deepseek | sd.line18 | DISAGREE | The 28% Rate Gain Worksheet is not supplied in the interface. The line is zero when no special sale makes the worksheet necessary; it refuses when line 17 is true and any sale is special. |
| sd | deepseek | sd.line19 | DISAGREE | (no reason given) |
| sd | deepseek | sd.net_gain | DISAGREE | (no reason given) |
| sdtw | deepseek | 30 | DISAGREE | (no reason given) |
| sdtw | deepseek | 33 | DISAGREE | (no reason given) |
| ssb | deepseek | 16 | DISAGREE | When married filing separately and the taxpayer lived with their spouse at any time in 2025, the line 8 instruction says to skip lines 8 through 15, multiply line 7 by 85%, and enter that on line 16. |
| ssb | deepseek | 6 | DISAGREE | The worksheet lists Schedule 1 lines 11 through 20, 23 and 25; unsupported Schedule 1 items are refused through scope.schedule1, so this sum uses the supported adjustment lines. |
| u1250 | deepseek | 10 | DISAGREE | (no reason given) |
| u1250 | deepseek | 12 | DISAGREE | (no reason given) |
| u1250 | deepseek | 13 | DISAGREE | (no reason given) |
| u1250 | deepseek | 14 | DISAGREE | Only Form 1099-DIV box 2d collectibles gain is represented; other components of the 28% Rate Gain Worksheet are outside this distribution-only path. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| asset | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 19(c) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 19(g) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 26(h) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 26(i) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.bonus_2025 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.cost179 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.dep_2025 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.dep_prior | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.mq_q4 | DISAGREE | DISAGREE | (no reason given) |
| carloan | deepseek | 22(ii) | DISAGREE | DISAGREE | (no reason given) |
| carloan | deepseek | 22(iii) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 2(c) | DISAGREE | DISAGREE | For a person who was age 13 at the end of 2025, whether any care was provided while over age 12 and disabled is read from dc_over12_care, except that a person who was 13 for all of 2025 is treated as over age 12 throughout; for older persons the age and incapacity facts determine the check. |
| dependent | deepseek | dependent.actc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.dc_count | DISAGREE | DISAGREE | Return-level count over the dependent collection; each dependent contributes one when dc_qp is true. |
| dependent | deepseek | dependent.dc_qp | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test1 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test2 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_person | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 5 | DISAGREE | DISAGREE | Line 5 is left blank when line 3 is below the threshold; modeled as zero, with line 6 then using line 2 per the instructions. |
| eic | deepseek | 6 (eic.line6) | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.check_27c | DISAGREE | DISAGREE | True when the computed EIC is zero, matching the STOP instructions that direct the filer to check line 27c. |
| eic | deepseek | eic.clergy | DISAGREE | DISAGREE | No separate clergy/church-employee line is provided; uses person.se_screen as the available screening proxy. |
| eic | deepseek | eic.credit | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.separated_box | DISAGREE | DISAGREE | Derived from the Step 3 separated-spouse questions and the qualifying-child US residence test. |
| f1040 | deepseek | 16 | DISAGREE | DISAGREE | Uses Schedule D Tax Worksheet when it applies, otherwise the Qualified Dividends and Capital Gain Tax Worksheet when it applies, otherwise the Tax Table/Tax Computation Worksheet; additional line 16 items are refused via scope.other_line16. |
| f1040 | deepseek | 1e | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 4a | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 4b | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 4c | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 5a | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 5b | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 5c | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 6c | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 1 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 2 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 30 | DISAGREE | DISAGREE | The supplied interface has no per-person allocation of line 28 benefits; this subtracts the total line 28 from the total line 2(d) expenses, floored at zero. |
| f2441 | deepseek | f2441.has_1e | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 12 | DISAGREE | DISAGREE | The IRS text says to enter the amount allocated to this business from the Summary. The supplied interface provides no separate allocation input; I take the existing per-business helper sc.s179_return as that allocated amount. |
| f4562 | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19a(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19b(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19c(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19d(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19e(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 19f(g) | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 21 | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| f4562 | deepseek | 26(h) | DISAGREE | DISAGREE | For a vehicle, column (h) is taken from the existing per-vehicle helper scveh.macrs, the vehicle MACRS depreciation allowed after the passenger-automobile limit. |
| f4562 | deepseek | 28 | DISAGREE | DISAGREE | No line 27 amount is supplied in this closed slice; line 28 sums the supplied line 25 and line 26(h) amounts. |
| f4562 | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| f4952 | deepseek | 4a | DISAGREE | DISAGREE | Computed as taxable interest plus ordinary dividends within the supported slice; other investment income is refused through f4952.unsupported. |
| f4952 | deepseek | 4d | DISAGREE | DISAGREE | Computed from the supported securities sales collection; capital gain distributions and capital loss carryovers are outside this interface and are covered by f4952.unsupported. |
| f4952 | deepseek | 4e | DISAGREE | DISAGREE | Net capital gain is computed from long-term sales over short-term losses in the supported securities sales collection. |
| f4952 | deepseek | f4952.required | DISAGREE | DISAGREE | Computed from the Who Must File exception: not required when line 4c is more than line 1, there is no carryover, and no unsupported other investment income or expense. |
| f5695 | deepseek | 14 | DISAGREE | DISAGREE | The limit worksheet also lists credits not present in the supplied interface (Schedule 3 lines 6l, 6d, 3, 6m, 6f, 6g, 6c, and 6h); they are omitted as outside this tool. Available worksheet credits are included. |
| f5695 | deepseek | 19c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 20d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 22d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 23d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 24d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 25e | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 29h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 32a | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 32b | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | f5695.claiming_part1 | DISAGREE | DISAGREE | The pages do not define a separate 'claiming Part I' result; chosen as line 15 being greater than zero (the residential clean energy credit actually claimed). |
| f8606 | deepseek | 1 | DISAGREE | DISAGREE | The IRS worksheet permits line 1 to be figured through the IRA Deduction Worksheet or the Pub. 590-A reduced-deduction worksheet; with no additional input interface, this slice takes line 1 as the supplied nondeductible contribution amount. |
| f8606 | deepseek | 2 | DISAGREE | DISAGREE | The IRS instructions allow line 2 to be adjusted for return of excess contributions, divorce transfers, and rollovers of nontaxable plan amounts; this closed slice takes line 2 as the supplied total basis. |
| f8606 | deepseek | 3 (question) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 6(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 6(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 9 | DISAGREE | DISAGREE | The printed over/but not over rate table is keyed by Form 1040 line 11a and filing status, as shown on the form. |
| f8889 | deepseek | 13 | DISAGREE | DISAGREE | Smaller of line 2 and line 12; zero is forced when line 2 is zero without needing line 12. |
| f8889 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 3 | DISAGREE | DISAGREE | Computes the line 3 limitation from the Line 3 Limitation Chart: monthly amounts by family/self-only coverage, with the last-month rule replacing the actual months with 12 months of December coverage, and the age-55 additional amount included on line 3 only when not married with family coverage (otherwise line 7). |
| f8889 | deepseek | 6 | DISAGREE | DISAGREE | Uses the Line 6 steps: share of the family-month limit plus the self-only-month limit when both spouses have HSAs and family coverage; otherwise line 5. |
| f8889 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.share_raw | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.split | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.step1 | DISAGREE | DISAGREE | (no reason given) |
| f8959 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| f8959 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| f8960 | deepseek | 1 | DISAGREE | DISAGREE | The excerpt does not restate line 1; the taxable-interest amount is read from Form 1040 line 2b and floored at zero to establish the declared nonnegative type. |
| f8960 | deepseek | 13 | DISAGREE | DISAGREE | With no section 911 exclusion and no CFC or PFIC adjustment in the supported slice, MAGI is AGI from Form 1040 line 11a. |
| f8960 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 4 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| f8995a | deepseek | 28 | DISAGREE | DISAGREE | Supported scope is section 199A dividends; PTP income or loss and prior carryforwards are refused by qbi.unsupported. |
| f8995a | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| f8995a | deepseek | 33 | DISAGREE | DISAGREE | Computed under the Form 8995 instructions for taxable income before the QBI deduction as Form 1040 line 11a minus lines 12e and 13b; floored at zero to match the declared NonNegDollars type. |
| f8995a | deepseek | 34 | DISAGREE | DISAGREE | Net capital gain is taken from Form 1040 line 7a when no Schedule D is filed (floored at zero), and from qdcg.schedule_d_net_gain when Schedule D is filed, per the Form 8995 instructions. |
| f8995a | deepseek | 40 | DISAGREE | DISAGREE | Line 29 is modeled as a positive carryforward loss, so the remaining carryforward is line 29 minus line 28, floored at zero. |
| ftc | deepseek | ftc.credit | DISAGREE | DISAGREE | The election instructions say to enter the smaller of total foreign tax or regular tax. The election conditions are all_passive, statements, eligible, elect, and taxes not more than the $300/$600 limit; when any fails the filer needs Form 1116, so this line refuses. |
| g28 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.all_eic_ssn | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.all_tin | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.ctc_ssn | DISAGREE | DISAGREE | Read as at least one spouse has an SSN valid for employment and each person on the return has an SSN or ITIN (or has applied for an ITIN). |
| household | deepseek | household.hoh_fails | DISAGREE | DISAGREE | Fails if not unmarried or considered unmarried, did not pay over half the home cost, or no dependent satisfies HOH Test 1 or Test 2. |
| household | deepseek | household.roster_bad | DISAGREE | DISAGREE | Treated as true when any dependent entry answers yes to divorced_rule, married, multiple_support, or other_claimant. |
| ira | deepseek | 11a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 11b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 12a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 12b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 1a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 1b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 2a | DISAGREE | DISAGREE | For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied. |
| ira | deepseek | 2b | DISAGREE | DISAGREE | For married filing separately living apart, the supplied ira.line2 parameter gives the married-filing-separately amount; no separate input for the line 20 checkbox is supplied. |
| ira | deepseek | 6a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 6b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 7a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 7b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 8 | DISAGREE | DISAGREE | Nontaxable combat pay is not represented in the supplied input interface; line 8 includes wages and alimony only. |
| ira | deepseek | ira.anyone_covered | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.both_kinds | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.combat_gate | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.cov_gate | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.excl_gate | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.kbh_short | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.line20 | DISAGREE | DISAGREE | If the filer elects to deduct a smaller amount and treat the rest as a nondeductible contribution, the smaller amount is not determined here; line 20 refuses via ira.deduct_less. |
| ira | deepseek | ira.over_comp | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.special_gate | DISAGREE | DISAGREE | (no reason given) |
| otjob | deepseek | 1(b) | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 1 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 6 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | eligible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned_b | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_has_box10 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.educator_deduction | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.eic_se | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_agreed | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_share | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_step1 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_8606_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_contrib | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_cov | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_deduction | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_dist_gate | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_files_8606 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line6 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line7 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_nondeductible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_se | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_ssb | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.s16 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_ineligible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line1 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sc_total | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line12 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line13 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line6 | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.deduction | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.taxable_before | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 3 | DISAGREE | DISAGREE | Blank Schedule D lines are not representable; if either line is supplied as a loss, the amount is zero. |
| qdcg | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 8 | DISAGREE | DISAGREE | The worksheet's note for married filing separately when the spouse itemized deductions is implemented by copying line 4 to line 8 and bypassing lines 5 through 7. |
| refund | deepseek | 9 | DISAGREE | DISAGREE | The STOP conditions on lines 3 and 8 are carried into zero through subtract_floor0 and the smaller of line 3 or line 8. |
| retirement | deepseek | (SMW 4) | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.amount_a | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.has_rollover | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.sav_amount | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 8c | DISAGREE | DISAGREE | (no reason given) |
| s179 | deepseek | 11 | DISAGREE | DISAGREE | (no reason given) |
| s179 | deepseek | s179.multi | DISAGREE | DISAGREE | Read as whether the line 12 allocation instruction for more than one business or activity applies. |
| s1a | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 12 | DISAGREE | DISAGREE | Line 11 is floor(line 10 / $1,000); line 12 is line 11 times $100, implemented as floor-to-$1,000 of positive excess times 1/10. |
| s1a | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 14a | DISAGREE | DISAGREE | Uses the person collection's overtime aggregate; Form W-2 box 1 qualification is represented by the s1a.overtime gate. |
| s1a | deepseek | 14b | DISAGREE | DISAGREE | Nonemployee qualified overtime is outside the closed input interface; entered as zero. |
| s1a | deepseek | 14c | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 18 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 20 | DISAGREE | DISAGREE | Line 19 is floor(line 18 / $1,000); line 20 is line 19 times $100, implemented as floor-to-$1,000 of positive excess times 1/10. |
| s1a | deepseek | 21 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 23 | DISAGREE | DISAGREE | Uses the carloan collection's column (iii) aggregate. |
| s1a | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 29 | DISAGREE | DISAGREE | Line 28 is ceil(line 27 / $1,000); line 29 is line 28 times $200, implemented as ceil-to-$1,000 of positive excess times 1/5. |
| s1a | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 31 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 32 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 33 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 34 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 35 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 36a | DISAGREE | DISAGREE | Assumes the taxpayer has a valid SSN and was born before January 2, 1961; the closed input interface does not supply these qualification facts. |
| s1a | deepseek | 36b | DISAGREE | DISAGREE | Spouse qualification facts are not supplied by the closed input interface; entered as zero. |
| s1a | deepseek | 4a | DISAGREE | DISAGREE | Uses the person collection's reported-tip aggregate; Form 4137 tips are outside the closed input interface. |
| s1a | deepseek | 4b | DISAGREE | DISAGREE | Form 4137 unreported tips are outside the closed input interface; entered as zero. |
| s1a | deepseek | 4c | DISAGREE | DISAGREE | Multiple-employer worksheet is represented by the person collection's total-tip aggregate. |
| s1a | deepseek | 5 | DISAGREE | DISAGREE | Trade-or-business qualified tips are outside the closed input interface; entered as zero. |
| s1a | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| s2 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5a | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 16b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 18a | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | s8812.clwb_14 | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | 16 | DISAGREE | DISAGREE | Only gambling losses are supported, limited to gambling winnings on Schedule 1 line 8b; other line 16 items are refused by sa.unsupported. |
| sa | deepseek | 5e | DISAGREE | DISAGREE | The worksheet's excluded-income lines 3a-3d are unavailable; sa.excluded_income true refuses. Otherwise line 4 is AGI. |
| sa | deepseek | sa.age65 | DISAGREE | DISAGREE | Counts person.age65 entries in the person collection; an MFS spouse covered only by sa.spouse_extra is not counted. |
| sa | deepseek | sa.deduction | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | sa.itemizes | DISAGREE | DISAGREE | (no reason given) |
| sales | deepseek | (e) | DISAGREE | DISAGREE | (no reason given) |
| sales | deepseek | (g) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 1(c) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 10 (sc.f7206_line10) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 12 (sc.s179_allowed) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 4 (sc.f7206_line4) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 4 (sc.ho_line4) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 5 (sc.ho_line5) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 7 (sc.f7206_line7) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 8 (sc.f7206_line8) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | 9 (sc.f7206_line9) | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.f25 | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.f28 | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.f29 | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.line31_pre179 | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.profit_pos | DISAGREE | DISAGREE | (no reason given) |
| sc | deepseek | sc.result | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | 13 | DISAGREE | DISAGREE | Business/investment-use percentage is figured from business, commuting and other miles and rounded to four decimal places where the IRS text does not state a rounding rule. |
| scveh | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | 19 | DISAGREE | DISAGREE | For a vehicle placed in service in 2019 the recovery period has ended; the provided inputs do not include prior-year MACRS amounts, so the unrecovered basis shown here is cost less prior section 179 only. |
| scveh | deepseek | 20a | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | 7 | DISAGREE | DISAGREE | The passenger automobile limit table is read with the placed-in-service year, the tax-year-in-service key (capped at 4th or later) and the bonus choice. |
| scveh | deepseek | 9 (scveh.line9) | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | 9 (scveh.line9w) | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.cost179 | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.macrs | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.mq_q4 | DISAGREE | DISAGREE | (no reason given) |
| scveh | deepseek | scveh.mq_total | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1a(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1a(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1a(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1a(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1b(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1b(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1b(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 1b(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 2(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 2(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 2(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 2(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 20 | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 3(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 3(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 3(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 3(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8a(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8a(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8a(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8a(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8b(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8b(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8b(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 8b(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 9(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 9(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 9(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 9(h) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | sd.filed | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | sd.to1040 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 23 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 28 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 31 | DISAGREE | DISAGREE | Returns zero when lines 1 and 16 are the same, because lines 23 through 43 are skipped. |
| sdtw | deepseek | 32 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 35 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 36 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 37 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 38 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 39 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 4 | DISAGREE | DISAGREE | The footnote's dotted-line smaller amount is not modeled; the expression copies Form 4952 line 4e. |
| sdtw | deepseek | 40 | DISAGREE | DISAGREE | Returns zero when lines 1 and 16 are the same, lines 1 and 32 are the same, or Schedule D line 19 is zero. |
| sdtw | deepseek | 41 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 42 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 43 | DISAGREE | DISAGREE | Returns zero when the worksheet skips lines 41 through 43. |
| se | deepseek | line13 | DISAGREE | DISAGREE | (no reason given) |
| sli | deepseek | 5 | DISAGREE | DISAGREE | The worksheet gives no line 5 amount for married filing separately because the deduction is not allowed for that status. Line 5 uses the non-MFJ amount for every status other than MFJ; sli.deduction returns zero when the filing status is MFS or the taxpayer is claimed as a dependent. |
| sli | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| sli | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| sli | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| sli | deepseek | sli.deduction | DISAGREE | DISAGREE | The printed line 9 is the worksheet result before the eligibility conditions. This result interface returns zero when the taxpayer (or spouse on a joint return) is claimed as a dependent or the filing status is married filing separately, because the IRS says the deduction can be taken only if those conditions are met. |
| ssb | deepseek | 10 | DISAGREE | DISAGREE | For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 10 is encoded as zero for that case. |
| ssb | deepseek | 18 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 8 | DISAGREE | DISAGREE | For married filing separately who lived with their spouse at any time in 2025, lines 8 through 15 are skipped; line 8 is encoded as zero for that case. |
| ssb | deepseek | ssb.has_benefits | DISAGREE | DISAGREE | (no reason given) |
| tax_on_amount | deepseek | tax | DISAGREE | DISAGREE | The Tax Table is used below ordinary.table_boundary ($100,000) and the Tax Computation Worksheet at or above that boundary. |
| tcw | deepseek | tax | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 18 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| w2 | deepseek | w2.sav_deferral | DISAGREE | DISAGREE | (no reason given) |

## Render comparison

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| asset | deepseek (deepseek-flash) | 15 | 11 | 73.3% | 0/15 (0.0%) | pending | 4 | 0 | 0 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pass | 0 | 1 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| dcprov | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 1/2 (50.0%) | pending | 0 | 2 | 0 | 0 |
| div | deepseek (deepseek-flash) | 22 | 22 | 100.0% | 0/22 (0.0%) | pass | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 58 | 54 | 93.1% | 0/58 (0.0%) | pass | 3 | 1 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 36 | 29 | 80.6% | 0/36 (0.0%) | pass | 2 | 5 | 0 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pass | 3 | 2 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 15 | 14 | 93.3% | 1/15 (6.7%) | pass | 0 | 1 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 72 | 71 | 98.6% | 0/72 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 1 | 0 | 1 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 18 | 85.7% | 0/21 (0.0%) | pending | 2 | 1 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 18 | 94.7% | 0/19 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 23 | 95.8% | 0/24 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 22 | 88.0% | 0/25 (0.0%) | pass | 1 | 2 | 0 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 13 | 81.2% | 0/16 (0.0%) | pending | 1 | 1 | 1 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 12 | 85.7% | 0/14 (0.0%) | pending | 1 | 0 | 1 | 0 |
| ftc | deepseek (deepseek-flash) | 11 | 8 | 72.7% | 0/11 (0.0%) | pass | 1 | 2 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 2 | 28.6% | 0/7 (0.0%) | pass | 1 | 4 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 5 | 4 | 80.0% | 0/5 (0.0%) | pending | 1 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 35 | 33 | 94.3% | 1/35 (2.9%) | pass | 0 | 1 | 1 | 0 |
| interest | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 21 | 16 | 76.2% | 0/21 (0.0%) | pending | 1 | 4 | 0 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 7 | 5 | 71.4% | 0/7 (0.0%) | pending | 0 | 2 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pass | 0 | 0 | 0 | 0 |
| person | deepseek (deepseek-flash) | 23 | 20 | 87.0% | 1/23 (4.3%) | pass | 3 | 0 | 0 | 0 |
| qbi | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 25 | 24 | 96.0% | 0/25 (0.0%) | pass | 0 | 0 | 1 | 0 |
| refund | deepseek (deepseek-flash) | 9 | 7 | 77.8% | 0/9 (0.0%) | pass | 0 | 2 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 10 | 6 | 60.0% | 0/10 (0.0%) | pass | 0 | 3 | 1 | 0 |
| s1 | deepseek (deepseek-flash) | 29 | 19 | 65.5% | 0/29 (0.0%) | pending | 6 | 4 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 13 | 11 | 84.6% | 1/13 (7.7%) | pass | 0 | 2 | 0 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 41 | 95.3% | 0/43 (0.0%) | pass | 1 | 1 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 8 | 6 | 75.0% | 0/8 (0.0%) | pending | 1 | 0 | 1 | 0 |
| s3 | deepseek (deepseek-flash) | 12 | 10 | 83.3% | 0/12 (0.0%) | pass | 1 | 1 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 31 | 28 | 90.3% | 0/31 (0.0%) | pass | 1 | 2 | 0 | 0 |
| sa | deepseek (deepseek-flash) | 24 | 21 | 87.5% | 0/24 (0.0%) | pending | 2 | 1 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 3 | 1 | 33.3% | 0/3 (0.0%) | pending | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 6 | 4 | 66.7% | 0/6 (0.0%) | pending | 1 | 1 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 75 | 68 | 90.7% | 0/75 (0.0%) | pending | 3 | 1 | 3 | 0 |
| scope | deepseek (deepseek-flash) | 5 | 0 | 0.0% | 0/5 (0.0%) | pending | 3 | 2 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 25 | 16 | 64.0% | 0/25 (0.0%) | pending | 2 | 4 | 3 | 0 |
| sd | deepseek (deepseek-flash) | 46 | 45 | 97.8% | 0/46 (0.0%) | pass | 1 | 0 | 0 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 46 | 97.9% | 0/47 (0.0%) | pass | 0 | 1 | 0 | 0 |
| se | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pending | 0 | 5 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 8 | 5 | 62.5% | 0/8 (0.0%) | pending | 1 | 2 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 18 | 17 | 94.4% | 0/18 (0.0%) | pass | 0 | 0 | 1 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 46 | 46 | 100.0% | 0/46 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 4 | 22.2% | 0/18 (0.0%) | pass | 0 | 13 | 1 | 0 |
| w2 | deepseek (deepseek-flash) | 17 | 17 | 100.0% | 0/17 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 1060 | 913 | 86.1% | | | 50 | 77 | 20 | 0 |

Pending asset [deepseek]: 4 open, unclassified or interface-gap rulings.
Pending dependent [deepseek]: model-error noise above 10%.
Pending f8606 [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending f8880 [deepseek]: 3 open, unclassified or interface-gap rulings.
Pending f8995 [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending f8995a [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending gift [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending ira [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending ltc [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending mq [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending oi8z [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending qbi [deepseek]: model-error noise above 10%.
Pending s1 [deepseek]: 10 open, unclassified or interface-gap rulings.
Pending s2 [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending sa [deepseek]: 3 open, unclassified or interface-gap rulings.
Pending sales [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending sb [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending sc [deepseek]: 4 open, unclassified or interface-gap rulings.
Pending scope [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending scveh [deepseek]: 6 open, unclassified or interface-gap rulings.
Pending se [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending sli [deepseek]: 3 open, unclassified or interface-gap rulings.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| asset | deepseek | (a) | MISMATCH | Column (a) asks for the classification, such as 3-year property, 5-year property, etc.; the restatement instead directs use of Pub. 946 Appendix B asset classes/class-life tables. |
| asset | deepseek | (b) | MISMATCH | Column (b) is month and year placed in service; the restatement captures only the year and limits it to 2005-2025. |
| asset | deepseek | (c) | MISMATCH | Column (c) requires subtracting allocable credits and deductions, including section 179 and the special allowance, after multiplying; the restatement stops at the multiplication. |
| asset | deepseek | 14 | MISMATCH | The IRS line also provides a 50% special allowance for qualified reuse and recycling property; the full/forty/none choices do not cover it and no refusal names it. |
| f1040 | deepseek | 1z | MISMATCH | The IRS line says 'Add lines 1a through 1h,' but the restatement adds only line 1a and line 1e. |
| f1040 | deepseek | 27c | MISMATCH | The IRS line says 'If you do not want to claim the EIC, check here,' but the restatement only handles instructed STOP cases and expressly does not ask the filer's own choice. |
| f1040 | deepseek | 28 (box) | MISMATCH | The IRS line provides 'If you do not want to claim the ACTC, check here,' but the restatement sets the box value to false unconditionally. |
| f2441 | deepseek | 12 | MISMATCH | The IRS line 12 includes amounts received under a dependent care assistance program from your sole proprietorship or partnership; person.dc_benefits sums only W-2 box 10 benefits less the box 1 part. |
| f2441 | deepseek | 22 | MISMATCH | The IRS line asks whether any amount on line 12 or 13 is from a sole proprietorship or partnership and says to enter the amount if Yes; the program unconditionally enters zero. |
| f4562 | deepseek | 25 | MISMATCH | The helper sums asset.bonus_2025 for listed property, but that asset helper uses line 14, which is expressly for property '(other than listed property)'; line 25 is the special allowance for qualified listed property used more than 50% in a qualified business use. |
| f4562 | deepseek | 28 | MISMATCH | The helper adds only line 25 and line 26(h). IRS line 28 says: 'Add amounts in column (h), lines 25 through 27,' so line 27 is omitted. |
| f4562 | deepseek | 29 | MISMATCH | The helper uses asset.s179_2025, which references line 6(c), but line 6 instructions say 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.' Line 29 is limited to column (i), line 26. |
| f8606 | deepseek | 1 | MISMATCH | The IRS line 1 instructions say to include repayments of qualified reservist distributions and to subtract worksheet line 12 "or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less"; the helper uses only worksheet line 12 and omits those items. |
| f8880 | deepseek | 1(b) | MISMATCH | The IRS says 'Complete column (b) only if you’re filing a joint return,' but the restatement sums spouse entries without conditioning column (b) on a joint return. |
| f8880 | deepseek | 2(b) | MISMATCH | The IRS says 'Complete column (b) only if you’re filing a joint return,' but the restatement sums spouse entries without conditioning column (b) on a joint return. |
| f8960 | deepseek | 9b | MISMATCH | IRS line 9b instructions say to include 'state, local, and foreign income taxes' and 'state, local, and foreign real property taxes'; the restatement's helper is limited to state/local income and property taxes and omits foreign income and foreign real property taxes not credited. |
| f8995 | deepseek | 11 | MISMATCH | IRS line 11 instructions compute 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b' and do not provide a zero floor; the restatement adds an 'If zero or less, enter -0-' condition. |
| f8995a | deepseek | 33 | MISMATCH | The restatement adds an 'if zero or less, enter -0-' floor, but the IRS instruction is only 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'; no zero floor is stated for line 33. |
| ftc | deepseek | taxes | UNCLEAR | The IRS text requires total creditable foreign taxes after reductions and lists Form 1099-INT and Form 1099-DIV as qualified payee statements, but it does not specify box 6 or box 7. |
| g28 | deepseek | 2 | MISMATCH | IRS line 2 requires the positive total of section 1202 exclusions from Form 8949 Part II code Q at 50%, 2/3, or 1/3; the restatement enters $0 from a distribution helper and does not compute those amounts, and its refusal covers only section 1202 distributions, not Code Q exclusions generally. |
| gift | deepseek | special | MISMATCH | IRS places only a qualified vehicle with a gross-proceeds acknowledgment, certain intellectual property, and inventory in Section A even over $5,000, and it requires Section B for partial or restricted interests only when the contribution is over $5,000; the restatement treats all vehicles, intellectual property, inventory, conservation or partial interests, and restricted-use property as special … |
| ira | deepseek | 2b | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ltc | deepseek | 2(a) | MISMATCH | The IRS note excludes payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under age 27 at the end of 2025; the restatement instead states the exclusion in terms of the covered person's eligibility for a plan subsidized by an employer. |
| oi8z | deepseek | 8z (amount) | MISMATCH | The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income. |
| person | deepseek | (screen) (person.ira_excess) | MISMATCH | Pub. 590-A defines an excess contribution by the $7,000/$8,000 or compensation limits and by failure to withdraw it; it does not make recharacterizing a 2025 contribution an excess contribution by itself. |
| person | deepseek | (screen) (person.sav_able) | MISMATCH | IRS Form 8880 line 4 includes only 'Certain distributions received after 2022 and before the due date' rather than any ABLE distribution; the restatement also combines that with the separate line 1 ABLE contribution question. |
| person | deepseek | Step 3 | MISMATCH | Pub. 560 Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; it does not provide the added 'If zero or less, enter -0-' floor. |
| s1 | deepseek | 15 | MISMATCH | The IRS says 'If you were self-employed and owe self-employment tax, fill in Schedule SE'; the restatement returns zero unless the person has at least one Schedule C, without refusing partnership or other self-employment income on that path. |
| s1 | deepseek | 16 | MISMATCH | The IRS line is 'Self-employed SEP, SIMPLE, and qualified plans'; the restatement computes only a 'Self-employed SEP or SIMPLE deduction' and returns zero when there is no Schedule C. |
| s1 | deepseek | 17 | MISMATCH | The IRS instructions allow the deduction for 'a partner with net earnings from self-employment' and a 'more-than-2% shareholder in an S corporation,' but the restatement only sums Schedule C (sc) Form 7206 line 14 amounts. |
| s1 | deepseek | 21 | MISMATCH | The IRS says 'Use Pub. 970 instead ... if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico'; the restatement has no such refusal and always uses worksheet line 9 for an eligible filer. |
| s1 | deepseek | 8f | MISMATCH | The IRS line 8f says 'Enter the total of the amounts from Form 8889, lines 16 and 20'; the restatement uses only Form 8889 line 16. |
| s1 | deepseek | 8j | MISMATCH | The restatement excludes 'the rental of personal property' from line 8j, but Pub. 525 says 'You must include on your return income from an activity, even if you don’t expect to make a profit'; line 8l covers only a for-profit rental not in the business. |
| s1a | deepseek | 23 | MISMATCH | Line 23 adds column (iii), but the program's column (iii) subtracts only Schedule C interest; IRS column (ii) is 'Deducted on Schedule C, Schedule E, or Schedule F.' |
| s2 | deepseek | 18 | MISMATCH | IRS line 18 says "Total additional taxes. Add lines 17a through 17z," but the restatement takes only line 17c and has no refusal excluding other 17a-17z amounts. |
| s3 | deepseek | 14 | MISMATCH | IRS line 14 says 'Add lines 13a through 13z'; the restatement instead takes a supplied subtotal and does not compute that addition. |
| s8812 | deepseek | 24 | MISMATCH | IRS line 24 distinguishes '1040-NR filers: Enter the amount from Schedule 3 (Form 1040), line 11'; the restatement always adds Form 1040 line 27a. |
| sa | deepseek | 5e | MISMATCH | IRS line 5e says if you completed Form 2555 or 4563, or excluded Puerto Rico income, see the SALT worksheet; that worksheet adds those excluded amounts to line 11b. The program's ceiling helper uses only Form 1040 line 11b and there is no excluded-income refusal on line 5e. |
| sa | deepseek | 9 | UNCLEAR | The provided Schedule A text only says 'Investment interest. Attach Form 4952 if required. See instructions'; the line 9 instructions, including how to figure investment interest when Form 4952 is not required, are not provided. |
| sb | deepseek | 7a | MISMATCH | The restatement covers only Line 7a—Question 1; the IRS also has 'Line 7a—Question 2' requiring a Yes box 'if you are required to file the form' (FinCEN Form 114). |
| sc | deepseek | 23 | MISMATCH | IRS line 23 includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'; the restatement omits the paid family and medical leave fund. |
| sc | deepseek | 4 (sc.f7206_line4) | MISMATCH | IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established'; the restatement uses only this business's net profit. |
| sc | deepseek | 5 (sc.f7206_line5) | MISMATCH | IRS line 5 says 'total of all net profits* from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income allocable to the profitable businesses'; the restatement uses only this person's Schedule C net profits. |
| scope | deepseek | other_income | UNCLEAR | The IRS text provided does not define the supported categories or the passive-activity and nonresident-alien return-treatment items, so the scope screen cannot be fully judged from the given text. |
| scope | deepseek | other_line16 | UNCLEAR | Form 1040 line 16 shows only checkboxes for Forms 8814 and 4972 plus a blank; the provided text does not include the line 16 instructions needed to verify the additional forms and education-credit recapture. |
| scope | deepseek | ready | UNCLEAR | This is a program scope gate rather than an IRS form line, and the provided text does not define the declared scope screens or the other gate conditions used by the helper. |
| scveh | deepseek | 7 | MISMATCH | IRS states 'The depreciation deduction, including the section 179 expense deduction and special depreciation allowance, for passenger automobiles is limited'; the restatement applies a published passenger-automobile limit unconditionally and has no refusal when scveh.passenger is false. |
| scveh | deepseek | 9 (scveh.line9) | MISMATCH | IRS says 'You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle'; the restatement allows actual whenever method is actual and only refuses standard under smr_bad. |
| sd | deepseek | 20 | MISMATCH | IRS line 17 says: 'No. Skip lines 18 through 21, and go to line 22.' The restatement computes line 20 even when line 17 is No; it should be skipped. |
| sli | deepseek | 6 | MISMATCH | The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| carloan | deepseek | 22(ii) | MISMATCH | MISMATCH | The IRS text says 'enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F),' but the restatement computes only the QPVLI part of Schedule C interest and omits other elsewhere-deducted QPVLI such as Schedule E or Schedule F. |
| dependent | deepseek | 2(c) | MISMATCH | MISMATCH | The IRS instruction says to check column (c) if the person 'was over age 12 at the time the care was provided and was disabled.' For a person over 13 at year-end the restatement does not use the care-time disabled helper; it only requires the separate 2025 incapacity input, so it can check the box even if the disability did not exist when the care was provided. |
| dependent | deepseek | 2(d) | MISMATCH | MISMATCH | Form 2441 column (d) says 'If you completed Part III, don't include in column (d) any benefits shown on line 28'; line 28 is lines 24 plus 25. The restatement instead says to include expenses paid with dependent care benefits and subtract only 'benefits you exclude,' so it can leave deductible benefits (line 24) in column (d). |
| f1040 | deepseek | Dependents (separated spouses) | MISMATCH | MISMATCH | The IRS checkbox is for MFS/HOH filers who lived apart for the last 6 months or are legally separated and lived apart at year end; the restatement instead uses an EIC Step 3/4 helper requiring EIC steps and a qualifying child. |
| f2441 | deepseek | 18 | MISMATCH | MISMATCH | Earned income for line 18 is determined as under lines 4 and 5 without line 12 benefits; person.dc_earned_b still omits Form 1040 line 1z and statutory employee Schedule C line 1 income. |
| f2441 | deepseek | 19 | MISMATCH | MISMATCH | The line uses the same earned-income helper as line 18, which omits Form 1040 line 1z and statutory employee Schedule C line 1 income; the IRS line 19 uses the lines 4/5 earned-income rules. |
| f2441 | deepseek | 4 | MISMATCH | MISMATCH | The IRS earned-income instructions include Form 1040 line 1z and, for a statutory employee, Schedule C line 1; person.dc_earned instead uses W-2 box 1, line 1e, and Schedule SE/Worksheet B, omitting those components. |
| f2441 | deepseek | 5 | MISMATCH | MISMATCH | For joint filers this uses spouse_earned, and otherwise line 4; the same person.dc_earned helper omits Form 1040 line 1z and statutory employee Schedule C line 1 earned income. |
| f2441 | deepseek | CLW 2 | MISMATCH | MISMATCH | The IRS worksheet line 2 says to enter Schedule 3 line 1 and line 6l (Form 8978, line 14); the program uses only Schedule 3 line 1. |
| f4562 | deepseek | 22 | MISMATCH | MISMATCH | The restatement omits lines 15 and 16, lines 19g through 19j, and line 20. IRS line 22 says: 'Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21.' |
| f4562 | deepseek | 26(h) | MISMATCH | MISMATCH | The helper uses asset.dep_listed, built from line 19(g) and line 17 MACRS; Part III says 'Don’t include listed property,' while line 26(h) is the Part V depreciation deduction for listed property used more than 50% in a qualified business use. |
| f4952 | deepseek | 4a | MISMATCH | MISMATCH | IRS line 4a includes ordinary dividends but 'except Alaska Permanent Fund dividends'; the restatement adds Schedule B ordinary dividends without that exception, so it can overstate line 4a. |
| f8880 | deepseek | (CLW 2) | MISMATCH | MISMATCH | The IRS Credit Limit Worksheet line 2 says 'Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l,' but the restatement adds only Schedule 3 lines 1 and 2, omitting line 3, 6d, and 6l. |
| f8960 | deepseek | 5a | MISMATCH | MISMATCH | IRS line 5a instructions say to combine 'Form 1040 or 1040-SR, line 7a, and Schedule 1 (Form 1040), line 4'; the restatement uses only f1040 line 7a. |
| f8960 | deepseek | 5b | MISMATCH | MISMATCH | The carryforward refusal is gated by f8960.carryforward_adj, which requires line 15 over $0; IRS says 'Starting in 2014, capital loss carryforwards must be adjusted if any sum of all capital gain or loss amounts excluded from NII on lines 5b and 5c was a net loss' with no MAGI-over-threshold condition. |
| f8995 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 instructions say if you're not required to file Schedule D, your net capital gain is the amount on Form 1040 line 7a; the restatement uses only the smaller of Schedule D lines 15 and 16. |
| ftc | deepseek | credit | MISMATCH | MISMATCH | The smaller-of rule is right, but the computation uses limited, which omits the Schedule 2 Part I line 1z addition and Form 4972 subtraction required for regular tax. |
| ftc | deepseek | limited | MISMATCH | MISMATCH | IRS line 20 regular tax is Form 1040 line 16 plus Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972; this uses only f1040 line 16. |
| g28 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 asks for "the total of all collectibles gain or (loss) from items you reported on Form 8949, Part II"; the restatement instead enters $0 from the distribution scope helper, and no refusal names Form 8949 Part II collectibles as excluded. |
| g28 | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 requires the total collectibles gain or (loss) from Form 4684 line 4 (if line 15 is more than zero), Form 6252, Form 6781 Part II, and Form 8824; the restatement is merely a $0 distribution-scope helper and no refusal names those forms as excluded. |
| g28 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is "the total of any collectibles gain reported to you on: Form 1099-DIV, box 2d; Form 2439, box 1d; and Schedule K-1"; the restatement uses only Form 1099-DIV box 2d and omits the other two sources without a refusal. |
| g28 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 says to enter long-term capital loss carryovers from "Schedule D, line 14; and Schedule K-1 (Form 1041), box 11, code D"; the restatement uses only Schedule D line 14 and does not refuse or account for the K-1 amount. |
| household | deepseek | test2_persons | UNCLEAR | MISMATCH | The restatement counts only confirmed dependent entries, but IRS Test 2 expressly includes 'Your unmarried qualifying child who isn’t your dependent' and other qualifying children who are not dependents. |
| ira | deepseek | 1a | MISMATCH | MISMATCH | IRS says if you weren't covered but your spouse was, you are considered covered unless you lived apart for all of 2025; cov_you counts only actual work or self-employed plan coverage, so the deemed-coverage case is omitted. |
| ira | deepseek | 2a | MISMATCH | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ira | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is the total of Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits lines 12, 14, and 23 and lists only selected lines. |
| ira | deepseek | 9 | UNCLEAR | MISMATCH | IRS line 9 includes earned income received 'as a self-employed individual or a partner'; person.ira_se is zero without a Schedule C, so partner or other self-employment income not on Schedule C is omitted, and the stated refusal covers only Schedule C income not from personal services. |
| mq | deepseek | q4 | MISMATCH | MISMATCH | The IRS test uses the total depreciable bases of MACRS property placed in service during the last 3 months, excluding nonresidential real property, residential rental property, railroad grading/tunnel bore, property placed in service and disposed of in the same year, and non-MACRS property; the helper merely adds person.mq_q4 and does not apply those exclusions or the personal-use basis reduction. |
| mq | deepseek | total | MISMATCH | MISMATCH | The IRS denominator is the total depreciable bases of all MACRS property placed in service during the entire year, with the same exclusions and personal-use reduction; the helper adds person.mq_total without those limitations. |
| qbi | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 is "Qualified business net (loss) carryforward from the prior year" shown with parentheses, and line 4 says "Combine lines 2 and 3," so the carryforward is a negative amount; the restatement instead says "entered as a positive amount." The line 3 instructions also require the "qualified portion" allowed in calculating taxable income in the current year, not merely prior-year line 16. |
| refund | deepseek | 1 | MISMATCH | MISMATCH | The min(refund, 2024 Schedule A line 5d) computation is right, but the IRS says to use Pub. 525 instead of this worksheet if the refund is for a tax year other than 2024 or if the last 2024 estimated state or local income tax payment was made in 2025; the refusal rules omit those exceptions. |
| refund | deepseek | 6 | UNCLEAR | MISMATCH | IRS line 6 says to multiply the number of boxes checked by $1,550 ($1,950 if the 2024 status was single or head of household), and for MFS the spouse boxes count only if the spouse had no income, isn’t filing, and can’t be claimed as a dependent; the restatement adds per-box amounts and omits the MFS conditions. |
| retirement | deepseek | (SMW 10) | MISMATCH | MISMATCH | IRS line 10 asks whether the annuity starting date was before 1987 and says Yes means STOP and do not complete the rest of the worksheet; the restatement unconditionally adds lines 6 and 8. |
| retirement | deepseek | (SMW 4) | MISMATCH | MISMATCH | The true branch matches, but for non-joint annuities the Table 1 helper uses only the after-November 18, 1996 numbers; IRS Table 1 separately provides a before-November 19, 1996 column (for example, 300 rather than 360 for age 55 or under). |
| retirement | deepseek | (SMW 8) | MISMATCH | MISMATCH | IRS line 5 says that if your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8; the restatement always computes the smaller of line 5 or line 7. |
| s1 | deepseek | 1 | MISMATCH | MISMATCH | The IRS Exception requires Pub. 525 instead of the worksheet in cases such as 'You owed alternative minimum tax in 2024' or 'You couldn’t use the full amount of credits...'; the restatement only refuses box 8 and not_2024. |
| s1 | deepseek | 10 | MISMATCH | MISMATCH | The IRS line says 'Combine lines 1 through 7 and 9'; the restatement adds only lines 1, 2a, 3, 7, and 9, omitting lines 4, 5, and 6. |
| s1 | deepseek | 25 | MISMATCH | MISMATCH | The IRS line says 'Total other adjustments. Add lines 24a through 24z'; the restatement enters only line 24a, omitting 24b through 24z. |
| s1 | deepseek | 26 | MISMATCH | MISMATCH | The IRS line says 'Add lines 11 through 23 and 25'; the restatement omits lines 12, 14, and 23, adding only a subset of that range. |
| s179 | deepseek | 1 | UNCLEAR | MISMATCH | Worksheet 1 says to "Enter the smaller of line 1 or line 2 here" and then "Enter the amount from line 3 here and on Form 4562, line 1"; the restatement enters only the $2,500,000 maximum. |
| s179 | deepseek | 13 | UNCLEAR | MISMATCH | The line 5 instructions say: "If line 5 is zero... enter the carryover of any disallowed deduction from 2024 ... on line 13." The restatement leaves line 10 out when line 5 is zero and then computes line 13 from lines 9 and 10 only, so it drops that carryover. |
| s1a | deepseek | 36b | MISMATCH | MISMATCH | IRS line 36b applies only 'If you are married filing jointly'; the restatement checks only that the spouse was born before January 2, 1961 and has a valid SSN. |
| s3 | deepseek | 1 | MISMATCH | MISMATCH | The helper uses f1040 line 16 alone as regular tax, but the IRS says regular tax is the total of Form 1040 line 16 and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972. |
| s8812 | deepseek | 18a | MISMATCH | MISMATCH | The Earned Income Chart says optional-method self-employment uses the Earned Income Worksheet 'even if you are also taking the EIC,' and the EIC rows add nontaxable combat pay not elected; the restatement instead routes taking-EIC filers to Worksheet B or Step 5 and does not add that combat pay. |
| s8812 | deepseek | 21 | MISMATCH | MISMATCH | The Additional Medicare Tax and RRTA Tax Worksheet says 'Add lines 6, 7, 11, and 15' for the line 21 amount; the restatement adds only lines 6 and 7 and has no RRTA refusal. |
| sa | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 says simply 'Enter amount from Form 1040 or 1040-SR, line 11b'; the program adds a 'but not less than zero' floor, which is not in the line text. |
| sales | deepseek | (e) | MISMATCH | MISMATCH | The restatement treats only A/D as 'Basis reported to IRS'; IRS column (e) says 'For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e),' and Box G/J transactions also have basis reported to the IRS, so G/J would wrongly use correct basis instead of reported basis. |
| sales | deepseek | (g) | MISMATCH | MISMATCH | The basis-correction helper is gated on 'Basis reported to IRS' being true only for A/D; for Box G/J with code B the IRS table says to 'enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect. Correct the error by entering an adjustment in column (g),' but the restatement would enter no basis correction. |
| sb | deepseek | 4 | UNCLEAR | UNCLEAR | The provided IRS instructions do not state line 4's text or computation; they mention lines 2 and 3 but not line 4. |
| sc | deepseek | 9 (sc.f7206_line9) | UNCLEAR | UNCLEAR | IRS line 9 says only to enter the Schedule 1 line 16 amount 'attributable to the same trade or business'; it does not state the line 4/line 5 allocation used here. |
| scope | deepseek | credits | UNCLEAR | UNCLEAR | The IRS text provided does not include Schedule 3 Part I or the credit instructions, so the Schedule 3 line references and the list of excluded credits cannot be verified. |
| scope | deepseek | schedule1 | UNCLEAR | UNCLEAR | The IRS text provided does not include Schedule 1 or its instructions, so the list of Schedule 1 income and adjustment items and the lines 12, 14, and 23 references cannot be verified. |
| scveh | deepseek | (b) | MISMATCH | MISMATCH | IRS column (b) says 'Date placed in service. Enter the date the property was placed in service' (including conversion date); the restatement asks only for the year. |
| scveh | deepseek | 19 | MISMATCH | MISMATCH | For a vehicle whose recovery period ended before 2025, IRS says 'enter your unrecovered basis, if any, in column (h)' and Pub. 946 allows unrecovered basis after the recovery period; the restatement forces zero for a 2019-placed vehicle. |
| scveh | deepseek | 20a | MISMATCH | MISMATCH | IRS line 20a says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement uses the gross business lease payments without the inclusion amount. |
| scveh | deepseek | 43 | MISMATCH | MISMATCH | IRS line 43 asks 'When did you place your vehicle in service for business purposes? (month/day/year)'; the restatement captures only the year, not the required date. |
| sdtw | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says to enter line 3 of the Foreign Earned Income Tax Worksheet instead when filing Form 2555; the restatement always uses Form 1040 line 15. |
| se | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 includes "Schedule K-1 (Form 1065), box 14, code A" and other income per instructions; restatement uses only this person Schedule C results. |
| se | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 says "Combine lines 1a, 1b, and 2"; restatement enters only the amount from line 2. |
| se | deepseek | 4b | MISMATCH | MISMATCH | IRS line 4b says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"; restatement always enters zero. |
| se | deepseek | 5b | MISMATCH | MISMATCH | IRS line 5b says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"; restatement always enters zero. |
| se | deepseek | 8d | MISMATCH | MISMATCH | IRS line 8d says "Add lines 8a, 8b, and 8c"; restatement enters only line 8a. |
| sli | deepseek | 3 | MISMATCH | MISMATCH | The IRS line says to total "Schedule 1, lines 11 through 20, and 23 and 25"; the restatement omits Schedule 1 line 23 (Archer MSA deduction). |
| sli | deepseek | 5 | MISMATCH | MISMATCH | The IRS says the deduction requires "any status except married filing separately" and line 5 lists only $85,000 for single/HOH/QSS and $170,000 for MFJ; assigning MFS $0 is not in the IRS text and does not exclude MFS. |
| u1250 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 requires the smaller of Form 4797 lines 22 or 24 for section 1250 property; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 10 | MISMATCH | MISMATCH | IRS line 10 requires gain from a sale or exchange of a partnership interest attributable to unrecaptured section 1250 gain; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 11 | MISMATCH | MISMATCH | IRS line 11 requires the total of unrecaptured section 1250 gain reported on Schedule K-1, Form 1099-DIV, or Form 2439, or in connection with Form 1099-R; the restatement uses only Form 1099-DIV box 2b. |
| u1250 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 requires total unrecaptured section 1250 gain from sales or other dispositions without a Form 4797 Part I entry; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 16 | MISMATCH | MISMATCH | IRS line 16 includes long-term capital loss carryovers from Schedule D, line 14 and Schedule K-1 (Form 1041), box 11, code D; the restatement uses only sd line 14. |
| u1250 | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 requires the amount from Form 4797, line 26g, for the property on line 1; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 requires subtracting line 2 from line 1; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 requires total unrecaptured section 1250 gain from Form(s) 6252 installment sales; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 requires Schedule K-1 unrecaptured section 1250 gain from a partnership or S corporation; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 6 | MISMATCH | MISMATCH | IRS line 6 requires adding lines 3 through 5; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 7 | MISMATCH | MISMATCH | IRS line 7 requires the smaller of line 6 or the gain from Form 4797, line 7; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 8 | MISMATCH | MISMATCH | IRS line 8 requires the amount, if any, from Form 4797, line 8; the restatement instead enters zero from div.screen. |
| u1250 | deepseek | 9 | MISMATCH | MISMATCH | IRS line 9 requires subtracting line 8 from line 7, with a zero floor; the restatement instead enters zero from div.screen. |

## Class M hand-work

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clcw | deepseek (deepseek-flash) | 31 | 31 | 100.0% | 0/34 (0.0%) | pass | 0 | 0 | 0 | 21 |
| clcw26 | deepseek (deepseek-flash) | 28 | 28 | 100.0% | 0/31 (0.0%) | pending | 0 | 0 | 0 | 24 |
| f2441 | deepseek (deepseek-flash) | 137 | 135 | 98.5% | 0/151 (0.0%) | pending | 0 | 0 | 2 | 67 |
| f4952 | deepseek (deepseek-flash) | 52 | 52 | 100.0% | 0/52 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 105 | 98 | 93.3% | 7/105 (6.7%) | pass | 7 | 0 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 50 | 50 | 100.0% | 0/50 (0.0%) | pass | 0 | 0 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pending | 0 | 0 | 0 | 11 |
| sd | deepseek (deepseek-flash) | 41 | 41 | 100.0% | 0/41 (0.0%) | pending | 0 | 0 | 0 | 97 |
| u1250 | deepseek (deepseek-flash) | 18 | 18 | 100.0% | 0/18 (0.0%) | pass | 0 | 0 | 0 | 18 |
| w2 | deepseek (deepseek-flash) | 39 | 39 | 100.0% | 0/39 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 504 | 495 | 98.2% | | | 7 | 0 | 2 | 238 |

Pending clcw26 [deepseek]: 5 missing expected lines.
Pending f2441 [deepseek]: 3 missing expected lines.
Pending g28 [deepseek]: 11 missing expected lines.
Pending sd [deepseek]: 32 missing expected lines.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| f8889 | deepseek | classm.f8889.2 — person[spouse].f8889[hsa].line12 | DISAGREE | model gave $1,844.00; work: line 8 $1,844.00 - line 11 $0 = $1,844.00 |
| f8889 | deepseek | classm.f8889.2 — person[spouse].f8889[hsa].line13 | DISAGREE | model gave $1,844.00; work: Smaller of line 2 $3,637.00 or line 12 $1,844.00 = $1,844.00 |
| f8889 | deepseek | classm.f8889.2 — person[spouse].f8889[hsa].line6 | DISAGREE | model gave $1,094.00; work: Allocated part of Step 1 family limit = $1,094.00 |
| f8889 | deepseek | classm.f8889.2 — person[spouse].f8889[hsa].line8 | DISAGREE | model gave $1,844.00; work: line 6 $1,094.00 + line 7 $750.00 = $1,844.00 |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line12 | DISAGREE | model gave $7,456.00; work: line 8 $7,456.00 - line 11 $0 = $7,456.00 |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line6 | DISAGREE | model gave $7,456.00; work: Allocated part of Step 1 family limit = $7,456.00 |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line8 | DISAGREE | model gave $7,456.00; work: line 6 $7,456.00 + line 7 $0 = $7,456.00 |

### Lines both families disputed

None.
