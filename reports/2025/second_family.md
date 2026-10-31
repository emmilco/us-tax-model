# Second-family review comparison — 2025

Summary: 149 form-kind pair(s) with logs from Claude and deepseek; ruled model-error noise 8.6% (401/4661 second-family lines judged; pending reviews are provisional); 71 eligible, 77 pending; raw agreement 79.5% (diagnostic only); current independence yield 273 line(s); both families disputed 503

Written by `tools/transcription/compare_families.py` on 2026-10-31 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

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
| aqee | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| asset | deepseek (deepseek-flash) | 16 | 2 | 12.5% | 10/16 (62.5%) | pending | 0 | 12 | 2 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 2/2 (100.0%) | pending | 0 | 2 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pass | 0 | 0 | 0 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 1/13 (7.7%) | pass | 1 | 0 | 0 | 0 |
| dcprov | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pending | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 21 | 1 | 4.8% | 16/21 (76.2%) | pending | 0 | 19 | 1 | 0 |
| div | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 18 | 9 | 50.0% | 7/18 (38.9%) | pending | 0 | 9 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 52 | 30 | 57.7% | 19/52 (36.5%) | pending | 18 | 4 | 0 | 0 |
| f1095a | deepseek (deepseek-flash) | 29 | 13 | 44.8% | 15/29 (51.7%) | pending | 13 | 3 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 37 | 22 | 59.5% | 10/37 (27.0%) | pending | 4 | 7 | 4 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 1 | 6.7% | 0/15 (0.0%) | pending | 0 | 14 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 14 | 9 | 64.3% | 3/14 (21.4%) | pending | 1 | 4 | 0 | 0 |
| f5329 | deepseek (deepseek-flash) | 10 | 4 | 40.0% | 5/10 (50.0%) | pending | 4 | 2 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 33 | 10 | 30.3% | 16/33 (48.5%) | pending | 9 | 11 | 3 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 2 | 40.0% | 0/5 (0.0%) | pending | 0 | 3 | 0 | 0 |
| f8863 | deepseek (deepseek-flash) | 28 | 21 | 75.0% | 7/28 (25.0%) | pending | 2 | 5 | 0 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 6 | 28.6% | 15/21 (71.4%) | pending | 7 | 8 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 20 | 6 | 30.0% | 10/20 (50.0%) | pending | 4 | 10 | 0 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 22 | 91.7% | 0/24 (0.0%) | pending | 0 | 2 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 19 | 76.0% | 3/25 (12.0%) | pending | 3 | 3 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 97 | 36 | 37.1% | 35/97 (36.1%) | pending | 3 | 32 | 26 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 7 | 43.8% | 0/16 (0.0%) | pending | 4 | 5 | 0 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 2 | 14.3% | 9/14 (64.3%) | pending | 7 | 5 | 0 | 0 |
| ftc | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 6 | 85.7% | 1/7 (14.3%) | pending | 0 | 1 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pass | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 14 | 7 | 50.0% | 5/14 (35.7%) | pending | 1 | 6 | 0 | 0 |
| interest | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 29 | 6 | 20.7% | 16/29 (55.2%) | pending | 0 | 22 | 1 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 0 | 1 | 0 | 0 |
| person | deepseek (deepseek-flash) | 99 | 33 | 33.3% | 52/99 (52.5%) | pending | 22 | 42 | 2 | 0 |
| qbi | deepseek (deepseek-flash) | 5 | 1 | 20.0% | 0/5 (0.0%) | pending | 2 | 2 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 26 | 23 | 88.5% | 0/26 (0.0%) | pass | 0 | 3 | 0 | 0 |
| refund | deepseek (deepseek-flash) | 11 | 6 | 54.5% | 5/11 (45.5%) | pending | 2 | 3 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 26 | 10 | 38.5% | 14/26 (53.8%) | pending | 2 | 14 | 0 | 0 |
| s1 | deepseek (deepseek-flash) | 27 | 6 | 22.2% | 20/27 (74.1%) | pending | 17 | 4 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 14 | 10 | 71.4% | 2/14 (14.3%) | pending | 1 | 2 | 1 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 8 | 18.6% | 34/43 (79.1%) | pending | 1 | 34 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 13 | 8 | 61.5% | 4/13 (30.8%) | pending | 4 | 1 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 11 | 6 | 54.5% | 5/11 (45.5%) | pending | 0 | 5 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 51 | 24 | 47.1% | 20/51 (39.2%) | pending | 14 | 10 | 3 | 0 |
| sa | deepseek (deepseek-flash) | 22 | 15 | 68.2% | 6/22 (27.3%) | pending | 2 | 5 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 4 | 2 | 50.0% | 0/4 (0.0%) | pass | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 48 | 13 | 27.1% | 0/48 (0.0%) | pending | 19 | 15 | 1 | 7 |
| scope | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | no lines | 0 | 0 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 21 | 2 | 9.5% | 0/21 (0.0%) | pending | 7 | 12 | 0 | 0 |
| sd | deepseek (deepseek-flash) | 55 | 7 | 12.7% | 4/55 (7.3%) | pending | 8 | 37 | 3 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 20 | 42.6% | 12/47 (25.5%) | pending | 2 | 19 | 6 | 0 |
| se | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 9 | 4 | 44.4% | 0/9 (0.0%) | pending | 0 | 5 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 19 | 13 | 68.4% | 3/19 (15.8%) | pending | 0 | 4 | 2 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 2 | 66.7% | 0/3 (0.0%) | pending | 0 | 0 | 1 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 6 | 33.3% | 7/18 (38.9%) | pending | 4 | 6 | 2 | 0 |
| w2 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 0 | 1 | 1 | 0 |
| **all** | | 1170 | 503 | 43.0% | | | 188 | 420 | 59 | 7 |

