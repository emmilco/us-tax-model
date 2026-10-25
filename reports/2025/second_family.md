# Second-family review comparison — 2025

Summary: 112 form-kind pair(s) with logs from Claude and deepseek; ruled model-error noise 1.2% (25/2117 second-family lines judged; pending reviews are provisional); 23 eligible, 89 pending; raw agreement 67.9% (diagnostic only); current independence yield 186 line(s); both families disputed 412

Written by `tools/transcription/compare_families.py` on 2026-10-25 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

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
| asset | deepseek (deepseek-flash) | 16 | 1 | 6.2% | 0/16 (0.0%) | pending | 0 | 15 | 0 | 0 |
| carloan | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| dcprov | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pending | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 14 | 1 | 7.1% | 12/14 (85.7%) | pending | 1 | 11 | 1 | 0 |
| div | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 1 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 18 | 7 | 38.9% | 0/18 (0.0%) | pending | 1 | 10 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 50 | 32 | 64.0% | 0/50 (0.0%) | pending | 13 | 4 | 1 | 0 |
| f2441 | deepseek (deepseek-flash) | 37 | 21 | 56.8% | 5/37 (13.5%) | pending | 4 | 8 | 4 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 1 | 6.7% | 0/15 (0.0%) | pending | 0 | 14 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 15 | 12 | 80.0% | 2/15 (13.3%) | pending | 0 | 3 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 33 | 12 | 36.4% | 0/33 (0.0%) | pending | 8 | 12 | 1 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 2 | 40.0% | 0/5 (0.0%) | pending | 0 | 3 | 0 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 15 | 71.4% | 0/21 (0.0%) | pending | 0 | 6 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 7 | 36.8% | 0/19 (0.0%) | pending | 0 | 11 | 1 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 20 | 83.3% | 2/24 (8.3%) | pending | 4 | 0 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 18 | 72.0% | 0/25 (0.0%) | pending | 7 | 0 | 0 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 7 | 43.8% | 0/16 (0.0%) | pending | 4 | 5 | 0 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 10 | 71.4% | 0/14 (0.0%) | pending | 4 | 0 | 0 | 0 |
| ftc | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 1 | 0 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 1 | 14.3% | 0/7 (0.0%) | pending | 4 | 2 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 9 | 4 | 44.4% | 0/9 (0.0%) | pending | 1 | 4 | 0 | 0 |
| interest | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 22 | 6 | 27.3% | 0/22 (0.0%) | pending | 0 | 16 | 0 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 0 | 1 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 1 | 0 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pending | 0 | 0 | 0 | 0 |
| person | deepseek (deepseek-flash) | 74 | 31 | 41.9% | 0/74 (0.0%) | pending | 15 | 27 | 1 | 0 |
| qbi | deepseek (deepseek-flash) | 5 | 1 | 20.0% | 0/5 (0.0%) | pending | 2 | 2 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 26 | 25 | 96.2% | 0/26 (0.0%) | pending | 0 | 1 | 0 | 0 |
| refund | deepseek (deepseek-flash) | 11 | 3 | 27.3% | 0/11 (0.0%) | pending | 5 | 3 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 16 | 10 | 62.5% | 0/16 (0.0%) | pending | 2 | 4 | 0 | 0 |
| s1 | deepseek (deepseek-flash) | 26 | 14 | 53.8% | 0/26 (0.0%) | pending | 8 | 4 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 13 | 6 | 46.2% | 0/13 (0.0%) | pending | 4 | 3 | 0 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 10 | 23.3% | 0/43 (0.0%) | pending | 0 | 33 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 8 | 6 | 75.0% | 0/8 (0.0%) | pending | 1 | 1 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 8 | 4 | 50.0% | 0/8 (0.0%) | pending | 1 | 3 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 34 | 23 | 67.6% | 0/34 (0.0%) | pending | 3 | 7 | 1 | 0 |
| sa | deepseek (deepseek-flash) | 22 | 17 | 77.3% | 0/22 (0.0%) | pending | 1 | 3 | 1 | 0 |
| sales | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pending | 0 | 0 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 48 | 13 | 27.1% | 0/48 (0.0%) | pending | 19 | 15 | 1 | 7 |
| scope | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 21 | 2 | 9.5% | 0/21 (0.0%) | pending | 7 | 12 | 0 | 0 |
| sd | deepseek (deepseek-flash) | 54 | 13 | 24.1% | 0/54 (0.0%) | pending | 0 | 39 | 2 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 26 | 55.3% | 0/47 (0.0%) | pending | 3 | 17 | 1 | 0 |
| se | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 9 | 4 | 44.4% | 0/9 (0.0%) | pending | 0 | 5 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 19 | 12 | 63.2% | 0/19 (0.0%) | pending | 2 | 4 | 1 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 0 | 1 | 0 |
| tcw | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 1 | 33.3% | 0/3 (0.0%) | pending | 0 | 0 | 2 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 3 | 16.7% | 0/18 (0.0%) | pending | 1 | 14 | 0 | 0 |
| w2 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 0 | 1 | 1 | 0 |
| **all** | | 894 | 418 | 46.8% | | | 128 | 328 | 20 | 7 |