Pending asset [deepseek]: model-error noise above 10%.
Pending carloan [deepseek]: model-error noise above 10%.
Pending dcprov [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending dependent [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails; no passing current source-based partial-input checks: claude, deepseek.
Excluded internal adapters for div: div.screen. Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.
Pending div [deepseek]: no source-defined computed targets; internal adapter checks earn no tax-evidence credit; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending eic [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f1040 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f1095a [deepseek]: model-error noise above 10%.
Pending f2441 [deepseek]: model-error noise above 10%.
Pending f4562 [deepseek]: 14 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Excluded internal adapters for f4952: f4952.election. Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.
Pending f4952 [deepseek]: model-error noise above 10%.
Pending f5329 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f5695 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f8606 [deepseek]: 3 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8863 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f8880 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f8889 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails; no passing current source-based partial-input checks: deepseek.
Pending f8959 [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8960 [deepseek]: model-error noise above 10%.
Pending f8962 [deepseek]: model-error noise above 10%.
Pending f8995 [deepseek]: 9 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8995a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending ftc [deepseek]: model-error noise above 10%; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: required input/interface wording is missing or stale.
Pending g28 [deepseek]: model-error noise above 10%.
Pending household [deepseek]: model-error noise above 10%.
Pending interest [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ira [deepseek]: model-error noise above 10%; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: required input/interface wording is missing or stale.
Pending mq [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending oi8z [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending otjob [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending person [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending qbi [deepseek]: 4 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending refund [deepseek]: model-error noise above 10%.
Pending retirement [deepseek]: model-error noise above 10%.
Pending s1 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending s179 [deepseek]: model-error noise above 10%.
Pending s1a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: current expression/refusal validation fails.
Pending s2 [deepseek]: 1 open, unclassified or interface-gap rulings; model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending s3 [deepseek]: model-error noise above 10%.
Pending s8812 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: current expression/refusal validation fails.
Pending sa [deepseek]: 1 open, unclassified or interface-gap rulings; model-error noise above 10%.
Pending sc [deepseek]: 7 missing expected lines; 34 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending scveh [deepseek]: 19 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sd [deepseek]: 2 open, unclassified or interface-gap rulings; no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: required input/interface wording is missing or stale.
Pending sdtw [deepseek]: model-error noise above 10%; no passing current expression type validation: claude; no verified current request context for claude: current expression/refusal validation fails.
Pending se [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending sli [deepseek]: 5 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ssb [deepseek]: model-error noise above 10%.
Pending tax_on_amount [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tcw [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tipjob [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending u1250 [deepseek]: model-error noise above 10%; no passing current expression type validation: claude, deepseek; no verified current request context for claude: current expression/refusal validation fails; no verified current request context for deepseek: current expression/refusal validation fails.
Pending w2 [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| clcw26 | deepseek | 3 | DISAGREE | (no reason given) |
| f1040 | deepseek | 19 | DISAGREE | (no reason given) |
| f1040 | deepseek | 1a | DISAGREE | (no reason given) |
| f1040 | deepseek | 20 | DISAGREE | (no reason given) |
| f1040 | deepseek | 21 | DISAGREE | (no reason given) |
| f1040 | deepseek | 22 | DISAGREE | (no reason given) |
| f1040 | deepseek | 24 | DISAGREE | (no reason given) |
| f1040 | deepseek | 25a | DISAGREE | (no reason given) |
| f1040 | deepseek | 25c | DISAGREE | (no reason given) |
| f1040 | deepseek | 27a | DISAGREE | (no reason given) |
| f1040 | deepseek | 28 | DISAGREE | (no reason given) |
| f1040 | deepseek | 2a | DISAGREE | (no reason given) |
| f1040 | deepseek | 2b | DISAGREE | (no reason given) |
| f1040 | deepseek | 32 | DISAGREE | (no reason given) |
| f1040 | deepseek | 33 | DISAGREE | (no reason given) |
| f1040 | deepseek | 34 | DISAGREE | (no reason given) |
| f1040 | deepseek | 37 | DISAGREE | (no reason given) |
| f1040 | deepseek | 3b | DISAGREE | (no reason given) |
| f1040 | deepseek | 6d | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_apr | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_aug | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_dec | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_feb | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jan | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jul | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jun | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_mar | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_may | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_nov | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_oct | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_sep | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.line33c | DISAGREE | (no reason given) |
| f2441 | deepseek | 20 | DISAGREE | (no reason given) |
| f2441 | deepseek | 21 | DISAGREE | The $5,000 limit is halved for married filing separately only when the spouse's earned income must be entered on line 19; the interface does not supply the considered-unmarried fact, so the MFS branch uses $2,500. |
| f2441 | deepseek | 25 | DISAGREE | (no reason given) |
| f2441 | deepseek | 6 | DISAGREE | (no reason given) |
| f4952 | deepseek | 2 | DISAGREE | (no reason given) |
| f5329 | deepseek | 4 | DISAGREE | The SIMPLE IRA 25% rate on the SIMPLE IRA portion is applied in the provided person.x_tax aggregate. |
| f5329 | deepseek | 47 | DISAGREE | Line 47 current-year HSA excess contributions are taken from Form 8889 line 13 because the underlying contribution, employer-contribution and limit detail is outside the supplied Form 5329 interface. |
| f5329 | deepseek | 48 | DISAGREE | Lines 42 through 46 are not in this Parts I and VII slice; the total excess contributions are taken from the provided person.x_hsa_excess aggregate. |
| f5329 | deepseek | 49 | DISAGREE | (no reason given) |
| f5695 | deepseek | 15 | DISAGREE | (no reason given) |
| f5695 | deepseek | 16 | DISAGREE | (no reason given) |
| f5695 | deepseek | 19f | DISAGREE | (no reason given) |
| f5695 | deepseek | 20c | DISAGREE | (no reason given) |
| f5695 | deepseek | 23c | DISAGREE | (no reason given) |
| f5695 | deepseek | 26c | DISAGREE | (no reason given) |
| f5695 | deepseek | 32 | DISAGREE | (no reason given) |
| f5695 | deepseek | 32b | DISAGREE | (no reason given) |
| f5695 | deepseek | f5695.claiming_part1 | DISAGREE | The IRS text does not define this project interface. Chosen reading: true when the Part I residential clean energy credit on line 15 is greater than zero. |
| f8863 | deepseek | 19 | DISAGREE | The printed line carries the Credit Limit Worksheet line 7 amount; because this interface is NonNegDollars, any negative worksheet amount is floored at zero. |
| f8863 | deepseek | 8 | DISAGREE | (no reason given) |
| f8880 | deepseek | 10 | DISAGREE | (no reason given) |
| f8880 | deepseek | 2(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 3(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 3(b) | DISAGREE | (no reason given) |
| f8880 | deepseek | 5(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 5(b) | DISAGREE | (no reason given) |
| f8880 | deepseek | 7 | DISAGREE | (no reason given) |
| f8889 | deepseek | 12 | DISAGREE | (no reason given) |
| f8889 | deepseek | 14b | DISAGREE | (no reason given) |
| f8889 | deepseek | 15 | DISAGREE | (no reason given) |
| f8889 | deepseek | 8 | DISAGREE | (no reason given) |
| f8960 | deepseek | 10 | DISAGREE | (no reason given) |
| f8960 | deepseek | 9a | DISAGREE | (no reason given) |
| f8960 | deepseek | 9b | DISAGREE | The closed interface supplies only state/local income and property taxes reasonably allocated to NII and excludes foreign taxes for which a credit is claimed; any other deductible investment tax is refused via f8960.unsupported. |
| f8962 | deepseek | 1 | DISAGREE | (no reason given) |
| f8962 | deepseek | 2a | DISAGREE | Worksheet 1-1 also adds Form 2555 lines 45 and 50; no such input is supplied, so this transcription omits them. |
| f8962 | deepseek | 2b | DISAGREE | (no reason given) |
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
| household | deepseek | household.qss_fails | DISAGREE | (no reason given) |
| person | deepseek | Step 5 | DISAGREE | The worksheet requires the reduced self-employed rate from the Pub. 560 rate table or rate worksheet; no supplied table or atom expresses the conversion from the plan contribution percentage to that rate. This transcription uses the actual SEP contribution as the step 5 amount. |
| person | deepseek | person.hsa_addtax | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_agreed | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_deduction | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_step1 | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_taxable | DISAGREE | (no reason given) |
| person | deepseek | person.income179 | DISAGREE | (no reason given) |
| person | deepseek | person.ira_contrib | DISAGREE | (no reason given) |
| person | deepseek | person.medicare5 | DISAGREE | (no reason given) |
| person | deepseek | person.medicare6 | DISAGREE | (no reason given) |
| person | deepseek | person.qbi | DISAGREE | (no reason given) |
| person | deepseek | person.s179_listed | DISAGREE | (no reason given) |
| person | deepseek | person.s179_nonlisted | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line1 | DISAGREE | (no reason given) |
| person | deepseek | person.sc_1a | DISAGREE | (no reason given) |
| person | deepseek | person.tip_reported | DISAGREE | (no reason given) |
| person | deepseek | person.x_hsa_excess | DISAGREE | (no reason given) |
| person | deepseek | person.x_l1 | DISAGREE | (no reason given) |
| person | deepseek | person.x_l1_s | DISAGREE | (no reason given) |
| person | deepseek | person.x_l2_all | DISAGREE | (no reason given) |
| person | deepseek | person.x_l2_s | DISAGREE | (no reason given) |
| person | deepseek | person.x_two23 | DISAGREE | No supplied field distinguishes multiple exception 23 situations; this transcription uses false. |
| qbi | deepseek | qbi.eligible | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.net_capital_gain | DISAGREE | (no reason given) |
| refund | deepseek | 9 | DISAGREE | The opening instruction says none of the refund is taxable if you did not itemize deductions or elected state and local general sales taxes instead of income taxes; line 9 is zero in those cases, otherwise it is the smaller of lines 3 and 8. |
| refund | deepseek | refund.has | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.is_e23 | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.is_ira | DISAGREE | (no reason given) |
| s1 | deepseek | 10 | DISAGREE | (no reason given) |
| s1 | deepseek | 11 | DISAGREE | (no reason given) |
| s1 | deepseek | 13 | DISAGREE | (no reason given) |
| s1 | deepseek | 15 | DISAGREE | (no reason given) |
| s1 | deepseek | 17 | DISAGREE | Summed across Schedule C businesses because no person-level health-insurance-deduction aggregate is supplied. |
| s1 | deepseek | 18 | DISAGREE | (no reason given) |
| s1 | deepseek | 19a | DISAGREE | (no reason given) |
| s1 | deepseek | 20 | DISAGREE | (no reason given) |
| s1 | deepseek | 26 | DISAGREE | (no reason given) |
| s1 | deepseek | 2a | DISAGREE | (no reason given) |
| s1 | deepseek | 3 | DISAGREE | (no reason given) |
| s1 | deepseek | 7 (box) | DISAGREE | (no reason given) |
| s1 | deepseek | 8f | DISAGREE | The archived instructions also mention Form 8889 line 20, but the supplied interfaces provide only the person-level taxable HSA distribution total (person.hsa_taxable); line 8f is computed from that total. |
| s1 | deepseek | 8z | DISAGREE | (no reason given) |
| s1 | deepseek | 9 | DISAGREE | (no reason given) |
| s1 | deepseek | s1.has_sc | DISAGREE | (no reason given) |
| s1 | deepseek | s1.sc_1a | DISAGREE | The IRS pages do not define a Schedule 1 result named sc_1a; I read this required flag as true when the supplied person.sc_1a count is positive. |
| s179 | deepseek | s179.differs | DISAGREE | The IRS pages do not name this interface. Read here as whether the business income limitation reduces the deduction below the sum of lines 9 and 10, i.e. whether a carryover arises. |
| s1a | deepseek | 38 | DISAGREE | (no reason given) |
| s2 | deepseek | 11 | DISAGREE | (no reason given) |
| s2 | deepseek | 21 | DISAGREE | Only the computed Part II amounts are summed; other Part II amounts are outside scope and covered by s2.other. |
| s2 | deepseek | 4 | DISAGREE | (no reason given) |
| s2 | deepseek | 8 (box) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW A 4) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 10) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 12) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 13) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 14) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 4) | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 5) | DISAGREE | (no reason given) |
| s8812 | deepseek | 19 | DISAGREE | (no reason given) |
| s8812 | deepseek | 20 | DISAGREE | (no reason given) |
| s8812 | deepseek | 22 | DISAGREE | Schedule 2 lines 5, 6 and 13 are read as Form 8959 line 24, Form 8960 line 17 and the aggregate additional HSA tax (person.hsa_addtax). Other Schedule 2 amounts are refused through s2.other. |
| s8812 | deepseek | 23 | DISAGREE | (no reason given) |
| s8812 | deepseek | 25 | DISAGREE | (no reason given) |
| s8812 | deepseek | 26 | DISAGREE | (no reason given) |
| s8812 | deepseek | s8812.clwb_complete | DISAGREE | Credit Limit Worksheet B is completed when a supported credit requiring it is claimed (residential clean energy credit), Form 2555 is not filed (approximated by sa.excluded_income false), and line 4 is more than zero. Other credits that would require Worksheet B are refused through scope.credits. |
| sa | deepseek | 12 | DISAGREE | No noncash charitable gift input is provided in this closed interface; entered as zero. |
| sa | deepseek | 9 | DISAGREE | The archived text only says attach Form 4952; the amount is taken from Form 4952 line 7 as the investment interest deduction. |
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
| dependent | deepseek | 2(c) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 28 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 31 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.actc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.claimed | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.dc_count | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.dc_qp | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_ssn_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test1 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test2 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_person | DISAGREE | DISAGREE | The taxpayer's own SSN or ITIN eligibility is a return-level condition and is not tested here. |
| dependent | deepseek | dependent.ptc_magi_counted | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 6 (eic.line6) | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.check_27c | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.clergy | DISAGREE | DISAGREE | No clergy/church-employee status input is in the supplied interface; set false. The arithmetic covers the non-clergy case. |
| eic | deepseek | eic.credit | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.self_employed | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | eic.separated_box | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 1e | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 6c | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_used | DISAGREE | DISAGREE | The IRS text supplies the b_counted gate for whether column B is counted; b_used exposes that same condition for other forms. |
| f1095a | deepseek | f1095a.line33a | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.line33b | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 1 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 2 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
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
| f5329 | deepseek | 2 | DISAGREE | DISAGREE | The exception amount is taken from the provided person.x_limited_sum aggregate, which limits the total exceptions to line 1. |
| f5329 | deepseek | f5329.must | DISAGREE | DISAGREE | Within this Parts I and VII slice, the form is treated as required when there is an early distribution on line 1 or total HSA excess contributions on line 48. |
| f5695 | deepseek | 14 | DISAGREE | DISAGREE | The archived worksheet lists additional Schedule 3 and Form 1040 credits not present in the supplied line interface; this transcription subtracts only the available referenced credits. The worksheet note allowing Schedule 8812 Credit Limit Worksheet B line 14 instead of Form 1040 line 19 is not exercised because no direction input is supplied. |
| f5695 | deepseek | 18b | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 20d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 22d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 23d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 24d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 25e | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 29h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 31 | DISAGREE | DISAGREE | The archived worksheet includes Schedule 3 lines 6l and 6d, which are not present in the supplied line interface; this transcription subtracts only the available Schedule 3 lines 1, 2, 3, and 4. |
| f5695 | deepseek | 32a | DISAGREE | DISAGREE | (no reason given) |
| f8606 | deepseek | 1 | DISAGREE | DISAGREE | The IRS worksheet permits line 1 to be figured through the IRA Deduction Worksheet or the Pub. 590-A reduced-deduction worksheet; with no additional input interface, this slice takes line 1 as the supplied nondeductible contribution amount. |
| f8606 | deepseek | 2 | DISAGREE | DISAGREE | The IRS instructions allow line 2 to be adjusted for return of excess contributions, divorce transfers, and rollovers of nontaxable plan amounts; this closed slice takes line 2 as the supplied total basis. |
| f8606 | deepseek | 3 (question) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 7 (box) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | f8863.eligible | DISAGREE | DISAGREE | The IRS pages do not define a single 'eligible' line; this helper encodes eligibility for the American opportunity credit from the two supplied gates: qualified expenses paid and no AOC ban. |
| f8863 | deepseek | f8863.kid_needed | DISAGREE | DISAGREE | Encodes the instructions' questions for whether the taxpayer is under age 24, meets the age/student/support tests, has a parent alive, and is not filing jointly. |
| f8880 | deepseek | 1(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 1(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 2(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 6(a) | DISAGREE | DISAGREE | The Form 8880 caution makes the credit unavailable for a person born after January 1, 2008, claimed as a dependent, or a student. When the taxpayer is ineligible under person.sav_ineligible, column (a) is zero; otherwise it is the smaller of line 5(a) and $2,000. |
| f8880 | deepseek | 6(b) | DISAGREE | DISAGREE | The Form 8880 caution makes the credit unavailable for a person born after January 1, 2008, claimed as a dependent, or a student. When the spouse is ineligible under person.sav_ineligible, column (b) is zero; otherwise it is the smaller of line 5(b) and $2,000. |
| f8889 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 17b | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | 3 | DISAGREE | DISAGREE | The IRS text does not state a rounding rule for line 3. The monthly amounts are summed and divided by 12 with half-up rounding to the cent using the supplied 1/12 rate. |
| f8889 | deepseek | 6 | DISAGREE | DISAGREE | The split uses the published household.hsa_both aggregate for whether both spouses have HSAs; if that aggregate is unknown, the split is unknown. |
| f8889 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.excess_amt | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.share_raw | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.split | DISAGREE | DISAGREE | (no reason given) |
| f8889 | deepseek | f8889.step1 | DISAGREE | DISAGREE | (no reason given) |
| f8959 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| f8959 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| f8960 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| f8960 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| f8960 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 28 | DISAGREE | DISAGREE | For line 5 of 400 or more there is no repayment limitation; line 28 is set to 0 here and line 29 uses line 27 directly. |
| f8962 | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 9 | DISAGREE | DISAGREE | Part IV allocation and Part V alternative-calculation inputs are not supplied; the tool refuses when f8962.alloc or f8962.married_in_2025 is true. |
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
| ftc | deepseek | ftc.credit | DISAGREE | DISAGREE | The archived text defines the election credit as the smaller of total foreign tax and regular tax. Regular tax is read as Form 1040 line 16 plus Schedule 2 Part I line 1z, floored at zero; scope.other_line16 is refused because the closed interface does not supply the Form 4972 and other line-16 adjustments the instructions require. The line returns zero when the election conditions are not met. |
| g28 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.ctc_ssn | DISAGREE | DISAGREE | Read as at least one person has an SSN valid for employment, as the CTC rule requires only one spouse on a joint return to have it. |
| household | deepseek | household.hoh_fails | DISAGREE | DISAGREE | Read as not meeting unmarried or considered-unmarried status, the home-cost test, and at least one dependent HOH test. |
| household | deepseek | household.hsa_both | DISAGREE | DISAGREE | Read as at least two person entries having HSA forms. |
| household | deepseek | household.rdp_community_property | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.roster_bad | DISAGREE | DISAGREE | Read as an invalid roster: not exactly one taxpayer, more than one spouse, or a spouse entry when the filer reports not married. |
| household | deepseek | household.taxpayer_work_ssn | DISAGREE | DISAGREE | (no reason given) |
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
| person | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | 28 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | 31 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | Step 6 | DISAGREE | DISAGREE | The worksheet requires multiplying $350,000 by the plan contribution rate; the supplied atoms do not multiply money by a whole-percent Count. This transcription uses the compensation limit itself, which does not reduce step 7 unless the step 5 amount exceeds $350,000. |
| person | deepseek | eligible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_earned_b | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.dc_has_box10 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.edu_kid | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.educator_deduction | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.eic_se | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.hsa_share | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_8606_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_amount_a | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_cov | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_deduction | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_dist_gate | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_files_8606 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line6 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_line7 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_nondeductible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_rollovers | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_se | DISAGREE | DISAGREE | No supplied input separately identifies the self-employment portion of the IRA deduction; this uses the total IRA deduction. |
| person | deepseek | person.ira_ssb | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.ira_taxable | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.plan_amount_a | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.plan_rollovers | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.plan_taxable | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.s16 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_ineligible | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.sav_line2 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line12 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line13 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.se_line6 | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.x_c05 | DISAGREE | DISAGREE | No supplied field separately reports exception 05; this transcription uses zero. |
| person | deepseek | person.x_limit_binds | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.x_limited_sum | DISAGREE | DISAGREE | (no reason given) |
| person | deepseek | person.x_other_exc | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.deduction | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.taxable_before | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 3 | DISAGREE | DISAGREE | Blank Schedule D lines are not representable; if either line is supplied as a loss, the amount is zero. |
| qdcg | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 8 | DISAGREE | DISAGREE | If the 2024 filing status was married filing separately and the spouse itemized, the worksheet says to skip lines 5 through 7 and enter line 4 on line 8; the true branch does that. |
| refund | deepseek | refund.taxable | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | (SMW 4) | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.amount_a | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.has_rollover | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l1 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l1_s | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_e05 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_e09 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_e19 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_e22 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_e23 | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.l2_s | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.sav_amount | DISAGREE | DISAGREE | (no reason given) |
| retirement | deepseek | retirement.taxable | DISAGREE | DISAGREE | A Roth IRA distribution other than a qualified distribution generally requires Form 8606; the archived text does not supply the needed basis, so this line refuses the listed screening inputs and otherwise uses the distribution reduced by rollover and box 5. |
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
| s2 | deepseek | 1a | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5a | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 5b | DISAGREE | DISAGREE | (no reason given) |
| s3 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 11) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 2) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 3) | DISAGREE | DISAGREE | The closed interface has no separate Earned Income Worksheet line 7; this uses Schedule 8812 line 18a as the earned income figure. |
| s8812 | deepseek | (CLW B 7) | DISAGREE | DISAGREE | The W-2 box 4 and box 6 aggregate (and Additional Medicare/RRTA worksheet amounts) is not supplied by the closed interface. This line is zero when Credit Limit Worksheet B is not completed and refuses when it is completed. |
| s8812 | deepseek | 16b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 18a | DISAGREE | DISAGREE | The closed interface supplies only a yes/no combat-pay question, not its amount. This line uses eic.earned_income, is zero-or-more, and refuses when s8812.combat_pay is true. |
| s8812 | deepseek | 21 | DISAGREE | DISAGREE | The required W-2 box 4 and 6 aggregate (and any Additional Medicare/RRTA worksheet amounts) is not supplied by the closed interface. When Part II-B is not needed this line is zero; when it is needed the line refuses. |
| s8812 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
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
| ssb | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 18 | DISAGREE | DISAGREE | Refused when ssb.pub915 or ssb.lump_sum is true; the worksheet cannot be used for the Pub. 915 exceptions or the lump-sum election. |
| ssb | deepseek | 6 | DISAGREE | DISAGREE | Sums the supplied Schedule 1 adjustment lines; refuses when scope.schedule1 is true. Schedule 1 lines 12, 14 and 23 are not supplied as separate lines. |
| ssb | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
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
| aqee | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| asset | deepseek (deepseek-flash) | 15 | 11 | 73.3% | 0/15 (0.0%) | pending | 4 | 0 | 0 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pass | 0 | 1 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| dcprov | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 11 | 8 | 72.7% | 0/11 (0.0%) | pass | 0 | 1 | 2 | 0 |
| div | deepseek (deepseek-flash) | 22 | 22 | 100.0% | 0/22 (0.0%) | pass | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 58 | 54 | 93.1% | 0/58 (0.0%) | pass | 2 | 1 | 1 | 0 |
| f1095a | deepseek (deepseek-flash) | 76 | 75 | 98.7% | 0/76 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f2441 | deepseek (deepseek-flash) | 36 | 29 | 80.6% | 0/36 (0.0%) | pass | 2 | 3 | 2 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pass | 3 | 2 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 15 | 14 | 93.3% | 1/15 (6.7%) | pass | 0 | 1 | 0 | 0 |
| f5329 | deepseek (deepseek-flash) | 7 | 5 | 71.4% | 0/7 (0.0%) | pass | 1 | 1 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 72 | 71 | 98.6% | 0/72 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 1 | 0 | 1 | 0 |
| f8863 | deepseek (deepseek-flash) | 25 | 17 | 68.0% | 0/25 (0.0%) | pass | 2 | 4 | 2 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 17 | 81.0% | 0/21 (0.0%) | pass | 3 | 1 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 12 | 63.2% | 0/19 (0.0%) | pass | 5 | 0 | 2 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 23 | 95.8% | 0/24 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 23 | 92.0% | 0/25 (0.0%) | pass | 1 | 1 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 95 | 25 | 26.3% | 0/95 (0.0%) | pass | 1 | 2 | 67 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 13 | 81.2% | 0/16 (0.0%) | pending | 1 | 1 | 1 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 12 | 85.7% | 0/14 (0.0%) | pending | 1 | 0 | 1 | 0 |
| ftc | deepseek (deepseek-flash) | 12 | 11 | 91.7% | 0/12 (0.0%) | pass | 0 | 1 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 2 | 28.6% | 0/7 (0.0%) | pass | 1 | 4 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 5 | 5 | 100.0% | 0/5 (0.0%) | pass | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 39 | 36 | 92.3% | 0/39 (0.0%) | pass | 2 | 0 | 1 | 0 |
| interest | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 21 | 16 | 76.2% | 0/21 (0.0%) | pending | 1 | 4 | 0 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 7 | 5 | 71.4% | 0/7 (0.0%) | pending | 0 | 2 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pass | 0 | 0 | 0 | 0 |
| person | deepseek (deepseek-flash) | 32 | 27 | 84.4% | 0/32 (0.0%) | pass | 0 | 0 | 5 | 0 |
| qbi | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 25 | 24 | 96.0% | 0/25 (0.0%) | pass | 0 | 0 | 1 | 0 |
| refund | deepseek (deepseek-flash) | 9 | 7 | 77.8% | 0/9 (0.0%) | pass | 0 | 2 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 10 | 3 | 30.0% | 0/10 (0.0%) | pass | 0 | 7 | 0 | 0 |
| s1 | deepseek (deepseek-flash) | 29 | 21 | 72.4% | 1/29 (3.4%) | pass | 3 | 3 | 2 | 0 |
| s179 | deepseek (deepseek-flash) | 13 | 11 | 84.6% | 1/13 (7.7%) | pass | 0 | 2 | 0 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 41 | 95.3% | 0/43 (0.0%) | pass | 1 | 1 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 12 | 10 | 83.3% | 0/12 (0.0%) | pass | 2 | 0 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 13 | 11 | 84.6% | 0/13 (0.0%) | pass | 1 | 0 | 1 | 0 |
| s8812 | deepseek (deepseek-flash) | 50 | 48 | 96.0% | 0/50 (0.0%) | pass | 0 | 1 | 1 | 0 |
| sa | deepseek (deepseek-flash) | 24 | 21 | 87.5% | 0/24 (0.0%) | pending | 2 | 1 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 3 | 1 | 33.3% | 0/3 (0.0%) | pass | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 6 | 4 | 66.7% | 0/6 (0.0%) | pending | 1 | 1 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 75 | 68 | 90.7% | 0/75 (0.0%) | pending | 3 | 1 | 3 | 0 |
| scope | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pass | 0 | 0 | 2 | 0 |
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
| **all** | | 1314 | 1082 | 82.3% | | | 50 | 77 | 105 | 0 |

Pending asset [deepseek]: 4 open, unclassified or interface-gap rulings.
Pending f8606 [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending f8995 [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending f8995a [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending ira [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending ltc [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending mq [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending oi8z [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending qbi [deepseek]: model-error noise above 10%.
Pending sa [deepseek]: 3 open, unclassified or interface-gap rulings.
Pending sb [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending sc [deepseek]: 4 open, unclassified or interface-gap rulings.
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
| f1040 | deepseek | 1z | MISMATCH | IRS says "Add lines 1a through 1h"; the restatement adds only line 1a and line 1e. |
| f1040 | deepseek | 27c | MISMATCH | IRS says to check the box if you do not want the EIC or if instructed; the restatement computes only instructed cases and does not ask the filer opt-out. |
| f2441 | deepseek | 12 | MISMATCH | The IRS line says 'If you were self-employed or a partner, include amounts you received under a dependent care assistance program from your sole proprietorship or partnership'; the restatement sums only W-2 box 10 benefits and has no refusal for that case. |
| f2441 | deepseek | 22 | MISMATCH | The IRS line asks whether any amount on line 12 or 13 is from a sole proprietorship or partnership and enters that amount if yes; the restatement always enters $0. |
| f4562 | deepseek | 25 | MISMATCH | The helper sums asset.bonus_2025 for listed property, but that asset helper uses line 14, which is expressly for property '(other than listed property)'; line 25 is the special allowance for qualified listed property used more than 50% in a qualified business use. |
| f4562 | deepseek | 28 | MISMATCH | The helper adds only line 25 and line 26(h). IRS line 28 says: 'Add amounts in column (h), lines 25 through 27,' so line 27 is omitted. |
| f4562 | deepseek | 29 | MISMATCH | The helper uses asset.s179_2025, which references line 6(c), but line 6 instructions say 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.' Line 29 is limited to column (i), line 26. |
| f5329 | deepseek | 48 | MISMATCH | The form says 'Total excess contributions. Add lines 46 and 47'; the restatement enters only line 47, omitting line 46 prior-year excess contributions. |
| f8606 | deepseek | 1 | MISMATCH | The IRS line 1 instructions say to include repayments of qualified reservist distributions and to subtract worksheet line 12 "or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less"; the helper uses only worksheet line 12 and omits those items. |
| f8863 | deepseek | 15 | MISMATCH | IRS line 15 says if zero or less, skip lines 16 and 17 and enter -0- on line 18; the restatement instead enters -0- on line 15. |
| f8863 | deepseek | 18 | MISMATCH | IRS says if line 10 is zero, skip lines 11 through 17 and enter -0- on line 18; the restatement gates line 18 only on line 4 and computes from lines 12, 15 and 16. |
| f8880 | deepseek | 1(b) | MISMATCH | The IRS says 'Complete column (b) only if you're filing a joint return'; the restatement sums spouse entries without an MFJ gate. |
| f8880 | deepseek | 2(b) | MISMATCH | The IRS says 'Complete column (b) only if you're filing a joint return'; the restatement sums spouse entries without an MFJ gate. |
| f8880 | deepseek | 4(a) | MISMATCH | The IRS line says 'If married filing jointly, include both spouses’ amounts in both columns'; the restatement's dist_2025 sums every confirmed person's 2025 distributions even on a nonjoint return. |
| f8889 | deepseek | 10 | MISMATCH | The IRS line is 'Qualified HSA funding distributions' and the instructions say 'Enter this amount on line 10'; the restatement always enters zero. |
| f8889 | deepseek | 14b | MISMATCH | The IRS line says 'Distributions included on line 14a that you rolled over to another HSA. Also include any excess contributions (and the earnings on those excess contributions) included on line 14a that were withdrawn by the due date'; the restatement includes only rollovers. |
| f8889 | deepseek | 15 | MISMATCH | The IRS instructions say 'Do not include the distribution of an excess contribution taken out after the due date, including extensions, of your return even if used for qualified medical expenses'; the restatement omits that exclusion. |
| f8889 | deepseek | 17a | MISMATCH | The IRS exceptions are distributions made after the account beneficiary 'Dies, Becomes disabled or Turns age 65'; the restatement lists only disabled or age 65. |
| f8889 | deepseek | 4 | MISMATCH | The IRS line says 'Enter the amount you and your employer contributed to your Archer MSAs for 2025 from Form 8853, lines 1 and 2' and to include spouse's Archer MSA contributions in family-coverage cases; the restatement always enters zero. |
| f8960 | deepseek | 9b | MISMATCH | IRS line 9b includes state, local, and foreign income taxes and foreign real property taxes; the restatement is limited to state and local income and property taxes and only notes an exclusion for foreign credits. |
| f8962 | deepseek | 9 | MISMATCH | The IRS asks whether you are allocating policy amounts or 'do you want to use the alternative calculation for year of marriage'; the restatement makes line 9 Yes merely for a joint return with pre-marriage Marketplace coverage, regardless of the election or other Table 4 eligibility. |
| f8995 | deepseek | 11 | MISMATCH | IRS line 11 instructions compute 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b' and do not provide a zero floor; the restatement adds an 'If zero or less, enter -0-' condition. |
| f8995a | deepseek | 33 | MISMATCH | The restatement adds an 'if zero or less, enter -0-' floor, but the IRS instruction is only 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'; no zero floor is stated for line 33. |
| g28 | deepseek | 2 | MISMATCH | IRS line 2 requires the positive total of section 1202 exclusions from Form 8949 Part II code Q at 50%, 2/3, or 1/3; the restatement enters $0 from a distribution helper and does not compute those amounts, and its refusal covers only section 1202 distributions, not Code Q exclusions generally. |
| household | deepseek | test1_met | MISMATCH | Because it is test1_persons > 0, it inherits the live-in-parent exclusion and can report Test 1 not met even though the IRS text says 'Your parent didn't have to live with you.' |
| household | deepseek | test1_persons | MISMATCH | The restatement limits Test 1 to a parent 'who does not live with you,' but the IRS text says 'Your parent didn't have to live with you,' so a live-in parent can still meet Test 1. |
| ira | deepseek | 2b | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ltc | deepseek | 2(a) | MISMATCH | The IRS note excludes payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under age 27 at the end of 2025; the restatement instead states the exclusion in terms of the covered person's eligibility for a plan subsidized by an employer. |
| oi8z | deepseek | 8z (amount) | MISMATCH | The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income. |
| s1 | deepseek | 16 | MISMATCH | IRS line 16 is 'Self-employed SEP, SIMPLE, and qualified plans'; the helper computes only SEP or SIMPLE and returns zero for a qualified plan such as a solo 401(k) without refusing it. |
| s1 | deepseek | 8f | MISMATCH | IRS line 8f says 'Enter the total of the amounts from Form 8889, lines 16 and 20'; the restatement uses only Form 8889 line 16. |
| s1 | deepseek | 8i | MISMATCH | IRS Pub. 525 says 'These rules don’t apply to scholarship or fellowship awards. See Scholarships and fellowships, later'; the restatement puts a 'scholarship prize' on line 8i. |
| s1a | deepseek | 23 | MISMATCH | Line 23 adds column (iii), but the program's column (iii) subtracts only Schedule C interest; IRS column (ii) is 'Deducted on Schedule C, Schedule E, or Schedule F.' |
| s2 | deepseek | 18 | MISMATCH | The IRS says 'Add lines 17a through 17z,' but the restatement enters only the amount from line 17c. |
| s2 | deepseek | 1z | MISMATCH | The IRS says 'Add lines 1a through 1y,' but the restatement enters only the amount from line 1a. |
| s3 | deepseek | 14 | MISMATCH | IRS line 14 says "Add lines 13a through 13z," but the restatement accepts a supplied subtotal instead of adding those lines. |
| sa | deepseek | 5e | MISMATCH | IRS line 5e says if you completed Form 2555 or 4563, or excluded Puerto Rico income, see the SALT worksheet; that worksheet adds those excluded amounts to line 11b. The program's ceiling helper uses only Form 1040 line 11b and there is no excluded-income refusal on line 5e. |
| sa | deepseek | 9 | UNCLEAR | The provided Schedule A text only says 'Investment interest. Attach Form 4952 if required. See instructions'; the line 9 instructions, including how to figure investment interest when Form 4952 is not required, are not provided. |
| sb | deepseek | 7a | MISMATCH | The restatement covers only Question 1; the IRS line also has Line 7a—Question 2, which asks whether you are required to file FinCEN Form 114. |
| sc | deepseek | 23 | MISMATCH | IRS line 23 includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'; the restatement omits the paid family and medical leave fund. |
| sc | deepseek | 4 (sc.f7206_line4) | MISMATCH | IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established'; the restatement uses only this business's net profit. |
| sc | deepseek | 5 (sc.f7206_line5) | MISMATCH | IRS line 5 says 'total of all net profits* from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income allocable to the profitable businesses'; the restatement uses only this person's Schedule C net profits. |
| scveh | deepseek | 7 | MISMATCH | IRS states 'The depreciation deduction, including the section 179 expense deduction and special depreciation allowance, for passenger automobiles is limited'; the restatement applies a published passenger-automobile limit unconditionally and has no refusal when scveh.passenger is false. |
| scveh | deepseek | 9 (scveh.line9) | MISMATCH | IRS says 'You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle'; the restatement allows actual whenever method is actual and only refuses standard under smr_bad. |
| sd | deepseek | 20 | MISMATCH | IRS line 17 says: 'No. Skip lines 18 through 21, and go to line 22.' The restatement computes line 20 even when line 17 is No; it should be skipped. |
| sli | deepseek | 6 | MISMATCH | The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| carloan | deepseek | 22(ii) | MISMATCH | MISMATCH | The IRS text says 'enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F),' but the restatement computes only the QPVLI part of Schedule C interest and omits other elsewhere-deducted QPVLI such as Schedule E or Schedule F. |
| dependent | deepseek | 2(d) | MISMATCH | MISMATCH | Form 2441 line 2(d) says: 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' The helper instead says to include expenses paid with dependent care benefits, and the line does not subtract them. |
| f1040 | deepseek | 28 (box) | MISMATCH | MISMATCH | IRS says "If you do not want to claim the ACTC, check here"; the restatement fixes the box to false and never supports the opt-out. |
| f2441 | deepseek | 18 | MISMATCH | MISMATCH | The helper person.dc_earned_b removes line 1e, but the IRS says only that 'earned income doesn’t include any dependent care benefits shown on line 12'; line 1e is not line 12. |
| f2441 | deepseek | 19 | MISMATCH | MISMATCH | The spouse-earned-income helper for line 19 uses the same line-18/19 definition that removes line 1e, while the IRS excludes only dependent care benefits 'shown on line 12'. |
| f2441 | deepseek | CLW 2 | MISMATCH | MISMATCH | The IRS Credit Limit Worksheet line 2 is the amount from 'Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14)'; the restatement enters only s3 line 1 and omits line 6l. |
| f4562 | deepseek | 22 | MISMATCH | MISMATCH | The restatement omits lines 15 and 16, lines 19g through 19j, and line 20. IRS line 22 says: 'Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21.' |
| f4562 | deepseek | 26(h) | MISMATCH | MISMATCH | The helper uses asset.dep_listed, built from line 19(g) and line 17 MACRS; Part III says 'Don’t include listed property,' while line 26(h) is the Part V depreciation deduction for listed property used more than 50% in a qualified business use. |
| f4952 | deepseek | 4a | MISMATCH | MISMATCH | IRS line 4a includes ordinary dividends but 'except Alaska Permanent Fund dividends'; the restatement adds Schedule B ordinary dividends without that exception, so it can overstate line 4a. |
| f5329 | deepseek | 2 | MISMATCH | MISMATCH | The Exception 22 and 23 helpers cap only at $10,300 and $1,000, but the IRS text limits them to the lesser of $10,300 or 50% of the present value of the IRA, and the lesser of $1,000 or your total interest in the IRA minus $1,000. |
| f8863 | deepseek | 13 | MISMATCH | MISMATCH | IRS line 13 lists $180,000 for MFJ and $90,000 only for single, head of household, or qualifying surviving spouse; the restatement adds MFS $90,000. |
| f8863 | deepseek | 16 | MISMATCH | MISMATCH | IRS line 16 gives $20,000 only for MFJ and $10,000 for single/HOH/QSS, not MFS, and it is skipped when line 15 is zero or less; the restatement adds MFS and reports whenever line 10 is more than zero. |
| f8863 | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 lists $180,000 for MFJ and $90,000 only for single, head of household, or qualifying surviving spouse; adding MFS $90,000 is not supported, and MFS cannot claim an education credit. |
| f8863 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 lists $20,000 for MFJ and $10,000 only for single, head of household, or qualifying surviving spouse; the restatement adds MFS $10,000. |
| f8880 | deepseek | (CLW 2) | MISMATCH | MISMATCH | The IRS says 'Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l'; the restatement adds only s3 lines 1, 2, and 3, omitting 6d and 6l. |
| f8960 | deepseek | 5a | MISMATCH | MISMATCH | IRS line 5a instructions say to combine Form 1040 or 1040-SR line 7a with Schedule 1 (Form 1040), line 4; the restatement takes only Form 1040 line 7a. |
| f8962 | deepseek | 1 | MISMATCH | MISMATCH | The line 1 instructions say that if someone can claim you, or your spouse on a joint return, as a dependent, that person is not included in the tax family size calculation; the restatement adds the filer and spouse unconditionally. |
| f8962 | deepseek | 24 | MISMATCH | MISMATCH | The IRS applicable-taxpayer test also requires that no one can claim you as a dependent and, if married at the end of 2025, a joint return unless an exception applies; the restatement reduces it to line 5 at least 100 or the Marketplace estimate exception. |
| f8995 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 instructions say if you're not required to file Schedule D, your net capital gain is the amount on Form 1040 line 7a; the restatement uses only the smaller of Schedule D lines 15 and 16. |
| ftc | deepseek | regular_tax | MISMATCH | MISMATCH | IRS line 20 requires Form 1040 line 16 plus Schedule 2 line 1z 'less any tax included on line 16 from Form 4972' (and possible Form 8978 adjustment); the restatement only adds the two lines. |
| g28 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 asks for "the total of all collectibles gain or (loss) from items you reported on Form 8949, Part II"; the restatement instead enters $0 from the distribution scope helper, and no refusal names Form 8949 Part II collectibles as excluded. |
| g28 | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 requires the total collectibles gain or (loss) from Form 4684 line 4 (if line 15 is more than zero), Form 6252, Form 6781 Part II, and Form 8824; the restatement is merely a $0 distribution-scope helper and no refusal names those forms as excluded. |
| g28 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is "the total of any collectibles gain reported to you on: Form 1099-DIV, box 2d; Form 2439, box 1d; and Schedule K-1"; the restatement uses only Form 1099-DIV box 2d and omits the other two sources without a refusal. |
| g28 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 says to enter long-term capital loss carryovers from "Schedule D, line 14; and Schedule K-1 (Form 1041), box 11, code D"; the restatement uses only Schedule D line 14 and does not refuse or account for the K-1 amount. |
| ira | deepseek | 1a | MISMATCH | MISMATCH | IRS says if you weren't covered but your spouse was, you are considered covered unless you lived apart for all of 2025; cov_you counts only actual work or self-employed plan coverage, so the deemed-coverage case is omitted. |
| ira | deepseek | 2a | MISMATCH | MISMATCH | IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000. |
| ira | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 is the total of Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits lines 12, 14, and 23 and lists only selected lines. |
| ira | deepseek | 9 | UNCLEAR | MISMATCH | IRS line 9 includes earned income received 'as a self-employed individual or a partner'; person.ira_se is zero without a Schedule C, so partner or other self-employment income not on Schedule C is omitted, and the stated refusal covers only Schedule C income not from personal services. |
| mq | deepseek | q4 | MISMATCH | MISMATCH | The IRS test uses the total depreciable bases of MACRS property placed in service during the last 3 months, excluding nonresidential real property, residential rental property, railroad grading/tunnel bore, property placed in service and disposed of in the same year, and non-MACRS property; the helper merely adds person.mq_q4 and does not apply those exclusions or the personal-use basis reduction. |
| mq | deepseek | total | MISMATCH | MISMATCH | The IRS denominator is the total depreciable bases of all MACRS property placed in service during the entire year, with the same exclusions and personal-use reduction; the helper adds person.mq_total without those limitations. |
| qbi | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 is "Qualified business net (loss) carryforward from the prior year" shown with parentheses, and line 4 says "Combine lines 2 and 3," so the carryforward is a negative amount; the restatement instead says "entered as a positive amount." The line 3 instructions also require the "qualified portion" allowed in calculating taxable income in the current year, not merely prior-year line 16. |
| refund | deepseek | 1 | MISMATCH | MISMATCH | The restatement omits required Pub. 525 exceptions: the worksheet cannot be used if the 2025 refund is for a tax year other than 2024 or if the filer made the last 2024 estimated state or local income tax payment in 2025; the IRS says to use Itemized Deduction Recoveries instead. |
| refund | deepseek | 6 | UNCLEAR | MISMATCH | IRS line 6 says 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)' and for MFS permits spouse boxes only if the spouse had no income, isn't filing, and can't be claimed; the restatement just adds box amounts and omits the MFS spouse eligibility condition. |
| retirement | deepseek | (SMW 10) | MISMATCH | MISMATCH | IRS line 10 asks 'Was your annuity starting date before 1987?' and says 'Yes. STOP Do not complete the rest of this worksheet'; the restatement always adds lines 6 and 8. |
| retirement | deepseek | (SMW 11) | MISMATCH | MISMATCH | IRS line 10 says 'Yes. STOP Do not complete the rest of this worksheet' for an annuity starting date before 1987; the restatement always subtracts line 10 from line 2. |
| retirement | deepseek | (SMW 2) | MISMATCH | MISMATCH | The IRS before-you-begin note says 'If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below'; the restatement only enters the cost helper and omits that addition. |
| retirement | deepseek | (SMW 4) | MISMATCH | MISMATCH | IRS Table 1 distinguishes 'before November 19, 1996' from 'after November 18, 1996' and gives different numbers (for example, '55 or under' is 300 before but 360 after); the program's Table 1 helper uses only the after-November 18, 1996 values. |
| retirement | deepseek | (SMW 6) | MISMATCH | MISMATCH | IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement reports line 6 for any completed Simplified Method worksheet without this exclusion. |
| retirement | deepseek | (SMW 7) | MISMATCH | MISMATCH | IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always subtracts line 6 from line 2. |
| retirement | deepseek | (SMW 8) | MISMATCH | MISMATCH | IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement instead always takes the smaller of line 5 or line 7. |
| s1 | deepseek | 10 | MISMATCH | MISMATCH | IRS line 10 says 'Combine lines 1 through 7 and 9'; the restatement adds only lines 1, 2a, 3, 7, and 9, omitting lines 4, 5, and 6. |
| s1 | deepseek | 25 | MISMATCH | MISMATCH | IRS line 25 says 'Total other adjustments. Add lines 24a through 24z'; the restatement enters only line 24a. |
| s1 | deepseek | 26 | MISMATCH | MISMATCH | IRS line 26 says 'Add lines 11 through 23 and 25'; the restatement omits lines 12, 14, and 23. |
| s179 | deepseek | 1 | UNCLEAR | MISMATCH | Worksheet 1 says to "Enter the smaller of line 1 or line 2 here" and then "Enter the amount from line 3 here and on Form 4562, line 1"; the restatement enters only the $2,500,000 maximum. |
| s179 | deepseek | 13 | UNCLEAR | MISMATCH | The line 5 instructions say: "If line 5 is zero... enter the carryover of any disallowed deduction from 2024 ... on line 13." The restatement leaves line 10 out when line 5 is zero and then computes line 13 from lines 9 and 10 only, so it drops that carryover. |
| s1a | deepseek | 36b | MISMATCH | MISMATCH | IRS line 36b applies only 'If you are married filing jointly'; the restatement checks only that the spouse was born before January 2, 1961 and has a valid SSN. |
| s8812 | deepseek | 21 | UNCLEAR | MISMATCH | IRS line 21 calls for the Additional Medicare Tax and RRTA Tax Worksheet amount; that worksheet line 16 says 'Add lines 6, 7, 11, and 15,' but the restatement adds only lines 6 and 7, omitting the Tier 1 RRTA amounts on lines 11 and 15. |
| sa | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 says simply 'Enter amount from Form 1040 or 1040-SR, line 11b'; the program adds a 'but not less than zero' floor, which is not in the line text. |
| sales | deepseek | (e) | MISMATCH | MISMATCH | The restatement's 'Basis reported to IRS' gate is true only for classifications A or D, but the IRS form also treats boxes G and J as 'reported on Form(s) 1099-DA showing basis was reported to the IRS'; for those rows column (e) must use the reported basis, not the records basis. |
| sales | deepseek | (g) | MISMATCH | MISMATCH | IRS column (g) says 'Enter in this column any necessary adjustments to gain (or loss)' and, for multiple codes, 'enter the net adjustment in column (g)'; the restatement only adds B basis correction and W wash-sale adjustment, omitting other required adjustment codes. |
| sb | deepseek | 4 | UNCLEAR | UNCLEAR | The provided IRS text contains no line 4 instruction or statement that line 4 is line 2 minus line 3, so the arithmetic cannot be verified from the text given. |
| sc | deepseek | 9 (sc.f7206_line9) | UNCLEAR | UNCLEAR | IRS line 9 says only to enter the Schedule 1 line 16 amount 'attributable to the same trade or business'; it does not state the line 4/line 5 allocation used here. |
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
| aqee | deepseek (deepseek-flash) | 10 | 10 | 100.0% | 0/10 (0.0%) | pass | 0 | 0 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 31 | 31 | 100.0% | 0/34 (0.0%) | pass | 0 | 0 | 0 | 21 |
| clcw26 | deepseek (deepseek-flash) | 28 | 28 | 100.0% | 0/31 (0.0%) | pending | 0 | 0 | 0 | 24 |
| dependent | deepseek (deepseek-flash) | 36 | 35 | 97.2% | 0/36 (0.0%) | pass | 0 | 1 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 43 | 43 | 100.0% | 0/52 (0.0%) | pass | 0 | 0 | 0 | 61 |
| f1040 | deepseek (deepseek-flash) | 304 | 304 | 100.0% | 0/304 (0.0%) | pending | 0 | 0 | 0 | 8 |
| f1095a | deepseek (deepseek-flash) | 66 | 65 | 98.5% | 1/66 (1.5%) | pass | 0 | 1 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 138 | 138 | 100.0% | 0/165 (0.0%) | pending | 0 | 0 | 0 | 66 |
| f4952 | deepseek (deepseek-flash) | 52 | 52 | 100.0% | 0/52 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f5329 | deepseek (deepseek-flash) | 21 | 21 | 100.0% | 0/21 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 322 | 321 | 99.7% | 1/342 (0.3%) | pending | 1 | 0 | 0 | 222 |
| f8863 | deepseek (deepseek-flash) | 52 | 52 | 100.0% | 0/66 (0.0%) | pending | 0 | 0 | 0 | 48 |
| f8880 | deepseek (deepseek-flash) | 45 | 45 | 100.0% | 0/48 (0.0%) | pending | 0 | 0 | 0 | 39 |
| f8889 | deepseek (deepseek-flash) | 135 | 132 | 97.8% | 0/135 (0.0%) | pass | 0 | 3 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 50 | 50 | 100.0% | 0/50 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 394 | 360 | 91.4% | 0/394 (0.0%) | pending | 34 | 0 | 0 | 176 |
| g28 | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pending | 0 | 0 | 0 | 11 |
| person | deepseek (deepseek-flash) | 15 | 14 | 93.3% | 1/15 (6.7%) | pass | 0 | 1 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 50 | 50 | 100.0% | 0/50 (0.0%) | pass | 0 | 0 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 36 | 36 | 100.0% | 0/36 (0.0%) | pass | 0 | 0 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 40 | 40 | 100.0% | 0/40 (0.0%) | pass | 0 | 0 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 129 | 129 | 100.0% | 0/129 (0.0%) | pass | 0 | 0 | 0 | 71 |
| sd | deepseek (deepseek-flash) | 41 | 41 | 100.0% | 0/41 (0.0%) | pending | 0 | 0 | 0 | 97 |
| u1250 | deepseek (deepseek-flash) | 18 | 18 | 100.0% | 0/18 (0.0%) | pass | 0 | 0 | 0 | 18 |
| w2 | deepseek (deepseek-flash) | 39 | 39 | 100.0% | 0/39 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 2098 | 2057 | 98.0% | | | 35 | 6 | 0 | 862 |

Pending clcw26 [deepseek]: 5 missing expected lines.
Pending f1040 [deepseek]: 7 missing expected lines.
Pending f2441 [deepseek]: 2 missing expected lines.
Pending f5695 [deepseek]: 4 missing expected lines.
Pending f8863 [deepseek]: 7 missing expected lines.
Pending f8880 [deepseek]: 3 missing expected lines.
Pending f8962 [deepseek]: 34 open, unclassified or interface-gap rulings.
Pending g28 [deepseek]: 11 missing expected lines.
Pending sd [deepseek]: 32 missing expected lines.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| f5695 | deepseek | classm.f5695.16 — 14 | DISAGREE | model gave $0.00; work: Limit worksheet: 7,955 - (600 + 7,355) = 0.00 |
| f8962 | deepseek | classm.f8962.6 — 12(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 12(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 12(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 13(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 13(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 13(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 14(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 14(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 14(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 15(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 15(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 15(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 16(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 16(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 16(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 17(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 17(d) | DISAGREE | model gave $692.00; work: 1,112 - 420 = 692 |
| f8962 | deepseek | classm.f8962.6 — 17(e) | DISAGREE | model gave $692.00; work: smaller of 802 and 692 = 692 |
| f8962 | deepseek | classm.f8962.6 — 18(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 18(d) | DISAGREE | model gave $672.00; work: 1,092 - 420 = 672 |
| f8962 | deepseek | classm.f8962.6 — 19(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 19(d) | DISAGREE | model gave $672.00; work: 1,092 - 420 = 672 |
| f8962 | deepseek | classm.f8962.6 — 20(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 20(d) | DISAGREE | model gave $672.00; work: 1,092 - 420 = 672 |
| f8962 | deepseek | classm.f8962.6 — 21(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 21(d) | DISAGREE | model gave $672.00; work: 1,092 - 420 = 672 |
| f8962 | deepseek | classm.f8962.6 — 22(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 23(c) | DISAGREE | model gave $420.00; work: Monthly contribution = line 8b = 420 |
| f8962 | deepseek | classm.f8962.6 — 24 | DISAGREE | model gave $5,560.00; work: 692 x 6 + 352 x 4 + 0 = 5,560 |
| f8962 | deepseek | classm.f8962.6 — 27 | DISAGREE | model gave $265.00; work: 5,825 - 5,560 = 265 |
| f8962 | deepseek | classm.f8962.6 — 29 | DISAGREE | model gave $265.00; work: smaller of 265 and 3,250 = 265 |
| f8962 | deepseek | classm.f8962.6 — 7 | DISAGREE | model gave 6.275%; work: 6.000% + 11 x 0.025% = 6.275% = 0.06275 |
| f8962 | deepseek | classm.f8962.6 — 8a | DISAGREE | model gave $5,043.00; work: 80,369 x 0.06275 = 5,043.15475; nearest dollar = 5,043 |
| f8962 | deepseek | classm.f8962.6 — 8b | DISAGREE | model gave $420.00; work: 5,043 / 12 = 420.25; nearest dollar = 420 |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| dependent | deepseek | classm.dependent.5 — dependent[dep_b].dc_line2d | DISAGREE | DISAGREE | model gave $0.00; work: Not a Form 2441 qualifying person: age 25 and not disabled; allowable expenses = $0.00 |
| f1095a | deepseek | classm.f1095a.1 — f1095a[mkt_b].line33c | DISAGREE | DISAGREE | model gave $2,042.00; work: Line 33 column C as given |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line12 | DISAGREE | DISAGREE | model gave $5,031.25; work: Line 8 minus line 11: 5,031.25 - 0.00 = 5,031.25. |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line7 | DISAGREE | DISAGREE | model gave $750.00; work: Age 55+, married, family coverage 9 months: 1,000 x 9/12 = 750.00. |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line8 | DISAGREE | DISAGREE | model gave $5,031.25; work: Line 6 plus line 7: 4,281.25 + 750.00 = 5,031.25. |
| person | deepseek | classm.person.1 — person[taxpayer].wages | DISAGREE | DISAGREE | model gave $29,524.00; work: W-2 box 1 totals: 29,524.00 + 0.00. |