Pending asset [deepseek]: 15 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending carloan [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending dcprov [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close.
Pending dependent [deepseek]: model-error noise above 10%; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; no passing current expression type validation: deepseek.
Pending div [deepseek]: 1 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending eic [deepseek]: 11 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f1040 [deepseek]: 17 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f2441 [deepseek]: 4 open or unclassified rulings; model-error noise above 10%; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f4562 [deepseek]: 14 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f4952 [deepseek]: model-error noise above 10%; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f5695 [deepseek]: 20 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8606 [deepseek]: 3 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8880 [deepseek]: 6 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8889 [deepseek]: 11 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8959 [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8960 [deepseek]: 7 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8995 [deepseek]: 9 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8995a [deepseek]: 4 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ftc [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending g28 [deepseek]: 6 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending gift [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending household [deepseek]: 5 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending interest [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ira [deepseek]: 16 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ltc [deepseek]: 1 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending mq [deepseek]: model-error noise above 10%; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending oi8z [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending otjob [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending person [deepseek]: 42 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending qbi [deepseek]: 4 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending qdcg [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending refund [deepseek]: 8 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending retirement [deepseek]: 4 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s1 [deepseek]: 12 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s179 [deepseek]: 7 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s1a [deepseek]: 33 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s2 [deepseek]: 2 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s3 [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending s8812 [deepseek]: 10 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sa [deepseek]: 4 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sales [deepseek]: 2 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sb [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sc [deepseek]: 7 missing expected lines; 34 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending scope [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending scveh [deepseek]: 19 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sd [deepseek]: 39 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sdtw [deepseek]: 20 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending se [deepseek]: 1 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sli [deepseek]: 5 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ssb [deepseek]: 6 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tax_on_amount [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tcw [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tipjob [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending u1250 [deepseek]: 15 open or unclassified rulings; BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending w2 [deepseek]: BUG-0129: transcription qualification held until model IR type validation and prior-agreement audit close; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| dependent | deepseek | dependent.dc_count | DISAGREE | This is the total number of dependent entries that are qualifying persons for Form 2441, computed as a sum over the dependent collection. |
| div | deepseek | div.screen | DISAGREE | The IRS Form 1099-DIV pages do not define a 'screen' line. I read the project interface as the total of the supplied distribution components that require scope screening; box 3 is accepted only when div.basis_reconciled is true. |
| eic | deepseek | 6 (eic.wsb_6) | DISAGREE | (no reason given) |
| f1040 | deepseek | 1a | DISAGREE | (no reason given) |
| f1040 | deepseek | 25a | DISAGREE | (no reason given) |
| f1040 | deepseek | 29 | DISAGREE | Form 8863 is outside this slice; the line is zero unless the credit screening refuses. |
| f1040 | deepseek | 2a | DISAGREE | (no reason given) |
| f1040 | deepseek | 2b | DISAGREE | (no reason given) |
| f1040 | deepseek | 30 | DISAGREE | Form 8839 is outside this slice; the line is zero unless the credit screening refuses. |
| f1040 | deepseek | 3b | DISAGREE | (no reason given) |
| f1040 | deepseek | 4a | DISAGREE | (no reason given) |
| f1040 | deepseek | 4b | DISAGREE | (no reason given) |
| f1040 | deepseek | 4c | DISAGREE | (no reason given) |
| f1040 | deepseek | 5a | DISAGREE | (no reason given) |
| f1040 | deepseek | 5b | DISAGREE | (no reason given) |
| f1040 | deepseek | 5c | DISAGREE | (no reason given) |
| f2441 | deepseek | 12 | DISAGREE | (no reason given) |
| f2441 | deepseek | 21 | DISAGREE | The supplied interface does not distinguish MFS filers considered unmarried under the instructions; the $2,500 base is used for all married-filing-separately returns. |
| f2441 | deepseek | 25 | DISAGREE | (no reason given) |
| f2441 | deepseek | f2441.one_box10 | DISAGREE | The IRS pages do not define this project helper; interpreted as any positive Form W-2 box 10 amount summed over persons. |
| f5695 | deepseek | 19f | DISAGREE | (no reason given) |
| f5695 | deepseek | 20c | DISAGREE | (no reason given) |
| f5695 | deepseek | 22c | DISAGREE | (no reason given) |
| f5695 | deepseek | 23c | DISAGREE | (no reason given) |
| f5695 | deepseek | 24c | DISAGREE | (no reason given) |
| f5695 | deepseek | 29g | DISAGREE | (no reason given) |
| f5695 | deepseek | 5b | DISAGREE | (no reason given) |
| f5695 | deepseek | 6a | DISAGREE | (no reason given) |
| f8959 | deepseek | 1 | DISAGREE | (no reason given) |
| f8959 | deepseek | 15 | DISAGREE | (no reason given) |
| f8959 | deepseek | 19 | DISAGREE | The input interface has no separate Form W-2 box 12 code B or N amounts; this line is the total of box 6 only. |
| f8959 | deepseek | 9 | DISAGREE | (no reason given) |
| f8960 | deepseek | 1 | DISAGREE | (no reason given) |
| f8960 | deepseek | 10 | DISAGREE | (no reason given) |
| f8960 | deepseek | 2 | DISAGREE | (no reason given) |
| f8960 | deepseek | 4c | DISAGREE | Line 4b is typed non-negative; this treats it as an amount subtracted from line 4a. |
| f8960 | deepseek | 5d | DISAGREE | Lines 5b and 5c are typed non-negative; this treats them as amounts not subject to NIIT and subtracts them from line 5a. |
| f8960 | deepseek | 9a | DISAGREE | (no reason given) |
| f8960 | deepseek | 9b | DISAGREE | Uses the supplied allocated state and local income and property taxes; foreign income taxes not claimed as a credit are not separately supplied. |
| f8995 | deepseek | 11 | DISAGREE | Computed per the instructions as Form 1040 line 11a minus lines 12e and 13b; floored at zero because the line is NonNegDollars. |
| f8995 | deepseek | 12 | DISAGREE | Net capital gain is Form 1040 line 7a if no Schedule D, otherwise the smaller of Schedule D lines 15 and 16; it is floored at zero when zero or less, as the Schedule D instruction states and as the NonNegDollars type requires. |
| f8995 | deepseek | 2 | DISAGREE | The tool supports QBI from the Schedule C businesses entered; other QBI and PTP items are refused via qbi.unsupported. |
| f8995 | deepseek | 6 | DISAGREE | The tool supports only qualified section 199A dividends; PTP income or loss is refused via qbi.unsupported. |
| f8995a | deepseek | 28 | DISAGREE | Supported case uses qualified section 199A dividends from Form 1099-DIV box 5; PTP income/loss is refused by qbi.unsupported. |
| f8995a | deepseek | 30 | DISAGREE | (no reason given) |
| f8995a | deepseek | 33 | DISAGREE | Computed as Form 1040 line 11a minus lines 12e and 13b, floored at zero to keep the NonNegDollars type. |
| f8995a | deepseek | 34 | DISAGREE | (no reason given) |
| ftc | deepseek | ftc.credit | DISAGREE | (no reason given) |
| g28 | deepseek | 1 | DISAGREE | The IRS line can be a collectibles gain or loss, but the declared type is NonNegDollars. In this distribution-only path, Form 8949 collectibles items are outside the computed scope; any such item is refused via sales.special, and the computed value is zero. |
| g28 | deepseek | 2 | DISAGREE | (no reason given) |
| g28 | deepseek | 3 | DISAGREE | (no reason given) |
| g28 | deepseek | 6 | DISAGREE | (no reason given) |
| household | deepseek | household.taxpayer_work_ssn | DISAGREE | (no reason given) |
| mq | deepseek | mq.applies | DISAGREE | The archived text does not say whether separate Schedule C businesses or spouses on a joint return are tested separately; this line aggregates the person entries on the return for one test. |
| person | deepseek | Step 1 | DISAGREE | (no reason given) |
| person | deepseek | Step 3 | DISAGREE | (no reason given) |
| person | deepseek | Step 5 | DISAGREE | Assumes no elective deferrals or catch-up contributions to the self-employed plan, because the closed input interface supplies none; only the skip-steps-9-through-20 branch is encoded. |
| person | deepseek | eligible | DISAGREE | (no reason given) |
| person | deepseek | person.dc_has_box10 | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_agreed | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_step1 | DISAGREE | (no reason given) |
| person | deepseek | person.income179 | DISAGREE | (no reason given) |
| person | deepseek | person.qbi | DISAGREE | (no reason given) |
| person | deepseek | person.s179_listed | DISAGREE | The available Schedule C summary field cost179_v is read as the listed-property (vehicle) total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface. |
| person | deepseek | person.s179_nonlisted | DISAGREE | The available Schedule C summary field cost179_a is read as the nonlisted-property total; the detailed listed-property flag is not separately aggregated at the person level in the supplied interface. |
| person | deepseek | person.sc_1a | DISAGREE | (no reason given) |
| person | deepseek | person.sc_total | DISAGREE | (no reason given) |
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
| s1 | deepseek | 13 | DISAGREE | (no reason given) |
| s1 | deepseek | 16 | DISAGREE | (no reason given) |
| s1 | deepseek | 17 | DISAGREE | (no reason given) |
| s1 | deepseek | 19a | DISAGREE | (no reason given) |
| s1 | deepseek | 2a | DISAGREE | (no reason given) |
| s1 | deepseek | 3 | DISAGREE | (no reason given) |
| s1 | deepseek | 8f | DISAGREE | The archived Schedule 1 text refers to Form 8889 lines 16 and 20; the provided Form 8889 interface has no line 20, so this transcription uses line 16 only. |
| s1 | deepseek | s1.has_sc | DISAGREE | (no reason given) |
| s179 | deepseek | 11 | DISAGREE | (no reason given) |
| s179 | deepseek | 6(c) | DISAGREE | (no reason given) |
| s179 | deepseek | 7 | DISAGREE | (no reason given) |
| s179 | deepseek | s179.differs | DISAGREE | The supplied IRS text does not define a Boolean named differs; this reads it as whether the business income limitation reduced line 12 below the sum of lines 9 and 10 (equivalently, whether a carryover remains on line 13). |
| s2 | deepseek | 11 | DISAGREE | (no reason given) |
| s3 | deepseek | 8 | DISAGREE | Lines 3 and 7 are not in the closed input interface. They are represented as zero helpers, and line 8 refuses under scope.credits when any other credit is claimed. The sum is floored at zero only to give the declared NonNegDollars result for a credit total. |
| s8812 | deepseek | 13 | DISAGREE | (no reason given) |
| s8812 | deepseek | 22 | DISAGREE | Schedule 2 lines 5, 6 and 13 are represented by Form 8959 line 24, Form 8960 line 17, and the person HSA additional tax. |
| s8812 | deepseek | s8812.clwb_complete | DISAGREE | The printed condition also includes credits other than Form 5695 Part I; those are screened by scope.credits. The Form 2555 condition is approximated by sa.excluded_income, the only provided gate, which also covers Form 4563 and Puerto Rico. |
| sa | deepseek | 2 | DISAGREE | (no reason given) |
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
| sdtw | deepseek | 30 | DISAGREE | (no reason given) |
| sdtw | deepseek | 33 | DISAGREE | (no reason given) |
| sdtw | deepseek | 39 | DISAGREE | (no reason given) |
| ssb | deepseek | 16 | DISAGREE | When married filing separately and the taxpayer lived with their spouse at any time in 2025, the line 8 instruction says to skip lines 8 through 15, multiply line 7 by 85%, and enter that on line 16. |
| ssb | deepseek | 6 | DISAGREE | The worksheet lists Schedule 1 lines 11 through 20, 23 and 25; unsupported Schedule 1 items are refused through scope.schedule1, so this sum uses the supported adjustment lines. |
| u1250 | deepseek | 14 | DISAGREE | The 28% Rate Gain Worksheet is not in the supplied closed interface; the distribution-only path takes line 14 as zero. Section 1202 or collectibles amounts would be outside this slice. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| asset | deepseek | (c) | DISAGREE | DISAGREE | Business basis is cost times business-use percentage, rounded to the cent. |
| asset | deepseek | (d) | DISAGREE | DISAGREE | The archived pages identify the recovery period through Pub. 946 Appendix B; the complete class-to-period table is not reproduced here, so the pinned table asset_class_period is used. |
| asset | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 19(c) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 19(g) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | 26(h) | DISAGREE | DISAGREE | Only line 26 (listed property used more than 50% in qualified business use) is computed; line 27 for 50% or less is outside this slice. |
| asset | deepseek | 26(i) | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.bonus_2025 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.cost179 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.dep_2025 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.dep_prior | DISAGREE | DISAGREE | The archived pages do not provide an accumulated prior-year depreciation figure for a single asset; this helper is the line 17 current-year amount for prior-year non-listed property. |
| asset | deepseek | asset.mq_q4 | DISAGREE | DISAGREE | (no reason given) |
| asset | deepseek | asset.s179_2025 | DISAGREE | DISAGREE | (no reason given) |
| carloan | deepseek | 22(iii) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 2(c) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.actc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.dc_qp | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_ssn_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test1 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test2 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_person | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 4b | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 6 (eic.line6) | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.check_27c | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.clergy | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.credit | DISAGREE | DISAGREE | Step 2 tests not represented by the closed interface beyond investment income and Form 2555/excluded income are not separately screened here. |
| eic | deepseek | eic.self_employed | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.separated_box | DISAGREE | DISAGREE | Reading: true only for a non-joint MFS/HOH filer who lived apart or is legally separated and is not a qualifying child of another. |
| f1040 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 1e | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 27c | DISAGREE | DISAGREE | No closed-interface input exists for the EIC opt-out election; the tool assumes the box is not checked. |
| f1040 | deepseek | 6c | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 1 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 2 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
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
| f4952 | deepseek | 4a | DISAGREE | DISAGREE | The archived instructions list interest and ordinary dividends as gross investment income but do not name a source line. The transcription uses supported taxable interest from the interest collection plus ordinary dividends (f1040.line3b). The instructions also mention annuities and royalties, but the closed interface supplies no such inputs. |
| f4952 | deepseek | 4d | DISAGREE | DISAGREE | The instructions define this as the excess of total gains over total losses from disposition and say to include capital gain distributions and capital loss carryovers, but do not name a source line. The transcription uses Schedule D's positive net gain, sd.net_gain. |
| f4952 | deepseek | f4952.required | DISAGREE | DISAGREE | Under the supported slice, no other deductible investment expenses are present. The exception applies when line 4c exceeds line 1 and there is no carryover; otherwise the form is required. |
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
| f8889 | deepseek | 13 | DISAGREE | DISAGREE | Prior-year excess contributions are not supplied by the interface; this line follows the general rule, the smaller of line 2 and line 12. |
| f8889 | deepseek | 14b | DISAGREE | DISAGREE | The interface supplies the rollover part only; excess contributions withdrawn by the due date are not separately supplied, so line 14b is limited to the rollover amount. |
| f8889 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 17b | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 3 | DISAGREE | DISAGREE | Line 3 uses the Line 3 Limitation Chart: monthly amounts are $4,300 self-only and $8,550 family, increased to $5,300 and $9,550 when the age-55 additional amount belongs on line 3; the total is divided by 12. |
| f8889 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.share_raw | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.split | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.step1 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 4 | DISAGREE | DISAGREE | (no reason given) |
| f8995 | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| g28 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| g28 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.all_eic_ssn | DISAGREE | DISAGREE | Compared the count of persons whose eic_ssn is false to zero. |
| household | deepseek | household.all_tin | DISAGREE | DISAGREE | Compared the count of persons with neither tin nor itin_applied to zero. |
| household | deepseek | household.ctc_ssn | DISAGREE | DISAGREE | At least one person has an SSN valid for employment, and everyone has an SSN/ITIN or has applied. |
| household | deepseek | household.hsa_both | DISAGREE | DISAGREE | Read i8889: If both you and your spouse have HSAs; counted persons with at least one HSA/Form 8889 entry. |
| ira | deepseek | 11a | DISAGREE | DISAGREE | Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A. |
| ira | deepseek | 11b | DISAGREE | DISAGREE | Refuses when the KBH spousal IRA limit applies because the text directs to Pub. 590-A. |
| ira | deepseek | 12a | DISAGREE | DISAGREE | Refuses when the filer wants to deduct a smaller amount (ira.deduct_less). |
| ira | deepseek | 12b | DISAGREE | DISAGREE | Refuses when the filer wants to deduct a smaller amount (ira.deduct_less). |
| ira | deepseek | 1a | DISAGREE | DISAGREE | Taxpayer retirement plan coverage is taken from person.ira_work_plan; the closed input interface does not provide a separate line for it. |
| ira | deepseek | 1b | DISAGREE | DISAGREE | Spouse retirement plan coverage is not provided by the closed input interface; treated as false. This understates deductions when a spouse is covered on a joint return. |
| ira | deepseek | 2a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 2b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 6a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 6b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 7a | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 7b | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | 8 | DISAGREE | DISAGREE | Nontaxable combat pay is not in the closed interface; omitted. Refuses when ira.special is true because nonqualified deferred compensation cannot be excluded. |
| ira | deepseek | 9 | DISAGREE | DISAGREE | Self-employment earned income is taken from person.ira_se; refuses when ira.se_capital is true because only material-income-producing-factor businesses are supported. |
| ira | deepseek | ira.anyone_covered | DISAGREE | DISAGREE | (no reason given) |
| ira | deepseek | ira.line20 | DISAGREE | DISAGREE | (no reason given) |
| ltc | deepseek | 2(b) | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 6 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned_b | DISAGREE | DISAGREE | The supplied interface has one earned-income figure per person; this helper repeats it for the form's second earned-income column. |
| person | deepseek | person.educator_deduction | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.eic_se | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_share | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_8606_line14 | DISAGREE | DISAGREE | (no reason given) |
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
| person | deepseek | person.ira_se | DISAGREE | DISAGREE | The archived text does not give a separate self-employment IRA figure beyond the deduction worksheet; the line repeats the computed IRA deduction. |
| person | deepseek | person.ira_ssb | DISAGREE | DISAGREE | The archived text sends this figure to Pub. 590-A worksheets not included here; the line repeats the computed IRA deduction as the available reading. |
| person | deepseek | person.s16 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_ineligible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line1 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line12 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line13 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line6 | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.deduction | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.taxable_before | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 3 | DISAGREE | DISAGREE | A blank Schedule D line 15 or 16 is treated as zero, as the tool's Schedule D supplies a computed amount on each; a loss, or a smaller-of result below zero, is floored at zero on the helper line. |
| refund | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 8 | DISAGREE | DISAGREE | The worksheet's note for married filing separately when the spouse itemized deductions is implemented by copying line 4 to line 8 and bypassing lines 5 through 7. |
| refund | deepseek | 9 | DISAGREE | DISAGREE | The STOP conditions on lines 3 and 8 are carried into zero through subtract_floor0 and the smaller of line 3 or line 8. |
| retirement | deepseek | (SMW 4) | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.amount_a | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.has_rollover | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.sav_amount | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | 8c | DISAGREE | DISAGREE | (no reason given) |
| s1 | deepseek | s1.has_gambling | DISAGREE | DISAGREE | (no reason given) |
| s179 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| s179 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| s179 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 12 | DISAGREE | DISAGREE | Line 11 is the floor of line 10 divided by $1,000; the helper computes the same amount as line 12. |
| s1a | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 14a | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 14b | DISAGREE | DISAGREE | The supplied interface provides no payor-level 1099 overtime amount; this slice treats line 14b as zero. |
| s1a | deepseek | 14c | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 18 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 20 | DISAGREE | DISAGREE | Line 19 is the floor of line 18 divided by $1,000; the helper computes line 20 directly. |
| s1a | deepseek | 21 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 29 | DISAGREE | DISAGREE | Line 28 is line 27 divided by $1,000 rounded up to the next higher whole number; the helper computes line 29 directly. |
| s1a | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 31 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 32 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 33 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 34 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 35 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 36a | DISAGREE | DISAGREE | The supplied interface does not provide a scalar taxpayer selector; this reads the person entry whose role is taxpayer. |
| s1a | deepseek | 36b | DISAGREE | DISAGREE | The supplied interface does not provide a scalar spouse selector; this reads the person entry whose role is spouse. |
| s1a | deepseek | 4a | DISAGREE | DISAGREE | Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c. |
| s1a | deepseek | 4b | DISAGREE | DISAGREE | Reads the single tipjob entry when there is exactly one employer; multiple-employer amounts are handled through line 4c. |
| s1a | deepseek | 4c | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 5 | DISAGREE | DISAGREE | The supplied interface does not provide nonemployee trade-or-business tip amounts; this slice treats line 5 as zero. |
| s1a | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| s1a | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| s2 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5a | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 16b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 18a | DISAGREE | DISAGREE | Uses the tool's EIC earned-income line. The IRS chart's alternative computation routes are not separately provided; combat pay is refused because only a yes/no is supplied. |
| s8812 | deepseek | 21 | DISAGREE | DISAGREE | The Additional Medicare and RRTA worksheet is represented only through Form 8959 lines; RRTA is refused. |
| s8812 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | s8812.clwb_14 | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | 16 | DISAGREE | DISAGREE | Supported case is gambling losses limited to gambling winnings; other line 16 items are refused. |
| sa | deepseek | sa.deduction | DISAGREE | DISAGREE | Standard deduction for dependents or dual-status aliens is outside this slice, so sa.dependent is refused. |
| sa | deepseek | sa.itemizes | DISAGREE | DISAGREE | Uses the larger of itemized and standard, or itemized if the election is made; dependent or dual-status standard deduction is refused. |
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
| sd | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
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
| sd | deepseek | sd.filed | DISAGREE | DISAGREE | The archived pages do not define a separate filed flag; chosen reading: true when any Schedule D amount or carryover/other-form input is present. A return with transactions that net to zero in every total is not distinguished. |
| sd | deepseek | sd.line18 | DISAGREE | DISAGREE | The 28% Rate Gain Worksheet's section 1202 exclusion and other-form amounts are outside this slice; line 18 is computed only from Form 1099-DIV box 2d reduced by a Schedule D line 7 loss, and refuses the listed screening inputs otherwise. |
| sd | deepseek | sd.line19 | DISAGREE | DISAGREE | The Unrecaptured Section 1250 Gain Worksheet is not fully reproduced in the archived text; chosen reading: with no other-form or special-sale source, line 19 is Form 1099-DIV box 2b. |
| sd | deepseek | sd.net_gain | DISAGREE | DISAGREE | Chosen reading: the smaller of Schedule D lines 15 and 16 when both are gains, otherwise zero, as in the Qualified Dividends and Capital Gain Tax Worksheet line 3. |
| sd | deepseek | sd.to1040 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 23 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 24 | DISAGREE | DISAGREE | Line 22 is computed by this model, so the blank alternative is not used. |
| sdtw | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 28 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 32 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 34 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 35 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 36 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 37 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 38 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 40 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 41 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 42 | DISAGREE | DISAGREE | (no reason given) |
| sdtw | deepseek | 43 | DISAGREE | DISAGREE | (no reason given) |
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
| tcw | deepseek | tax | DISAGREE | DISAGREE | Section B applies to married filing jointly or qualifying surviving spouse, so a qss filing status uses the mfj rows. |
| u1250 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 4 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| w2 | deepseek | w2.sav_deferral | DISAGREE | DISAGREE | (no reason given) |

## Render comparison

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| asset | deepseek (deepseek-flash) | 15 | 11 | 73.3% | 0/15 (0.0%) | pending | 4 | 0 | 0 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 0/2 (0.0%) | pass | 0 | 2 | 0 | 0 |
| dcprov | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 0/2 (0.0%) | pass | 0 | 1 | 1 | 0 |
| div | deepseek (deepseek-flash) | 22 | 19 | 86.4% | 1/22 (4.5%) | pass | 3 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 57 | 49 | 86.0% | 0/57 (0.0%) | pending | 1 | 1 | 6 | 0 |
| f2441 | deepseek (deepseek-flash) | 36 | 29 | 80.6% | 2/36 (5.6%) | pass | 2 | 5 | 0 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pass | 3 | 2 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 15 | 13 | 86.7% | 0/15 (0.0%) | pass | 0 | 2 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 72 | 71 | 98.6% | 0/72 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 1 | 0 | 1 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 18 | 85.7% | 0/21 (0.0%) | pending | 2 | 1 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 18 | 94.7% | 0/19 (0.0%) | pass | 0 | 1 | 0 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 23 | 95.8% | 0/24 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 23 | 92.0% | 0/25 (0.0%) | pending | 0 | 2 | 0 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 13 | 81.2% | 0/16 (0.0%) | pending | 1 | 1 | 1 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 12 | 85.7% | 0/14 (0.0%) | pending | 1 | 0 | 1 | 0 |
| ftc | deepseek (deepseek-flash) | 11 | 8 | 72.7% | 0/11 (0.0%) | pass | 1 | 2 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 2 | 28.6% | 0/7 (0.0%) | pending | 0 | 5 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 5 | 4 | 80.0% | 0/5 (0.0%) | pending | 1 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 35 | 31 | 88.6% | 0/35 (0.0%) | pending | 4 | 0 | 0 | 0 |
| interest | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 21 | 16 | 76.2% | 0/21 (0.0%) | pending | 1 | 4 | 0 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 7 | 5 | 71.4% | 0/7 (0.0%) | pending | 0 | 2 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pass | 0 | 0 | 0 | 0 |
| person | deepseek (deepseek-flash) | 23 | 19 | 82.6% | 0/23 (0.0%) | pending | 2 | 1 | 1 | 0 |
| qbi | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 25 | 22 | 88.0% | 0/25 (0.0%) | pending | 0 | 2 | 1 | 0 |
| refund | deepseek (deepseek-flash) | 9 | 7 | 77.8% | 0/9 (0.0%) | pending | 0 | 2 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 10 | 3 | 30.0% | 0/10 (0.0%) | pass | 2 | 5 | 0 | 0 |
| s1 | deepseek (deepseek-flash) | 29 | 19 | 65.5% | 0/29 (0.0%) | pending | 6 | 4 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 13 | 10 | 76.9% | 0/13 (0.0%) | pending | 2 | 1 | 0 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 42 | 97.7% | 0/43 (0.0%) | pending | 0 | 1 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 8 | 6 | 75.0% | 0/8 (0.0%) | pending | 1 | 0 | 1 | 0 |
| s3 | deepseek (deepseek-flash) | 12 | 10 | 83.3% | 0/12 (0.0%) | pass | 1 | 1 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 31 | 25 | 80.6% | 0/31 (0.0%) | pending | 2 | 2 | 2 | 0 |
| sa | deepseek (deepseek-flash) | 24 | 21 | 87.5% | 0/24 (0.0%) | pending | 2 | 1 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 3 | 1 | 33.3% | 0/3 (0.0%) | pending | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 6 | 4 | 66.7% | 0/6 (0.0%) | pending | 1 | 1 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 75 | 68 | 90.7% | 0/75 (0.0%) | pending | 3 | 1 | 3 | 0 |
| scope | deepseek (deepseek-flash) | 5 | 0 | 0.0% | 0/5 (0.0%) | pending | 3 | 2 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 25 | 16 | 64.0% | 0/25 (0.0%) | pending | 2 | 4 | 3 | 0 |
| sd | deepseek (deepseek-flash) | 46 | 14 | 30.4% | 0/46 (0.0%) | pass | 0 | 0 | 32 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 42 | 89.4% | 0/47 (0.0%) | pending | 3 | 2 | 0 | 0 |
| se | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pending | 0 | 5 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 8 | 5 | 62.5% | 0/8 (0.0%) | pending | 1 | 2 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 18 | 17 | 94.4% | 0/18 (0.0%) | pass | 0 | 0 | 1 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 46 | 46 | 100.0% | 0/46 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 5 | 27.8% | 0/18 (0.0%) | pending | 0 | 13 | 0 | 0 |
| w2 | deepseek (deepseek-flash) | 17 | 17 | 100.0% | 0/17 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 1033 | 835 | 80.8% | | | 58 | 84 | 56 | 0 |

Pending asset [deepseek]: 4 open or unclassified rulings.
Pending f1040 [deepseek]: 2 open or unclassified rulings.
Pending f8606 [deepseek]: 1 open or unclassified rulings.
Pending f8880 [deepseek]: 3 open or unclassified rulings.
Pending f8960 [deepseek]: 2 open or unclassified rulings.
Pending f8995 [deepseek]: 2 open or unclassified rulings.
Pending f8995a [deepseek]: 1 open or unclassified rulings.
Pending g28 [deepseek]: 5 open or unclassified rulings.
Pending gift [deepseek]: 1 open or unclassified rulings.
Pending household [deepseek]: 4 open or unclassified rulings.
Pending ira [deepseek]: 5 open or unclassified rulings.
Pending ltc [deepseek]: 1 open or unclassified rulings.
Pending mq [deepseek]: 2 open or unclassified rulings.
Pending oi8z [deepseek]: 1 open or unclassified rulings.
Pending person [deepseek]: 3 open or unclassified rulings.
Pending qbi [deepseek]: 1 open or unclassified rulings.
Pending qdcg [deepseek]: 2 open or unclassified rulings.
Pending refund [deepseek]: 2 open or unclassified rulings.
Pending s1 [deepseek]: 10 open or unclassified rulings.
Pending s179 [deepseek]: 3 open or unclassified rulings.
Pending s1a [deepseek]: 1 open or unclassified rulings.
Pending s2 [deepseek]: 1 open or unclassified rulings.
Pending s8812 [deepseek]: 4 open or unclassified rulings.
Pending sa [deepseek]: 3 open or unclassified rulings.
Pending sales [deepseek]: 2 open or unclassified rulings.
Pending sb [deepseek]: 2 open or unclassified rulings.
Pending sc [deepseek]: 4 open or unclassified rulings.
Pending scope [deepseek]: 5 open or unclassified rulings.
Pending scveh [deepseek]: 6 open or unclassified rulings.
Pending sdtw [deepseek]: 5 open or unclassified rulings.
Pending se [deepseek]: 5 open or unclassified rulings.
Pending sli [deepseek]: 3 open or unclassified rulings.
Pending u1250 [deepseek]: 13 open or unclassified rulings.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| asset | deepseek | (a) | MISMATCH | Column (a) asks for the classification, such as 3-year property, 5-year property, etc.; the restatement instead directs use of Pub. 946 Appendix B asset classes/class-life tables. |
| asset | deepseek | (b) | MISMATCH | Column (b) is month and year placed in service; the restatement captures only the year and limits it to 2005-2025. |
| asset | deepseek | (c) | MISMATCH | Column (c) requires subtracting allocable credits and deductions, including section 179 and the special allowance, after multiplying; the restatement stops at the multiplication. |
| asset | deepseek | 14 | MISMATCH | The IRS line also provides a 50% special allowance for qualified reuse and recycling property; the full/forty/none choices do not cover it and no refusal names it. |
| div | deepseek | bad_components | MISMATCH | IRS says Box 1b and Box 5 are portions of the amount in box 1a; the helper compares Form 1040 line 3a (total qualified dividends) to box 1a instead of comparing box 1b to box 1a. |
| div | deepseek | box1b | MISMATCH | IRS says 'Box 1b. Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates'; the helper instead takes Form 1040 line 3a, not the Form 1099-DIV box 1b portion. |
| div | deepseek | unsupported | MISMATCH | IRS says 'Any amount received in excess of your basis is taxable to you as capital gain'; the helper only tests box 3 > 0 with basis_reconciled false and omits an excess-distribution condition. |
| f1040 | deepseek | 27b | MISMATCH | IRS says check the box if you are a minister, member of a religious order, or Christian Science practitioner and are filing Schedule SE with an amount also on Form 1040 line 1z; the helper is true for any scope.schedule1 item, so it can check/refuse for non-clergy Schedule 1 income. |
| f2441 | deepseek | 12 | MISMATCH | The IRS line requires including amounts received under a dependent care assistance program from a sole proprietorship or partnership if self-employed or a partner, but the restatement only sums W-2 box 10 benefits through person.dc_benefits. |
| f2441 | deepseek | 22 | MISMATCH | The IRS line says if any amount on line 12 or 13 is from a sole proprietorship or partnership, answer Yes and 'Enter the amount here'; the restatement always enters $0 (sales.zero) and provides no input or refusal. |
| f4562 | deepseek | 25 | MISMATCH | The helper sums asset.bonus_2025 for listed property, but that asset helper uses line 14, which is expressly for property '(other than listed property)'; line 25 is the special allowance for qualified listed property used more than 50% in a qualified business use. |
| f4562 | deepseek | 28 | MISMATCH | The helper adds only line 25 and line 26(h). IRS line 28 says: 'Add amounts in column (h), lines 25 through 27,' so line 27 is omitted. |
| f4562 | deepseek | 29 | MISMATCH | The helper uses asset.s179_2025, which references line 6(c), but line 6 instructions say 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.' Line 29 is limited to column (i), line 26. |
| f8606 | deepseek | 1 | MISMATCH | The IRS line 1 instructions say to include repayments of qualified reservist distributions and to subtract worksheet line 12 "or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less"; the helper uses only worksheet line 12 and omits those items. |
| f8880 | deepseek | 1(b) | MISMATCH | The IRS says 'Complete column (b) only if you’re filing a joint return,' but the restatement sums spouse entries without conditioning column (b) on a joint return. |
| f8880 | deepseek | 2(b) | MISMATCH | The IRS says 'Complete column (b) only if you’re filing a joint return,' but the restatement sums spouse entries without conditioning column (b) on a joint return. |
| f8995 | deepseek | 11 | MISMATCH | IRS line 11 instructions compute 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b' and do not provide a zero floor; the restatement adds an 'If zero or less, enter -0-' condition. |
| f8995a | deepseek | 33 | MISMATCH | The restatement adds an 'if zero or less, enter -0-' floor, but the IRS instruction is only 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'; no zero floor is stated for line 33. |
| ftc | deepseek | taxes | UNCLEAR | The IRS text requires total creditable foreign taxes after reductions and lists Form 1099-INT and Form 1099-DIV as qualified payee statements, but it does not specify box 6 or box 7. |
| gift | deepseek | special | MISMATCH | IRS places only a qualified vehicle with a gross-proceeds acknowledgment, certain intellectual property, and inventory in Section A even over $5,000, and it requires Section B for partial or restricted interests only when the contribution is over $5,000; the restatement treats all vehicles, intellectual property, inventory, conservation or partial interests, and restricted-use property as special … |
| household | deepseek | hsa_both | MISMATCH | It detects both spouses only through hsa_people = 2, which counts people on the return; the IRS says the family-coverage spouse rule applies regardless of whether spouses file jointly or separately. |
| household | deepseek | hsa_step1_sum | MISMATCH | It adds both spouses' Step 1 limits, but IRS line 6 Step 2 says to divide the refigured contribution limit from Step 1 equally between you and your spouse. |
| household | deepseek | test1_met | MISMATCH | Because it depends on test1_persons, it can be false when IRS Test 1 is met by a parent who lives with the filer; the IRS says 'Your parent didn’t have to live with you.' |
| household | deepseek | test1_persons | MISMATCH | It excludes a parent who lives with the filer from Test 1, but the IRS says 'Your parent didn’t have to live with you.' |
| ira | deepseek | 2b | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ltc | deepseek | 2(a) | MISMATCH | The IRS note excludes payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under age 27 at the end of 2025; the restatement instead states the exclusion in terms of the covered person's eligibility for a plan subsidized by an employer. |
| oi8z | deepseek | 8z (amount) | MISMATCH | The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income. |
| person | deepseek | Step 21 | MISMATCH | IRS Step 21 says to subtract step 20 from step 19 as the maximum deductible contribution; the smaller of Step 7 or Step 8 is only the Step 8 shortcut when there are no elective deferrals. |
| person | deepseek | Step 3 | MISMATCH | IRS Step 3 says only to subtract step 2 from step 1, while the restatement adds a zero-or-less floor that can change a negative result. |
| retirement | deepseek | (SMW 6) | MISMATCH | IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still computes line 6 from the recovered-tax-free helper. |
| retirement | deepseek | (SMW 7) | MISMATCH | IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still subtracts line 6 from line 2. |
| s1 | deepseek | 15 | MISMATCH | The IRS says 'If you were self-employed and owe self-employment tax, fill in Schedule SE'; the restatement returns zero unless the person has at least one Schedule C, without refusing partnership or other self-employment income on that path. |
| s1 | deepseek | 16 | MISMATCH | The IRS line is 'Self-employed SEP, SIMPLE, and qualified plans'; the restatement computes only a 'Self-employed SEP or SIMPLE deduction' and returns zero when there is no Schedule C. |
| s1 | deepseek | 17 | MISMATCH | The IRS instructions allow the deduction for 'a partner with net earnings from self-employment' and a 'more-than-2% shareholder in an S corporation,' but the restatement only sums Schedule C (sc) Form 7206 line 14 amounts. |
| s1 | deepseek | 21 | MISMATCH | The IRS says 'Use Pub. 970 instead ... if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico'; the restatement has no such refusal and always uses worksheet line 9 for an eligible filer. |
| s1 | deepseek | 8f | MISMATCH | The IRS line 8f says 'Enter the total of the amounts from Form 8889, lines 16 and 20'; the restatement uses only Form 8889 line 16. |
| s1 | deepseek | 8j | MISMATCH | The restatement excludes 'the rental of personal property' from line 8j, but Pub. 525 says 'You must include on your return income from an activity, even if you don’t expect to make a profit'; line 8l covers only a for-profit rental not in the business. |
| s179 | deepseek | 2 | MISMATCH | Line 2 is the total cost of all section 179 property placed in service, including 'Any listed property from Part V'; the vehicle helper for this total takes 'the amount from line 13' (the carryover to 2026) rather than the vehicle's Part V cost. |
| s179 | deepseek | 7 | MISMATCH | Line 7 must be 'the amount from line 29,' and line 29 says 'Add amounts in column (i), line 26'; the listed-asset helper uses line 6(c) and the vehicle helper uses line 10, not column (i) of line 26. |
| s2 | deepseek | 18 | MISMATCH | IRS line 18 says "Total additional taxes. Add lines 17a through 17z," but the restatement takes only line 17c and has no refusal excluding other 17a-17z amounts. |
| s3 | deepseek | 14 | MISMATCH | IRS line 14 says 'Add lines 13a through 13z'; the restatement instead takes a supplied subtotal and does not compute that addition. |
| s8812 | deepseek | 22 | MISMATCH | IRS line 22 says 'Enter the total of the amounts from Schedule 1 (Form 1040), line 15; Schedule 2 (Form 1040), line 5; Schedule 2 (Form 1040), line 6; and Schedule 2 (Form 1040), line 13'; the restatement uses only Schedule 1 line 15. |
| s8812 | deepseek | 24 | MISMATCH | IRS line 24 has a 1040-NR branch: '1040-NR filers: Enter the amount from Schedule 3 (Form 1040), line 11'; the restatement always adds Form 1040 line 27a. |
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
| sdtw | deepseek | 41 | MISMATCH | The IRS says 'If Schedule D, line 18, is zero or blank, skip lines 41 through 43 and go to line 44.' The gate also computes lines 41-43 when line 19 is zero even if line 18 is zero. |
| sdtw | deepseek | 42 | MISMATCH | Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero. |
| sdtw | deepseek | 43 | MISMATCH | Same gate error as line 41: the IRS skips lines 41 through 43 when Schedule D line 18 is zero or blank, but the restatement computes when line 19 is zero even if line 18 is zero. |
| sli | deepseek | 6 | MISMATCH | The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| carloan | deepseek | 22(ii) | MISMATCH | MISMATCH | IRS column (ii) says 'the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)', but the restatement limits it to Schedule C. |
| carloan | deepseek | 22(iii) | MISMATCH | MISMATCH | IRS line 22(iii) says to subtract 'the amount on line 22, column (ii)', which can include Schedule E or Schedule F deductions; the restatement subtracts only a Schedule C helper (zero without a Schedule C), so it does not compute the IRS line. |
| dependent | deepseek | 2(d) | MISMATCH | MISMATCH | The helper includes expenses paid with dependent care benefits and enters that gross helper amount on line 2(d), but the Form 2441 column (d) instruction says 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' |
| f1040 | deepseek | 27c | MISMATCH | MISMATCH | IRS says check the box on line 27c if you do not want to claim the earned income credit or if you have been instructed to check the box; the restatement expressly does not ask the filer's own choice not to claim the EIC. |
| f2441 | deepseek | 18 | MISMATCH | MISMATCH | The IRS says earned income for lines 18 and 19 is determined as for lines 4 and 5 but does not include dependent care benefits shown on line 12; the restatement's person.dc_earned_b instead removes line 1e, not line 12 benefits. |
| f2441 | deepseek | 19 | MISMATCH | MISMATCH | The spouse's line 19 helper uses person.dc_earned_b, which removes line 1e rather than the line 12 dependent care benefits the IRS says to exclude for lines 18 and 19. |
| f2441 | deepseek | 4 | MISMATCH | MISMATCH | The IRS instructions define earned income using 'The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z,' while the restatement's person.dc_earned helper uses W-2 box 1 plus line 1e and Schedule SE, omitting other line 1z earned income. |
| f2441 | deepseek | 5 | MISMATCH | MISMATCH | The spouse's earned income helper sums person.dc_earned, which uses W-2 box 1 rather than the IRS's Form 1040 line 1z earned-income definition. |
| f2441 | deepseek | CLW 2 | MISMATCH | MISMATCH | The IRS worksheet line 2 says to enter amounts from 'Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14),' but the restatement uses only Schedule 3 line 1. |
| f4562 | deepseek | 22 | MISMATCH | MISMATCH | The restatement omits lines 15 and 16, lines 19g through 19j, and line 20. IRS line 22 says: 'Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21.' |
| f4562 | deepseek | 26(h) | MISMATCH | MISMATCH | The helper uses asset.dep_listed, built from line 19(g) and line 17 MACRS; Part III says 'Don’t include listed property,' while line 26(h) is the Part V depreciation deduction for listed property used more than 50% in a qualified business use. |
| f4952 | deepseek | 4d | UNCLEAR | MISMATCH | The IRS line is 'Net gain from the disposition of property held for investment'; the restatement uses Schedule D line 16, which is not limited to property held for investment and can include other gains or losses. |
| f4952 | deepseek | 4e | UNCLEAR | MISMATCH | The IRS line uses 'your net capital gain from the disposition of property held for investment'; the restatement uses the QDCGT helper based on the smaller of Schedule D lines 15 and 16, which is not limited to property held for investment. |
| f8880 | deepseek | (CLW 2) | MISMATCH | MISMATCH | The IRS Credit Limit Worksheet line 2 says 'Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l,' but the restatement adds only Schedule 3 lines 1 and 2, omitting line 3, 6d, and 6l. |
| f8889 | deepseek | 7 | MISMATCH | MISMATCH | IRS line 7 worksheet counts only months when 'You or your spouse had family coverage under an HDHP and were, or were considered to be, an eligible individual on the first day of the month' and not Medicare; the program uses all months of eligible-individual status, overstating when family coverage did not exist all eligible months. |
| f8960 | deepseek | 5a | UNCLEAR | MISMATCH | IRS line 5a is 'Net gain or loss from disposition of property'; taking only f1040 line 7a's 'Capital gain or (loss)' omits other disposition gains or losses. |
| f8960 | deepseek | 9b | MISMATCH | MISMATCH | IRS line 9b is 'State, local, and foreign income tax' and the instructions require including foreign income and foreign real property taxes attributable to NII unless a credit is claimed; the restatement covers only state/local income and property taxes. |
| f8995 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 instructions say if you're not required to file Schedule D, your net capital gain is the amount on Form 1040 line 7a; the restatement uses only the smaller of Schedule D lines 15 and 16. |
| ftc | deepseek | credit | MISMATCH | MISMATCH | The smaller-of rule is right, but the computation uses limited, which omits the Schedule 2 Part I line 1z addition and Form 4972 subtraction required for regular tax. |
| ftc | deepseek | limited | MISMATCH | MISMATCH | IRS line 20 regular tax is Form 1040 line 16 plus Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972; this uses only f1040 line 16. |
| g28 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says 'Enter the total of all collectibles gain or (loss) from items you reported on Form 8949, Part II'; the restatement enters $0 from div.screen instead, and no refusal excludes Form 8949 collectibles items. |
| g28 | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 requires a positive total of 50%, 2/3, and 1/3 of section 1202 exclusions reported in Form 8949 Part II with code Q; the restatement enters $0 and does not compute those exclusions. |
| g28 | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 requires collectibles gain or (loss) from Form 4684 line 4, Form 6252, Form 6781 Part II, and Form 8824; the restatement enters $0 instead. |
| g28 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is the total collectibles gain from Form 1099-DIV box 2d, Form 2439 box 1d, and Schedule K-1; the restatement uses only div.box2d and omits Form 2439 and Schedule K-1. |
| g28 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 requires long-term capital loss carryovers from Schedule D line 14 and Schedule K-1 (Form 1041) box 11 code D; the restatement enters $0 instead. |
| ira | deepseek | 1a | MISMATCH | MISMATCH | IRS says if you weren't covered but your spouse was, you are considered covered unless you lived apart for all of 2025; cov_you counts only actual work or self-employed plan coverage, so the deemed-coverage case is omitted. |
| ira | deepseek | 2a | MISMATCH | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ira | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is the total of Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits lines 12, 14, and 23 and lists only selected lines. |
| ira | deepseek | 9 | UNCLEAR | MISMATCH | IRS line 9 includes earned income received 'as a self-employed individual or a partner'; person.ira_se is zero without a Schedule C, so partner or other self-employment income not on Schedule C is omitted, and the stated refusal covers only Schedule C income not from personal services. |
| mq | deepseek | q4 | MISMATCH | MISMATCH | The IRS test uses the total depreciable bases of MACRS property placed in service during the last 3 months, excluding nonresidential real property, residential rental property, railroad grading/tunnel bore, property placed in service and disposed of in the same year, and non-MACRS property; the helper merely adds person.mq_q4 and does not apply those exclusions or the personal-use basis reduction. |
| mq | deepseek | total | MISMATCH | MISMATCH | The IRS denominator is the total depreciable bases of all MACRS property placed in service during the entire year, with the same exclusions and personal-use reduction; the helper adds person.mq_total without those limitations. |
| person | deepseek | Step 1 | MISMATCH | MISMATCH | IRS Step 1 says to enter net profit from Schedule C line 31, Schedule F line 34, or Schedule K-1 box 14 code A; the restatement uses only the Schedule C helper. |
| qbi | deepseek | 3 | MISMATCH | MISMATCH | The IRS form line is 'Qualified business net (loss) carryforward from the prior year . . . 3 ( )', where the parentheses indicate a negative loss carryforward; the restatement says to enter it as a positive amount. |
| qdcg | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says to use Form 1040 line 15, but adds: 'However, if you are filing Form 2555 ... enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.' The restatement always uses Form 1040 line 15 and has no Form 2555 refusal or alternate. |
| qdcg | deepseek | 3 | UNCLEAR | UNCLEAR | The Schedule D 'Yes' branch matches, but for the 'No' branch IRS says 'Enter the amount from Form 1040 or 1040-SR, line 7a'; the provided text does not define line 7a, so the program's use of a 'Capital gain distributions, generally Form 1099-DIV box 2a' helper cannot be verified. |
| refund | deepseek | 1 | MISMATCH | MISMATCH | The IRS Exception also requires Pub. 525 when 'You received a refund in 2025 that is for a tax year other than 2024' or 'You made your last payment of 2024 estimated state or local income tax in 2025'; the program's refusals do not exclude those cases. |
| refund | deepseek | 6 | UNCLEAR | MISMATCH | The IRS line says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for married filing separately allows spouse boxes only if 'your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent'; the restatement only adds helper amounts and zeroes spouse boxes for statuses other than MFJ/MFS, omitting those c… |
| retirement | deepseek | (SMW 10) | MISMATCH | MISMATCH | IRS line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement adds line 6 and line 8 even for a pre-1987 annuity. |
| retirement | deepseek | (SMW 11) | MISMATCH | MISMATCH | IRS line 10 says 'Do not complete the rest of this worksheet' when the annuity starting date was before 1987; the restatement still subtracts line 10 from line 2. |
| retirement | deepseek | (SMW 2) | MISMATCH | MISMATCH | The worksheet's before-you-begin note says to 'include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2'; the restatement uses only the cost helper and omits that addition. |
| retirement | deepseek | (SMW 4) | MISMATCH | MISMATCH | The Table 1 helper uses only the after-November 18-1996 numbers; IRS Table 1 also has a before-November 19-1996 column, so a pre-November 19, 1996 annuity would use 300/260/240/170/120 rather than 360/310/260/210/160. |
| retirement | deepseek | (SMW 8) | MISMATCH | MISMATCH | IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement always takes the smaller of line 5 or line 7. |
| s1 | deepseek | 1 | MISMATCH | MISMATCH | The IRS Exception requires Pub. 525 instead of the worksheet in cases such as 'You owed alternative minimum tax in 2024' or 'You couldn’t use the full amount of credits...'; the restatement only refuses box 8 and not_2024. |
| s1 | deepseek | 10 | MISMATCH | MISMATCH | The IRS line says 'Combine lines 1 through 7 and 9'; the restatement adds only lines 1, 2a, 3, 7, and 9, omitting lines 4, 5, and 6. |
| s1 | deepseek | 25 | MISMATCH | MISMATCH | The IRS line says 'Total other adjustments. Add lines 24a through 24z'; the restatement enters only line 24a, omitting 24b through 24z. |
| s1 | deepseek | 26 | MISMATCH | MISMATCH | The IRS line says 'Add lines 11 through 23 and 25'; the restatement omits lines 12, 14, and 23, adding only a subset of that range. |
| s179 | deepseek | 1 | MISMATCH | MISMATCH | Worksheet 1 computes line 1 as the smaller of total cost or $2,500,000: 'Enter the smaller of line 1 or line 2 here' and 'Enter the amount from line 3 here and on Form 4562, line 1'; the restatement always enters $2,500,000. |
| s1a | deepseek | 36b | MISMATCH | MISMATCH | IRS line 36b applies only "If you are married filing jointly," with spouse valid SSN and birth before January 2, 1961; the restatement triggers on the spouse SSN and birth date alone, so it could compute line 36b for a non-MFJ filer such as married filing separately. |
| s3 | deepseek | 1 | MISMATCH | MISMATCH | The helper uses f1040 line 16 alone as regular tax, but the IRS says regular tax is the total of Form 1040 line 16 and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972. |
| s8812 | deepseek | 18a | MISMATCH | MISMATCH | The IRS chart sends optional-method self-employment to the Earned Income Worksheet even when taking the EIC and uses Worksheet B line 4b only if Worksheet B was completed; the restatement selects line 4b/Step 5 merely when a Schedule C exists. |
| s8812 | deepseek | 21 | MISMATCH | MISMATCH | The IRS worksheet line 16 says 'Add lines 6, 7, 11, and 15' for the line 21 amount; the restatement adds only worksheet lines 6 and 7, omitting Tier 1 RRTA lines 11 and 15. |
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
| sdtw | deepseek | 1 | MISMATCH | MISMATCH | The IRS line adds a Form 2555 alternative: 'if you are filing Form 2555 ... enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet'; the restatement always uses Form 1040 line 15. |
| sdtw | deepseek | 4 | MISMATCH | MISMATCH | The IRS footnote says 'If applicable, enter instead the smaller amount you entered on the dotted line next to line 4e of Form 4952'; the restatement always uses line 4e. |
| se | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 includes "Schedule K-1 (Form 1065), box 14, code A" and other income per instructions; restatement uses only this person Schedule C results. |
| se | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 says "Combine lines 1a, 1b, and 2"; restatement enters only the amount from line 2. |
| se | deepseek | 4b | MISMATCH | MISMATCH | IRS line 4b says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"; restatement always enters zero. |
| se | deepseek | 5b | MISMATCH | MISMATCH | IRS line 5b says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"; restatement always enters zero. |
| se | deepseek | 8d | MISMATCH | MISMATCH | IRS line 8d says "Add lines 8a, 8b, and 8c"; restatement enters only line 8a. |
| sli | deepseek | 3 | MISMATCH | MISMATCH | The IRS line says to total "Schedule 1, lines 11 through 20, and 23 and 25"; the restatement omits Schedule 1 line 23 (Archer MSA deduction). |
| sli | deepseek | 5 | MISMATCH | MISMATCH | The IRS says the deduction requires "any status except married filing separately" and line 5 lists only $85,000 for single/HOH/QSS and $170,000 for MFJ; assigning MFS $0 is not in the IRS text and does not exclude MFS. |
| u1250 | deepseek | 1 | UNCLEAR | MISMATCH | IRS line 1 requires the smaller of Form 4797 lines 22 or 24 for the section 1250 property (or going to line 4 if none); the restatement enters $0 from the distribution screen. |
| u1250 | deepseek | 10 | UNCLEAR | MISMATCH | IRS line 10 requires the gain from sale or exchange of a partnership interest attributable to unrecaptured section 1250 gain; the restatement enters $0. |
| u1250 | deepseek | 11 | UNCLEAR | MISMATCH | IRS line 11 requires the total of amounts reported on Schedule K-1, Form 1099-DIV, Form 2439, or a Form 1099-R; using only Form 1099-DIV box 2b omits the other sources. |
| u1250 | deepseek | 12 | UNCLEAR | MISMATCH | IRS line 12 requires unrecaptured section 1250 gain from sales or other dispositions of section 1250 property held more than 1 year outside Part I of Form 4797; the restatement enters $0. |
| u1250 | deepseek | 16 | MISMATCH | MISMATCH | IRS line 16 requires long-term capital loss carryovers from Schedule D line 14 and Schedule K-1 (Form 1041) box 11 code D; the restatement enters $0. |
| u1250 | deepseek | 2 | UNCLEAR | MISMATCH | IRS line 2 requires the Form 4797 line 26g amount for the property on line 1; the restatement enters $0. |
| u1250 | deepseek | 3 | UNCLEAR | MISMATCH | IRS line 3 says to subtract line 2 from line 1; the restatement instead enters $0. |
| u1250 | deepseek | 4 | UNCLEAR | MISMATCH | IRS line 4 requires the unrecaptured section 1250 gain from Form(s) 6252 installment sales; the restatement enters $0. |
| u1250 | deepseek | 5 | UNCLEAR | MISMATCH | IRS line 5 requires Schedule K-1 unrecaptured section 1250 gain from partnerships or S corporations; the restatement enters $0. |
| u1250 | deepseek | 6 | UNCLEAR | MISMATCH | IRS line 6 says to add lines 3 through 5; the restatement instead enters $0. |
| u1250 | deepseek | 7 | UNCLEAR | MISMATCH | IRS line 7 requires the smaller of line 6 or the Form 4797 line 7 gain; the restatement enters $0. |
| u1250 | deepseek | 8 | UNCLEAR | MISMATCH | IRS line 8 requires the amount, if any, from Form 4797 line 8; the restatement enters $0. |
| u1250 | deepseek | 9 | UNCLEAR | MISMATCH | IRS line 9 says to subtract line 8 from line 7 and enter -0- if zero or less; the restatement instead enters $0. |

## Class M hand-work

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f2441 | deepseek (deepseek-flash) | 137 | 135 | 98.5% | 0/151 (0.0%) | pending | 0 | 0 | 2 | 67 |
| w2 | deepseek (deepseek-flash) | 39 | 39 | 100.0% | 0/39 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 176 | 174 | 98.9% | | | 0 | 0 | 2 | 67 |

Pending f2441 [deepseek]: 3 missing expected lines.

### Independence yield

None: every line the second family disputed, the Claude run disputed too.

### Lines both families disputed

None.
