# Second-family review comparison — 2025

Summary: 140 form-kind pair(s) with logs from Claude and deepseek, gpt; ruled model-error noise 8.1% (337/4164 second-family lines judged; pending reviews are provisional); 64 eligible, 76 pending; raw agreement 80.7% (diagnostic only); current independence yield 161 line(s); both families disputed 579

Written by `tools/transcription/compare_families.py` on 2026-11-04 from the review logs under `reviews/2025/`. For each form with a Claude log and a second model family's log of the same kind (`<form>.<family>.md`, families.py), the lines judged in both are compared.

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
| aqee | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pending | 0 | 0 | 0 | 0 |
| carloan | deepseek (deepseek-flash) | 2 | 0 | 0.0% | 2/2 (100.0%) | pending | 0 | 2 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pending | 0 | 0 | 0 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 1/13 (7.7%) | pending | 1 | 0 | 0 | 0 |
| dcprov | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pending | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 22 | 1 | 4.5% | 17/22 (77.3%) | pending | 2 | 17 | 2 | 0 |
| div | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 18 | 1 | 5.6% | 13/18 (72.2%) | pending | 1 | 16 | 0 | 1 |
| eic | gpt (gpt-6-astra) | 19 | 2 | 10.5% | 14/19 (73.7%) | pending | 0 | 17 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 52 | 39 | 75.0% | 11/52 (21.2%) | pending | 8 | 5 | 0 | 0 |
| f1095a | deepseek (deepseek-flash) | 29 | 1 | 3.4% | 15/29 (51.7%) | pending | 13 | 15 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 34 | 7 | 20.6% | 23/34 (67.6%) | pending | 19 | 7 | 1 | 3 |
| f2441 | gpt (gpt-6-astra) | 37 | 25 | 67.6% | 8/37 (21.6%) | pending | 4 | 8 | 0 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 1 | 6.7% | 0/15 (0.0%) | pending | 0 | 14 | 0 | 0 |
| f5329 | deepseek (deepseek-flash) | 10 | 2 | 20.0% | 5/10 (50.0%) | pending | 0 | 8 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 33 | 6 | 18.2% | 23/33 (69.7%) | pending | 0 | 24 | 3 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 2 | 40.0% | 0/5 (0.0%) | pending | 0 | 3 | 0 | 0 |
| f8863 | deepseek (deepseek-flash) | 28 | 1 | 3.6% | 22/28 (78.6%) | pending | 0 | 27 | 0 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 6 | 28.6% | 15/21 (71.4%) | pending | 7 | 8 | 0 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 22 | 91.7% | 0/24 (0.0%) | pending | 0 | 2 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 97 | 0 | 0.0% | 3/97 (3.1%) | pending | 0 | 95 | 2 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 7 | 43.8% | 0/16 (0.0%) | pending | 4 | 5 | 0 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 2 | 14.3% | 9/14 (64.3%) | pending | 7 | 5 | 0 | 0 |
| ftc | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 0 | 0.0% | 4/7 (57.1%) | pending | 0 | 7 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 19 | 5 | 26.3% | 11/19 (57.9%) | pending | 2 | 10 | 2 | 0 |
| interest | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 29 | 6 | 20.7% | 16/29 (55.2%) | pending | 0 | 22 | 1 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| mq | gpt (gpt-6-astra) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pending | 0 | 0 | 0 | 0 |
| qbi | deepseek (deepseek-flash) | 5 | 1 | 20.0% | 0/5 (0.0%) | pending | 2 | 2 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 26 | 23 | 88.5% | 0/26 (0.0%) | pending | 0 | 3 | 0 | 0 |
| refund | deepseek (deepseek-flash) | 11 | 3 | 27.3% | 5/11 (45.5%) | pending | 4 | 4 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 14 | 10 | 71.4% | 2/14 (14.3%) | pending | 1 | 2 | 1 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 8 | 18.6% | 34/43 (79.1%) | pending | 1 | 34 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 13 | 8 | 61.5% | 4/13 (30.8%) | pending | 4 | 1 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 51 | 12 | 23.5% | 32/51 (62.7%) | pending | 1 | 38 | 0 | 0 |
| sa | deepseek (deepseek-flash) | 22 | 16 | 72.7% | 4/22 (18.2%) | pending | 2 | 4 | 0 | 0 |
| sales | deepseek (deepseek-flash) | 4 | 2 | 50.0% | 0/4 (0.0%) | pending | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pending | 0 | 0 | 0 | 0 |
| scope | deepseek (deepseek-flash) | 0 | 0 | n/a | 0/0 (n/a) | pending | 0 | 0 | 0 | 0 |
| sd | deepseek (deepseek-flash) | 55 | 9 | 16.4% | 7/55 (12.7%) | pending | 7 | 37 | 2 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 20 | 42.6% | 12/47 (25.5%) | pending | 2 | 19 | 6 | 0 |
| se | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 19 | 5 | 26.3% | 3/19 (15.8%) | pending | 1 | 12 | 1 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 0/1 (0.0%) | pending | 0 | 1 | 0 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 0 | 0.0% | 7/18 (38.9%) | pending | 0 | 18 | 0 | 0 |
| w2 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 0 | 1 | 1 | 0 |
| **all** | | 909 | 294 | 32.3% | | | 93 | 500 | 22 | 4 |

Pending aqee [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending carloan [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending clcw [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending clcw26 [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending dcprov [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending dependent [deepseek]: model-error noise above 10%; no passing current source-based partial-input checks: deepseek.
Excluded internal adapters for div: div.screen. Original logs/rulings are preserved; separate engineering checks earn no independent tax-evidence credit.
Pending div [deepseek]: stale subject: claude, deepseek; no source-defined computed targets; internal adapter checks earn no tax-evidence credit; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending eic [deepseek]: 1 missing expected lines; model-error noise above 10%; current source targets not judged by claude: eic.zero; current source targets not judged by deepseek: eic.zero; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending eic [gpt]: model-error noise above 10%; current source targets not judged by claude: eic.zero; current source targets not judged by gpt: eic.zero; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for gpt: required input/interface wording is missing or stale.
Pending f1040 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f1095a [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f2441 [deepseek]: 3 missing expected lines; model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f2441 [gpt]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for gpt: required input/interface wording is missing or stale.
Pending f4562 [deepseek]: 14 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f5329 [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f5695 [deepseek]: model-error noise above 10%.
Pending f8606 [deepseek]: 3 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8863 [deepseek]: 3 open, unclassified or interface-gap rulings; model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for deepseek: current expression/refusal validation fails.
Pending f8880 [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f8959 [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8962 [deepseek]: 89 open, unclassified or interface-gap rulings; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending f8995 [deepseek]: 9 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending f8995a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending ftc [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending g28 [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending gift [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending household [deepseek]: model-error noise above 10%.
Pending interest [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ira [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending mq [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending mq [gpt]: no verified current request context for claude: saved prompt differs from the original log receipt.
Pending oi8z [deepseek]: transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending qbi [deepseek]: 4 open, unclassified or interface-gap rulings; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending qdcg [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending refund [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending s179 [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending s1a [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending s2 [deepseek]: 1 open, unclassified or interface-gap rulings; model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending s8812 [deepseek]: model-error noise above 10%; no passing current expression type validation: claude, deepseek; no verified current request context for claude: current expression/refusal validation fails; no verified current request context for deepseek: current expression/refusal validation fails.
Pending sa [deepseek]: 1 open, unclassified or interface-gap rulings; model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending sales [deepseek]: no verified current request context for claude: required input/interface wording is missing or stale; no verified current request context for deepseek: required input/interface wording is missing or stale.
Pending sb [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending scope [deepseek]: stale subject: claude, deepseek; no verified current request context for claude: log subject no longer matches the project definition; no verified current request context for deepseek: log subject no longer matches the project definition.
Pending sd [deepseek]: model-error noise above 10%; no passing current expression type validation: deepseek; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending sdtw [deepseek]: model-error noise above 10%; no passing current expression type validation: claude; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending se [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending ssb [deepseek]: model-error noise above 10%.
Pending tax_on_amount [deepseek]: no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.
Pending tcw [deepseek]: no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending u1250 [deepseek]: model-error noise above 10%; no verified current request context for claude: saved prompt differs from the original log receipt; no verified current request context for deepseek: saved prompt differs from the original log receipt.
Pending w2 [deepseek]: stale subject: claude, deepseek; transcription predates unit-preserving comparison; verified re-comparison required: claude, deepseek; no passing current expression type validation: claude, deepseek; no verified complete input context in the request: claude, deepseek.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| clcw26 | deepseek | 3 | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_child | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.eic_ssn_child | DISAGREE | (no reason given) |
| eic | deepseek | eic.self_employed | DISAGREE | Uses the available Schedule C aggregate. No separate self-employment/Schedule SE screening input is in the closed interface. |
| f1040 | deepseek | 19 | DISAGREE | (no reason given) |
| f1040 | deepseek | 1a | DISAGREE | (no reason given) |
| f1040 | deepseek | 25a | DISAGREE | (no reason given) |
| f1040 | deepseek | 25c | DISAGREE | (no reason given) |
| f1040 | deepseek | 2a | DISAGREE | (no reason given) |
| f1040 | deepseek | 2b | DISAGREE | (no reason given) |
| f1040 | deepseek | 3b | DISAGREE | (no reason given) |
| f1040 | deepseek | 6d | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_apr | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_aug | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_dec | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_feb | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_jan | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_jul | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_jun | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_mar | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_may | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_nov | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_oct | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.a_sep | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.line33c | DISAGREE | (no reason given) |
| f2441 | deepseek | 10 | DISAGREE | The supplied catalog has no Schedule 3 line 6l or Form 8978 amount; only Schedule 3 line 1 is subtracted. |
| f2441 | deepseek | 11 | DISAGREE | (no reason given) |
| f2441 | deepseek | 12 | DISAGREE | Only Form W-2 box 10 benefits are computed; sole-proprietorship or partnership benefits are refused through scope.other_income. |
| f2441 | deepseek | 15 | DISAGREE | (no reason given) |
| f2441 | deepseek | 17 | DISAGREE | (no reason given) |
| f2441 | deepseek | 19 | DISAGREE | For married filing separately the expression treats the filer as required to enter the spouse's earned income; the considered-unmarried checkbox is not in the interface. |
| f2441 | deepseek | 20 | DISAGREE | (no reason given) |
| f2441 | deepseek | 21 | DISAGREE | Married filing separately uses the $2,500 base; the considered-unmarried case using $5,000 is not distinguished in the supplied interface. |
| f2441 | deepseek | 23 | DISAGREE | (no reason given) |
| f2441 | deepseek | 24 | DISAGREE | (no reason given) |
| f2441 | deepseek | 26 | DISAGREE | (no reason given) |
| f2441 | deepseek | 28 | DISAGREE | (no reason given) |
| f2441 | deepseek | 29 | DISAGREE | (no reason given) |
| f2441 | deepseek | 30 | DISAGREE | (no reason given) |
| f2441 | deepseek | 31 | DISAGREE | (no reason given) |
| f2441 | deepseek | 6 | DISAGREE | (no reason given) |
| f2441 | deepseek | 9a | DISAGREE | (no reason given) |
| f2441 | deepseek | 9c | DISAGREE | (no reason given) |
| f2441 | deepseek | f2441.one_box10 | DISAGREE | The interface name is not defined by the IRS pages; read here as exactly one Form W-2 entry with box 10 benefits. |
| f2441 | gpt | 11 | DISAGREE | (no reason given) |
| f2441 | gpt | 21 | DISAGREE | The printed form conditions the $2,500 limit on the line 19 spouse-income requirement; the instructions state it for married filing separately generally. This transcription follows the printed form’s explicit condition. |
| f2441 | gpt | 30 | DISAGREE | The closed interface supplies expenses before excluding benefits. The exclusion is subtracted once from the aggregate; no allocation among qualifying persons is inferred. |
| f2441 | gpt | 31 | DISAGREE | (no reason given) |
| f8880 | deepseek | 10 | DISAGREE | (no reason given) |
| f8880 | deepseek | 2(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 3(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 3(b) | DISAGREE | (no reason given) |
| f8880 | deepseek | 5(a) | DISAGREE | (no reason given) |
| f8880 | deepseek | 5(b) | DISAGREE | (no reason given) |
| f8880 | deepseek | 7 | DISAGREE | (no reason given) |
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
| household | deepseek | household.cp_marriage_ended | DISAGREE | (no reason given) |
| household | deepseek | household.qss_fails | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.eligible | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.net_capital_gain | DISAGREE | (no reason given) |
| refund | deepseek | 1 | DISAGREE | The instructions’ tip says none of the refund is taxable if you didn’t itemize or elected sales taxes. I set the worksheet lines to zero in that case rather than using line 5d. |
| refund | deepseek | 2 | DISAGREE | When 2024 Schedule A line 5d is not more than line 5e, the worksheet does not enter line 2 and sends line 1 to line 3; I use zero on line 2 so line 3 equals line 1. |
| refund | deepseek | 4 | DISAGREE | (no reason given) |
| refund | deepseek | refund.has | DISAGREE | (no reason given) |
| s179 | deepseek | s179.differs | DISAGREE | The IRS pages do not name this interface. Read here as whether the business income limitation reduces the deduction below the sum of lines 9 and 10, i.e. whether a carryover arises. |
| s1a | deepseek | 38 | DISAGREE | (no reason given) |
| s2 | deepseek | 11 | DISAGREE | (no reason given) |
| s2 | deepseek | 21 | DISAGREE | Only the computed Part II amounts are summed; other Part II amounts are outside scope and covered by s2.other. |
| s2 | deepseek | 4 | DISAGREE | (no reason given) |
| s2 | deepseek | 8 (box) | DISAGREE | (no reason given) |
| s8812 | deepseek | s8812.clwb_complete | DISAGREE | (no reason given) |
| sa | deepseek | 5e | DISAGREE | The SALT worksheet is applied as printed: the $40,000 base and $10,000 floor are halved for married filing separately at the final step. |
| sa | deepseek | 9 | DISAGREE | (no reason given) |
| sd | deepseek | 11 | DISAGREE | (no reason given) |
| sd | deepseek | 12 | DISAGREE | (no reason given) |
| sd | deepseek | 21 | DISAGREE | (no reason given) |
| sd | deepseek | 4 | DISAGREE | (no reason given) |
| sd | deepseek | 5 | DISAGREE | (no reason given) |
| sd | deepseek | sd.line18 | DISAGREE | No 28% Rate Gain Worksheet fields are supplied; this line is zero when no collectibles or other unsupported special gain is present, and refuses otherwise. |
| sd | deepseek | sd.line19 | DISAGREE | (no reason given) |
| sdtw | deepseek | 30 | DISAGREE | (no reason given) |
| sdtw | deepseek | 33 | DISAGREE | (no reason given) |
| ssb | deepseek | ssb.has_benefits | DISAGREE | (no reason given) |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| carloan | deepseek | 22(ii) | DISAGREE | DISAGREE | (no reason given) |
| carloan | deepseek | 22(iii) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 2(c) | DISAGREE | DISAGREE | For a person age 13 at the end of 2025, the checkbox depends on whether any care was provided after age 12; when dc_over12_care is not answered the result is unknown. |
| dependent | deepseek | 2(d) | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 28 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 30 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | 31 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.actc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.claimed | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.ctc_child | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.dc_qp | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_absence | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test1 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.hoh_test2 | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_amount | DISAGREE | DISAGREE | (no reason given) |
| dependent | deepseek | dependent.odc_person | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | (Step 5, 1) | DISAGREE | DISAGREE | The clergy/church-employee adjustment to line 1 is not supported by the closed input interface; line 1z is used directly. |
| eic | deepseek | (Step 5, 2) | DISAGREE | DISAGREE | No Medicaid waiver payment amount is in the closed input interface; within the supplied scope this amount is zero. |
| eic | deepseek | (Step 5, 3) | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | (Step 5, 4) | DISAGREE | DISAGREE | No nontaxable combat pay amount is in the closed input interface; within the supplied scope this amount is zero. |
| eic | deepseek | (Step 5, 5) | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 4b | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| eic | deepseek | 6 (eic.wsb_6) | DISAGREE | DISAGREE | Floored at zero. The IRS STOP for line 4b zero or less is carried into the credit eligibility gate. |
| eic | deepseek | eic.check_27c | DISAGREE | DISAGREE | The voluntary election not to claim the EIC is not supplied by the closed interface; this records only the ineligible STOP cases. |
| eic | deepseek | eic.clergy | DISAGREE | DISAGREE | No supplied input distinguishes clergy or church employees. Within the closed input interface this is set false rather than inventing an input. |
| eic | deepseek | eic.credit | DISAGREE | DISAGREE | All STOP conditions are carried to this result as zero. Worksheet B is used when the available self-employment aggregate requires it. |
| eic | deepseek | eic.eligible | DISAGREE | DISAGREE | The Step 2 investment-income branch for Form 4797 filers is not separately supported; investment income over the limit is treated as ineligible. Nonresident-alien status is not separately supplied. |
| eic | deepseek | eic.separated_box | DISAGREE | DISAGREE | Uses the main-home input as the available reading of the requirement that the qualifying child lived in the United States for more than half of 2025. |
| eic | gpt | (Step 5, 1) | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | (Step 5, 2) | DISAGREE | DISAGREE | Medicaid waiver payments are excluded by the supplied scope screens. |
| eic | gpt | (Step 5, 3) | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | (Step 5, 4) | DISAGREE | DISAGREE | Combat pay is outside the supplied screening scope; no election or amount is invented. |
| eic | gpt | (Step 5, 5) | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | 1 | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | 2 | DISAGREE | DISAGREE | The printed table starts at $1 and gives no row for smaller amounts. This transcription uses zero below that first row; no positive credit is inferred there. |
| eic | gpt | 3 | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | 4b | DISAGREE | DISAGREE | The published per-person eic_se interface supplies the applicable Part 1 or Part 2 amount. Statutory employees, farm and partnership income, clergy, church employee income, and other exempt or special self-employment cases are excluded by the supplied screens. |
| eic | gpt | 5 | DISAGREE | DISAGREE | The hidden zero is a representation of a skipped blank, not a credit used in the minimum. |
| eic | gpt | 6 (eic.line6) | DISAGREE | DISAGREE | (no reason given) |
| eic | gpt | 6 (eic.wsb_6) | DISAGREE | DISAGREE | Zero represents the no-credit STOP before line 6; on the continuing branch the positive line 4b amount is preserved. |
| eic | gpt | eic.check_27c | DISAGREE | DISAGREE | Only instructed checks within the screened scope are computed. A voluntary decision not to claim the credit cannot be determined from the closed input interface. A zero resulting only from the later AGI comparison does not itself instruct a check. |
| eic | gpt | eic.clergy | DISAGREE | DISAGREE | Clergy and church employee cases are screened out; the supported case has no line 27b check. |
| eic | gpt | eic.credit | DISAGREE | DISAGREE | The closed interface provides no election to decline the credit or have the IRS figure it. This computes the credit for a filer claiming it. |
| eic | gpt | eic.eligible | DISAGREE | DISAGREE | True means the applicable eligibility flow reaches the credit lookup; the lookup may still produce zero. |
| eic | gpt | eic.separated_box | DISAGREE | DISAGREE | The specific definition on page 44 limits this checkbox to married filers not filing jointly; the broader placement of the checkbox instruction in Step 3 question 6 is read in that context. |
| f1040 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 1e | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 28 (box) | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| f1040 | deepseek | 6c | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_apr | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_aug | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_dec | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_feb | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jan | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jul | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_jun | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_mar | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_may | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_nov | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_oct | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_sep | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.b_used | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.line33a | DISAGREE | DISAGREE | (no reason given) |
| f1095a | deepseek | f1095a.line33b | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 1 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 2 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | deepseek | f2441.has_1e | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 1 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 16 | DISAGREE | DISAGREE | The supplied expense inputs exclude employer-furnished care and collectively include incurred expenses regardless of payment date. No additional employer-furnished-care expense is inferred. |
| f2441 | gpt | 2 (box) | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 25 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 27 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 3 | DISAGREE | DISAGREE | (no reason given) |
| f2441 | gpt | 5 | DISAGREE | DISAGREE | Publication 503 page 11 permits a surviving spouse filing jointly to omit the deceased spouse’s earned income. This transcription chooses that permitted treatment. |
| f2441 | gpt | f2441.has_1e | DISAGREE | DISAGREE | (no reason given) |
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
| f5329 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| f5329 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| f5329 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f5329 | deepseek | 4 | DISAGREE | DISAGREE | The SIMPLE IRA portion included in lines 1 and 2 is read from person.x_l1_s and person.x_l2_s and taxed at 25% per the line 4 caution; the rest of line 3 is taxed at 10%. |
| f5329 | deepseek | 47 | DISAGREE | DISAGREE | Reads the person-level helper person.x_hsa_excess as the 2025 excess HSA contribution amount; prior-year excess contributions are outside this slice. |
| f5329 | deepseek | 48 | DISAGREE | DISAGREE | Assumes line 46 is zero because a prior-year excess HSA contribution on 2024 Form 5329 line 48 is screened by person.x_other. |
| f5329 | deepseek | 49 | DISAGREE | DISAGREE | (no reason given) |
| f5329 | deepseek | f5329.must | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 11 | DISAGREE | DISAGREE | Fuel cell property is not computed; a Yes answer to line 7a refuses. When line 7a is No, lines 7b through 11 are skipped and line 11 is zero. |
| f5695 | deepseek | 14 | DISAGREE | DISAGREE | Uses Form 1040 line 19 for the child tax credit or credit for other dependents; the Schedule 8812 Credit Limit Worksheet B alternative is not modeled. |
| f5695 | deepseek | 18b | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19f | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19g | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 19h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 20c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 20d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 22c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 22d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 23c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 23d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 24c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 24d | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 25e | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 26c | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 29g | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 29h | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 32 | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 32a | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 32b | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | 5b | DISAGREE | DISAGREE | (no reason given) |
| f5695 | deepseek | f5695.claiming_part1 | DISAGREE | DISAGREE | The IRS text does not define this result interface; read as true when the Part I credit on line 15 is positive. |
| f8606 | deepseek | 1 | DISAGREE | DISAGREE | The IRS worksheet permits line 1 to be figured through the IRA Deduction Worksheet or the Pub. 590-A reduced-deduction worksheet; with no additional input interface, this slice takes line 1 as the supplied nondeductible contribution amount. |
| f8606 | deepseek | 2 | DISAGREE | DISAGREE | The IRS instructions allow line 2 to be adjusted for return of excess contributions, divorce transfers, and rollovers of nontaxable plan amounts; this closed slice takes line 2 as the supplied total basis. |
| f8606 | deepseek | 3 (question) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 1) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 2) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 3) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 4) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 5) | DISAGREE | DISAGREE | Schedule 3 lines 6d and 6l are not supplied in the interface; this line sums the available Schedule 3 lines 1 and 2 only. |
| f8863 | deepseek | (CLW 6) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | (CLW 7) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 1 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 11 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 14 | DISAGREE | DISAGREE | Uses Form 1040 line 11b; excluded income under Form 2555 or 4563 or Puerto Rico is outside this slice. |
| f8863 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 18 | DISAGREE | DISAGREE | Line 17 is not separately transcribed; the prorate atom folds its ratio (line 15 divided by line 16, capped at 1 and rounded to three decimal places) into this line. |
| f8863 | deepseek | 19 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 2 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 3 | DISAGREE | DISAGREE | Uses Form 1040 line 11b; excluded income under Form 2555 or 4563 or Puerto Rico is outside this slice. |
| f8863 | deepseek | 4 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 7 | DISAGREE | DISAGREE | Line 6 is not separately transcribed; the prorate atom folds its ratio (line 4 divided by line 5, capped at 1 and rounded to three decimal places) into this line. |
| f8863 | deepseek | 7 (box) | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| f8863 | deepseek | f8863.eligible | DISAGREE | DISAGREE | Project interface; defined as paid education expenses, positive MAGI room on line 4, and not married filing separately. Other eligibility conditions such as being claimed as a dependent, nonresident alien status, or a student TIN are outside the supplied inputs. |
| f8863 | deepseek | f8863.kid_needed | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 1(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 1(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 2(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(a) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 4(b) | DISAGREE | DISAGREE | (no reason given) |
| f8880 | deepseek | 6(a) | DISAGREE | DISAGREE | The Form 8880 caution makes the credit unavailable for a person born after January 1, 2008, claimed as a dependent, or a student. When the taxpayer is ineligible under person.sav_ineligible, column (a) is zero; otherwise it is the smaller of line 5(a) and $2,000. |
| f8880 | deepseek | 6(b) | DISAGREE | DISAGREE | The Form 8880 caution makes the credit unavailable for a person born after January 1, 2008, claimed as a dependent, or a student. When the spouse is ineligible under person.sav_ineligible, column (b) is zero; otherwise it is the smaller of line 5(b) and $2,000. |
| f8959 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| f8959 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 1 | DISAGREE | DISAGREE | Counts taxpayer/spouse person entries plus dependents claimed; the supplied interface has no separate flag excluding only a taxpayer or spouse who can be claimed as another person’s dependent, so sa.dependent refuses the line when it applies. |
| f8962 | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(a) | DISAGREE | DISAGREE | The supplied Form 1095-A premium inputs are treated as already net of any premiums refunded in 2025; f8962.premium_adjust is used to select the monthly calculation when coverage began after the first day of a month. |
| f8962 | deepseek | 11(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 11(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 12(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 13(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 14(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 15(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 16(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 17(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 18(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 19(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 20(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 21(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 22(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(a) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(b) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(c) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(d) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(e) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 23(f) | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 28 | DISAGREE | DISAGREE | Line 28 is blank when line 5 is 400 or more; that blank is represented as zero here and line 29 ignores it in that case. |
| f8962 | deepseek | 29 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 2a | DISAGREE | DISAGREE | Form 2555 lines 45 and 50 are not in the supplied interface; returns with Form 2555, Form 4563 or Puerto Rico exclusion are refused through sa.excluded_income. |
| f8962 | deepseek | 2b | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 4 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 8a | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 8b | DISAGREE | DISAGREE | (no reason given) |
| f8962 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
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
| g28 | deepseek | 1 | DISAGREE | DISAGREE | Distribution-only path: this slice does not handle Form 8949 Part II collectibles, so line 1 is zero. |
| g28 | deepseek | 2 | DISAGREE | DISAGREE | Distribution-only path: no Form 8949 Part II section 1202 exclusion is represented, so line 2 is zero. |
| g28 | deepseek | 3 | DISAGREE | DISAGREE | Distribution-only path: no Form 4684, Form 6252, Form 6781 or Form 8824 collectibles gain is represented, so line 3 is zero. |
| g28 | deepseek | 4 | DISAGREE | DISAGREE | Only Form 1099-DIV box 2d is represented by a supplied line; Form 2439 box 1d and Schedule K-1 collectibles gain are not represented and are treated as absent. |
| g28 | deepseek | 5 | DISAGREE | DISAGREE | Only the Schedule D, line 14 carryover is represented by a supplied line; the Schedule K-1 (Form 1041), box 11, code D amount is not represented and is treated as absent. |
| g28 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| g28 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.all_eic_ssn | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.all_tin | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.ctc_disallowed_claim | DISAGREE | DISAGREE | The supplied credit_disallowed question combines EIC and CTC/ACTC/ODC disallowance; without separate inputs this is treated as a CTC disallowance when true. |
| household | deepseek | household.ctc_ssn | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.eic_disallowed_claim | DISAGREE | DISAGREE | The supplied credit_disallowed question combines EIC and CTC/ACTC/ODC disallowance; without separate inputs this is treated as an EIC disallowance when true. |
| household | deepseek | household.filing_status_conflict | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.hoh_fails | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.rdp_community_property | DISAGREE | DISAGREE | (no reason given) |
| household | deepseek | household.roster_bad | DISAGREE | DISAGREE | Reads the person roster as valid when there is exactly one taxpayer and a spouse entry only on a joint return. |
| household | deepseek | household.widowed_2025 | DISAGREE | DISAGREE | (no reason given) |
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
| mq | deepseek | mq.applies | DISAGREE | DISAGREE | (no reason given) |
| mq | gpt | mq.applies | DISAGREE | DISAGREE | Applies to the supported property for which the mid-month convention does not apply. The comparison is strictly more than 40%; equality, including zero total basis, yields false. |
| qbi | deepseek | qbi.deduction | DISAGREE | DISAGREE | (no reason given) |
| qbi | deepseek | qbi.taxable_before | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| qdcg | deepseek | 3 | DISAGREE | DISAGREE | Blank Schedule D lines are not representable; if either line is supplied as a loss, the amount is zero. |
| qdcg | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 8 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| refund | deepseek | refund.taxable | DISAGREE | DISAGREE | (no reason given) |
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
| s8812 | deepseek | (CLW A 1) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW A 2) | DISAGREE | DISAGREE | The supplied catalog has Schedule 3 lines 1, 2, 3, 4, and 5b but not lines 6d, 6f, 6l, or 6m. Those unavailable entries are not included. |
| s8812 | deepseek | (CLW A 3) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW A 4) | DISAGREE | DISAGREE | The condition for completing Credit Limit Worksheet B is inferred from the supplied credit flag for the residential clean energy credit, the absence of a Form 2555 amount, and line 4 being greater than zero; mortgage interest, adoption, and D.C. first-time homebuyer credit flags are not in the supplied interface. |
| s8812 | deepseek | (CLW A 5) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 1) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 10) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 11) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 12) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 13) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 14) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 15) | DISAGREE | DISAGREE | The supplied catalog provides Schedule 3 line 5a but not lines 6c, 6g, or 6h. Only the available line 5a amount is included. |
| s8812 | deepseek | (CLW B 2) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 3) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 4) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 5) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 7) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 8) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | (CLW B 9) | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 16a | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 16b | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 18a | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 18b | DISAGREE | DISAGREE | The closed input interface supplies only a yes/no combat pay screen, not the combat pay amount. The line is zero when the screen is false and refuses when the screen is true. |
| s8812 | deepseek | 19 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 20 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 21 | DISAGREE | DISAGREE | The supplied catalog exposes the nested W-2 box 4 and box 6 entry fields, which are summed. The Additional Medicare Tax and RRTA Tax Worksheet is outside the supplied interface and is not computed. |
| s8812 | deepseek | 22 | DISAGREE | DISAGREE | The supplied catalog provides Schedule 1 line 15 but not Schedule 2 lines 5, 6, or 13. Only the available Schedule 1 line 15 amount is included. |
| s8812 | deepseek | 23 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 24 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 25 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 26 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 27 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 5 | DISAGREE | DISAGREE | (no reason given) |
| s8812 | deepseek | 7 | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | sa.age65 | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | sa.deduction | DISAGREE | DISAGREE | (no reason given) |
| sa | deepseek | sa.itemizes | DISAGREE | DISAGREE | (no reason given) |
| sales | deepseek | (e) | DISAGREE | DISAGREE | (no reason given) |
| sales | deepseek | (g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(d) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(e) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(g) | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | 10(h) | DISAGREE | DISAGREE | (no reason given) |
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
| sd | deepseek | sd.filed | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | sd.investment_election | DISAGREE | DISAGREE | (no reason given) |
| sd | deepseek | sd.net_gain | DISAGREE | DISAGREE | (no reason given) |
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
| ssb | deepseek | 10 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 11 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 12 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 14 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 16 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| ssb | deepseek | 18 | DISAGREE | DISAGREE | The worksheet is not used when the line 6a/6b exception applies (ssb.pub915); if the taxpayer elects the lump-sum method (ssb.lump_sum), the taxable amount may be reduced by Pub. 915 and is outside this worksheet's arithmetic. |
| ssb | deepseek | 6 | DISAGREE | DISAGREE | Schedule 1 line 23 is named by the worksheet but is not in the supplied catalog; this line sums the named Schedule 1 adjustment lines that are present. |
| ssb | deepseek | 8 | DISAGREE | DISAGREE | For married filing separately who lived with their spouse at any time in 2025, the worksheet skips lines 8 through 15; this line is not shown and its value is not used by line 16 in that case. The expression still assigns the single/lived-apart amount for computation only. |
| ssb | deepseek | 9 | DISAGREE | DISAGREE | When line 8 is not less than line 7, the worksheet stops and taxable benefits are zero; subtract_floor0 yields zero, which propagates to line 18. |
| tax_on_amount | deepseek | tax | DISAGREE | DISAGREE | The Tax Table is used below ordinary.table_boundary ($100,000) and the Tax Computation Worksheet at or above that boundary. |
| tcw | deepseek | tax | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 1 | DISAGREE | DISAGREE | Distribution-only path: no Form 4797 section 1250 property is in scope; entered as zero. |
| u1250 | deepseek | 10 | DISAGREE | DISAGREE | Distribution-only path: no partnership interest sale is in scope; entered as zero. |
| u1250 | deepseek | 11 | DISAGREE | DISAGREE | Only Form 1099-DIV box 2b is available in this closed distribution-only slice; other line 11 sources (Schedule K-1, Form 2439, Form 1099-R) are outside it. |
| u1250 | deepseek | 12 | DISAGREE | DISAGREE | Distribution-only path: no section 1250 sale or disposition outside Part I of Form 4797 is in scope; entered as zero. |
| u1250 | deepseek | 13 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 14 | DISAGREE | DISAGREE | Uses the 28% Rate Gain Worksheet total of lines 1 through 4; in this distribution-only slice the other sources are zero. |
| u1250 | deepseek | 15 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 16 | DISAGREE | DISAGREE | Only the Schedule D, line 14 carryover is available in this slice; no Schedule K-1 (Form 1041), box 11, code D carryover is in scope. |
| u1250 | deepseek | 17 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 18 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 2 | DISAGREE | DISAGREE | No Form 4797 property in scope; entered as zero. |
| u1250 | deepseek | 3 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 4 | DISAGREE | DISAGREE | Distribution-only path: no Form 6252 installment sale is in scope; entered as zero. |
| u1250 | deepseek | 5 | DISAGREE | DISAGREE | Distribution-only path: no Schedule K-1 partnership or S corporation amount is in scope; entered as zero. |
| u1250 | deepseek | 6 | DISAGREE | DISAGREE | (no reason given) |
| u1250 | deepseek | 7 | DISAGREE | DISAGREE | No Form 4797, line 7 gain is in scope, so the smaller of line 6 and that gain is zero. |
| u1250 | deepseek | 8 | DISAGREE | DISAGREE | No Form 4797, line 8 amount is in scope; entered as zero. |
| u1250 | deepseek | 9 | DISAGREE | DISAGREE | (no reason given) |
| w2 | deepseek | w2.sav_deferral | DISAGREE | DISAGREE | (no reason given) |

## Render comparison

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aqee | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| asset | deepseek (deepseek-flash) | 14 | 10 | 71.4% | 0/14 (0.0%) | pending | 2 | 1 | 1 | 1 |
| carloan | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pass | 0 | 1 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| clcw26 | deepseek (deepseek-flash) | 13 | 12 | 92.3% | 0/13 (0.0%) | pass | 0 | 0 | 1 | 0 |
| dcprov | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| dependent | deepseek (deepseek-flash) | 11 | 10 | 90.9% | 0/11 (0.0%) | pass | 0 | 1 | 0 | 0 |
| div | deepseek (deepseek-flash) | 22 | 20 | 90.9% | 1/22 (4.5%) | pass | 1 | 0 | 1 | 0 |
| eic | deepseek (deepseek-flash) | 13 | 13 | 100.0% | 0/13 (0.0%) | pending | 0 | 0 | 0 | 0 |
| f1040 | deepseek (deepseek-flash) | 58 | 52 | 89.7% | 1/58 (1.7%) | pass | 4 | 1 | 1 | 0 |
| f1095a | deepseek (deepseek-flash) | 77 | 76 | 98.7% | 0/77 (0.0%) | pass | 0 | 1 | 0 | 0 |
| f2441 | deepseek (deepseek-flash) | 36 | 28 | 77.8% | 0/36 (0.0%) | pass | 3 | 5 | 0 | 0 |
| f4562 | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pass | 3 | 2 | 0 | 0 |
| f4952 | deepseek (deepseek-flash) | 15 | 12 | 80.0% | 1/15 (6.7%) | pass | 1 | 0 | 2 | 0 |
| f5329 | deepseek (deepseek-flash) | 7 | 6 | 85.7% | 0/7 (0.0%) | pass | 1 | 0 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 72 | 72 | 100.0% | 0/72 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f8606 | deepseek (deepseek-flash) | 5 | 3 | 60.0% | 0/5 (0.0%) | pending | 1 | 0 | 1 | 0 |
| f8863 | deepseek (deepseek-flash) | 25 | 19 | 76.0% | 0/25 (0.0%) | pass | 2 | 4 | 0 | 0 |
| f8880 | deepseek (deepseek-flash) | 21 | 17 | 81.0% | 0/21 (0.0%) | pass | 3 | 1 | 0 | 0 |
| f8889 | deepseek (deepseek-flash) | 19 | 12 | 63.2% | 0/19 (0.0%) | pass | 4 | 2 | 1 | 0 |
| f8959 | deepseek (deepseek-flash) | 24 | 23 | 95.8% | 0/24 (0.0%) | pass | 0 | 0 | 1 | 0 |
| f8960 | deepseek (deepseek-flash) | 25 | 23 | 92.0% | 0/25 (0.0%) | pass | 1 | 1 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 95 | 92 | 96.8% | 0/95 (0.0%) | pass | 0 | 1 | 2 | 0 |
| f8995 | deepseek (deepseek-flash) | 16 | 13 | 81.2% | 0/16 (0.0%) | pending | 1 | 1 | 1 | 0 |
| f8995a | deepseek (deepseek-flash) | 14 | 12 | 85.7% | 0/14 (0.0%) | pending | 1 | 0 | 1 | 0 |
| ftc | deepseek (deepseek-flash) | 12 | 11 | 91.7% | 0/12 (0.0%) | pass | 0 | 1 | 0 | 0 |
| g28 | deepseek (deepseek-flash) | 7 | 3 | 42.9% | 0/7 (0.0%) | pass | 0 | 4 | 0 | 0 |
| gift | deepseek (deepseek-flash) | 5 | 5 | 100.0% | 0/5 (0.0%) | pass | 0 | 0 | 0 | 0 |
| household | deepseek (deepseek-flash) | 48 | 41 | 85.4% | 2/48 (4.2%) | pass | 5 | 2 | 0 | 0 |
| interest | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| ira | deepseek (deepseek-flash) | 21 | 13 | 61.9% | 0/21 (0.0%) | pending | 2 | 4 | 2 | 0 |
| ltc | deepseek (deepseek-flash) | 2 | 2 | 100.0% | 0/2 (0.0%) | pass | 0 | 0 | 0 | 0 |
| mq | deepseek (deepseek-flash) | 7 | 7 | 100.0% | 0/7 (0.0%) | pass | 0 | 0 | 0 | 0 |
| oi8z | deepseek (deepseek-flash) | 2 | 1 | 50.0% | 0/2 (0.0%) | pending | 1 | 0 | 0 | 0 |
| otjob | deepseek (deepseek-flash) | 1 | 1 | 100.0% | 0/1 (0.0%) | pass | 0 | 0 | 0 | 0 |
| person | deepseek (deepseek-flash) | 32 | 26 | 81.2% | 0/32 (0.0%) | pass | 1 | 0 | 5 | 0 |
| qbi | deepseek (deepseek-flash) | 1 | 0 | 0.0% | 1/1 (100.0%) | pending | 0 | 1 | 0 | 0 |
| qdcg | deepseek (deepseek-flash) | 25 | 24 | 96.0% | 0/25 (0.0%) | pass | 0 | 0 | 1 | 0 |
| refund | deepseek (deepseek-flash) | 9 | 7 | 77.8% | 0/9 (0.0%) | pass | 0 | 2 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 10 | 3 | 30.0% | 0/10 (0.0%) | pending | 2 | 4 | 1 | 0 |
| s1 | deepseek (deepseek-flash) | 29 | 21 | 72.4% | 0/29 (0.0%) | pass | 5 | 3 | 0 | 0 |
| s179 | deepseek (deepseek-flash) | 13 | 11 | 84.6% | 1/13 (7.7%) | pass | 0 | 2 | 0 | 0 |
| s1a | deepseek (deepseek-flash) | 43 | 41 | 95.3% | 0/43 (0.0%) | pass | 1 | 1 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 12 | 10 | 83.3% | 0/12 (0.0%) | pass | 2 | 0 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 13 | 10 | 76.9% | 0/13 (0.0%) | pass | 2 | 1 | 0 | 0 |
| s8812 | deepseek (deepseek-flash) | 50 | 48 | 96.0% | 0/50 (0.0%) | pass | 0 | 2 | 0 | 0 |
| sa | deepseek (deepseek-flash) | 24 | 21 | 87.5% | 0/24 (0.0%) | pass | 1 | 1 | 1 | 0 |
| sales | deepseek (deepseek-flash) | 3 | 1 | 33.3% | 0/3 (0.0%) | pass | 0 | 2 | 0 | 0 |
| sb | deepseek (deepseek-flash) | 6 | 4 | 66.7% | 0/6 (0.0%) | pending | 1 | 1 | 0 | 0 |
| sc | deepseek (deepseek-flash) | 75 | 72 | 96.0% | 0/75 (0.0%) | pass | 3 | 0 | 0 | 0 |
| scope | deepseek (deepseek-flash) | 5 | 2 | 40.0% | 1/5 (20.0%) | pending | 3 | 0 | 0 | 0 |
| scveh | deepseek (deepseek-flash) | 27 | 21 | 77.8% | 0/27 (0.0%) | pass | 0 | 5 | 1 | 0 |
| sd | deepseek (deepseek-flash) | 46 | 44 | 95.7% | 0/46 (0.0%) | pass | 0 | 1 | 1 | 0 |
| sdtw | deepseek (deepseek-flash) | 47 | 46 | 97.9% | 0/47 (0.0%) | pass | 0 | 1 | 0 | 0 |
| se | deepseek (deepseek-flash) | 15 | 10 | 66.7% | 0/15 (0.0%) | pending | 0 | 5 | 0 | 0 |
| sli | deepseek (deepseek-flash) | 8 | 5 | 62.5% | 0/8 (0.0%) | pending | 1 | 2 | 0 | 0 |
| ssb | deepseek (deepseek-flash) | 18 | 17 | 94.4% | 0/18 (0.0%) | pass | 1 | 0 | 0 | 0 |
| tax_on_amount | deepseek (deepseek-flash) | 4 | 4 | 100.0% | 0/4 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tcw | deepseek (deepseek-flash) | 46 | 46 | 100.0% | 0/46 (0.0%) | pass | 0 | 0 | 0 | 0 |
| tipjob | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pass | 0 | 0 | 0 | 0 |
| u1250 | deepseek (deepseek-flash) | 18 | 4 | 22.2% | 0/18 (0.0%) | pass | 5 | 8 | 1 | 0 |
| w2 | deepseek (deepseek-flash) | 17 | 16 | 94.1% | 1/17 (5.9%) | pass | 1 | 0 | 0 | 0 |
| **all** | | 1325 | 1158 | 87.4% | | | 65 | 75 | 27 | 1 |

Pending asset [deepseek]: 1 missing expected lines.
Pending eic [deepseek]: stale subject: claude, deepseek.
Pending f8606 [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending f8995 [deepseek]: 2 open, unclassified or interface-gap rulings.
Pending f8995a [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending ira [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending oi8z [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending qbi [deepseek]: model-error noise above 10%.
Pending retirement [deepseek]: stale subject: claude, deepseek.
Pending sb [deepseek]: 1 open, unclassified or interface-gap rulings.
Pending scope [deepseek]: 2 open, unclassified or interface-gap rulings; model-error noise above 10%.
Pending se [deepseek]: 5 open, unclassified or interface-gap rulings.
Pending sli [deepseek]: 3 open, unclassified or interface-gap rulings.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| asset | deepseek | 25 | MISMATCH | IRS line 25 says 'Enter on line 25 your total special depreciation allowance for all qualified listed property'; line 14 is not the listed-property special allowance total, so copying line 14 uses a different operand. |
| asset | deepseek | 26(i) | MISMATCH | IRS says 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.'; line 6(c) is not the listed-property elected section 179 cost. |
| div | deepseek | unsupported | MISMATCH | MISMATCH: The IRS text says 'Any amount received in excess of your basis is taxable to you as capital gain.' The condition only flags Box 3 when basis reductions were not applied to records with no distribution exceeding basis, so it omits distributions exceeding basis. |
| f1040 | deepseek | 16 | MISMATCH | The restatement also requires the Qualified Dividends and Capital Gain Tax Worksheet to apply, but the IRS says to use the Schedule D Tax Worksheet if 'You have to file Form 4952 and you have an amount on line 4g, even if you don’t need to file Schedule D.' |
| f1040 | deepseek | 1z | MISMATCH | IRS line 1z says 'Add lines 1a through 1h', but the restatement adds only line 1a and line 1e, omitting lines 1b through 1d and 1f through 1h. |
| f1040 | deepseek | 27c | MISMATCH | IRS says 'Check the box on line 27c if you do not want to claim the earned income credit or if you have been instructed to check the box'; the restatement deliberately omits the filer's own choice not to claim the EIC. |
| f1040 | deepseek | 28 (box) | MISMATCH | IRS line 28 says 'If you do not want to claim the ACTC, check here'; the restatement hard-codes the box to false, so it cannot reflect a taxpayer's election not to claim the ACTC. |
| f2441 | deepseek | 12 | MISMATCH | The restatement sums only W-2-derived benefits, but line 12 says 'If you were self-employed or a partner, include amounts you received under a dependent care assistance program from your sole proprietorship or partnership.' |
| f2441 | deepseek | 21 | MISMATCH | Uses a $5,000 cap only; the form says '$5,000 ($2,500 if married filing separately and you were required to enter your spouse's earned income on line 19).' |
| f2441 | deepseek | 22 | MISMATCH | The program always enters zero, but line 22 says 'Is any amount on line 12 or 13 from your sole proprietorship or partnership? ... Yes. Enter the amount here.' |
| f4562 | deepseek | 25 | MISMATCH | The helper sums asset.bonus_2025 for listed property, but that asset helper uses line 14, which is expressly for property '(other than listed property)'; line 25 is the special allowance for qualified listed property used more than 50% in a qualified business use. |
| f4562 | deepseek | 28 | MISMATCH | The helper adds only line 25 and line 26(h). IRS line 28 says: 'Add amounts in column (h), lines 25 through 27,' so line 27 is omitted. |
| f4562 | deepseek | 29 | MISMATCH | The helper uses asset.s179_2025, which references line 6(c), but line 6 instructions say 'Do not include any listed property on line 6. Enter the elected section 179 cost of listed property in column (i) of line 26.' Line 29 is limited to column (i), line 26. |
| f4952 | deepseek | 4a | MISMATCH | IRS line 4a includes ordinary dividends "except Alaska Permanent Fund dividends"; adding f1040 line 3b without that exclusion would include them. |
| f5329 | deepseek | 1 | MISMATCH | IRS line 1 is 'Early distributions includible in income,' and line 2 subtracts 'Early distributions included on line 1 that are not subject to the additional tax'; the helper only includes code 1 or code S distributions with no known exception, so early distributions with a known exception are omitted. |
| f8606 | deepseek | 1 | MISMATCH | The IRS line 1 instructions say to include repayments of qualified reservist distributions and to subtract worksheet line 12 "or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less"; the helper uses only worksheet line 12 and omits those items. |
| f8863 | deepseek | 15 | MISMATCH | IRS line 15 says if zero or less, 'skip lines 16 and 17, enter -0- on line 18, and go to line 19'; the restatement instead enters -0- on line 15 and does not skip line 16. |
| f8863 | deepseek | 18 | MISMATCH | IRS line 10 says if line 10 is zero, 'skip lines 11 through 17, enter -0- on line 18'; the restatement always divides line 15 by line 16, using lines that are not reported when line 10 is zero. |
| f8880 | deepseek | 1(b) | MISMATCH | The IRS says 'Complete column (b) only if you're filing a joint return'; the restatement sums spouse entries without an MFJ gate. |
| f8880 | deepseek | 2(b) | MISMATCH | The IRS says 'Complete column (b) only if you're filing a joint return'; the restatement sums spouse entries without an MFJ gate. |
| f8880 | deepseek | 4(a) | MISMATCH | The IRS line says 'If married filing jointly, include both spouses’ amounts in both columns'; the restatement's dist_2025 sums every confirmed person's 2025 distributions even on a nonjoint return. |
| f8889 | deepseek | 10 | MISMATCH | The IRS line is 'Qualified HSA funding distributions' and the instructions say 'Enter this amount on line 10'; the restatement always enters zero. |
| f8889 | deepseek | 15 | MISMATCH | The IRS instructions say 'Do not include the distribution of an excess contribution taken out after the due date, including extensions, of your return even if used for qualified medical expenses'; the restatement omits that exclusion. |
| f8889 | deepseek | 17a | MISMATCH | The IRS exceptions are distributions made after the account beneficiary 'Dies, Becomes disabled or Turns age 65'; the restatement lists only disabled or age 65. |
| f8889 | deepseek | 4 | MISMATCH | The IRS line says 'Enter the amount you and your employer contributed to your Archer MSAs for 2025 from Form 8853, lines 1 and 2' and to include spouse's Archer MSA contributions in family-coverage cases; the restatement always enters zero. |
| f8960 | deepseek | 9b | MISMATCH | IRS says to include 'state, local, and foreign income taxes' and 'state, local, and foreign real property taxes,' but the restatement mentions only state/local income and property taxes and an exclusion for foreign taxes claimed as a credit. |
| f8995 | deepseek | 11 | MISMATCH | IRS line 11 instructions compute 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b' and do not provide a zero floor; the restatement adds an 'If zero or less, enter -0-' condition. |
| f8995a | deepseek | 33 | MISMATCH | The restatement adds an 'if zero or less, enter -0-' floor, but the IRS instruction is only 'Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b'; no zero floor is stated for line 33. |
| household | deepseek | ctc_ssn | MISMATCH | The IRS says 'To claim the child tax credit, you must have a valid SSN, which means it must be valid for employment' and 'If your qualifying child didn’t have an SSN valid for employment... you can’t claim the child tax credit for that child'; the restatement allows SSN or ITIN for each other person and does not check the qualifying children. |
| household | deepseek | hoh_community_property | MISMATCH | The IRS says 'If you were considered married for part of the year and lived in a community property state... special rules may apply'; this helper requires married at the end of 2025, missing part-year married HOH filers. |
| household | deepseek | home_cost | MISMATCH | The IRS note says TANF used 'to support another person' is considered support you provided for that person, and amounts in a child's or qualifying person's name are considered paid by the child; the restatement instead treats TANF used for the home as paid by you and refers to any person living in the home. |
| household | deepseek | test2_absence_persons | MISMATCH | The same omission exists for non-dependent Test 2 persons: the IRS Test 2 can turn on a qualifying child who isn’t your dependent, but the restatement counts only dependent entries. |
| household | deepseek | test2_persons | MISMATCH | IRS Test 2 includes 'Your unmarried qualifying child who isn’t your dependent,' a married qualifying child who isn’t your dependent, and certain divorced/separated-parent children; counting only dependent entries misses those non-dependent Test 2 persons. |
| ira | deepseek | 1b | MISMATCH | The IRS line is 'If married filing jointly, was your spouse covered by a retirement plan?'; the restatement adds a contribution condition and does not condition the line on married filing jointly. |
| ira | deepseek | 8 | MISMATCH | The IRS line includes 'Nontaxable combat pay' in the total; the restatement adds only W-2 box 1 wages and Schedule 1 line 2a. |
| oi8z | deepseek | 8z (amount) | MISMATCH | The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income. |
| person | deepseek | Step 3 | MISMATCH | IRS Step 3 says only 'Net earnings from self-employment. Subtract step 2 from step 1'; the restatement adds 'If zero or less, enter -0-,' which changes a negative subtraction result. |
| retirement | deepseek | (SMW 6) | MISMATCH | The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always computes line 6. |
| retirement | deepseek | (SMW 7) | MISMATCH | The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always subtracts line 6 from line 2. |
| s1 | deepseek | 15 | MISMATCH | The restatement returns zero when the person has no Schedule C, but line 15 is the Schedule SE line 13 deduction and Schedule SE also covers farm and partnership self-employment; no refusal names that exclusion. |
| s1 | deepseek | 16 | MISMATCH | The IRS line is 'Self-employed SEP, SIMPLE, and qualified plans'; the restatement computes only a SEP or SIMPLE deduction and does not refuse qualified plans. |
| s1 | deepseek | 17 | MISMATCH | The computation uses only Schedule C Form 7206 line 14 amounts; a partner's self-employed health insurance deduction (Form 7206) would produce zero without a refusal naming partners. |
| s1 | deepseek | 20 | MISMATCH | The IRA Deduction Worksheet line 2 says married filing separately and lived apart from your spouse for all of 2025, enter $89,000; the program uses $10,000 for every MFS filer, so the line 20 deduction can be wrong. |
| s1 | deepseek | 8f | MISMATCH | The IRS line 8f instruction says 'Enter the total of the amounts from Form 8889, lines 16 and 20.' The restatement uses only Form 8889 line 16. |
| s1a | deepseek | 23 | MISMATCH | Line 23 adds column (iii), but the program's column (iii) subtracts only Schedule C interest; IRS column (ii) is 'Deducted on Schedule C, Schedule E, or Schedule F.' |
| s2 | deepseek | 18 | MISMATCH | The IRS says 'Add lines 17a through 17z,' but the restatement enters only the amount from line 17c. |
| s2 | deepseek | 1z | MISMATCH | The IRS says 'Add lines 1a through 1y,' but the restatement enters only the amount from line 1a. |
| s3 | deepseek | 14 | MISMATCH | The IRS says 'Add lines 13a through 13z'; the program instead accepts a supplied total without adding those lines. |
| s3 | deepseek | 3 | MISMATCH | The gate treats expenses paid plus not being claimed as a dependent as sufficient to claim the credit, but the IRS also says 'You cannot claim an education credit ... if ... Your filing status is married filing separately' and if MAGI is at or above the threshold; those disqualifiers are omitted. |
| sa | deepseek | 2 | MISMATCH | The IRS line says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement uses an AGI helper that is not less than zero, adding a floor not in the line. |
| sb | deepseek | 7a | MISMATCH | The restatement covers only Question 1; the IRS line also has Line 7a—Question 2, which asks whether you are required to file FinCEN Form 114. |
| sc | deepseek | 13 (sc.line13) | MISMATCH | IRS line 13 is depreciation and the section 179 expense deduction; Form 4562 line 22 includes lines 14 through 17, lines 19 and 20(g), and line 21, while the restatement's helper lists only lines 14, 17, 19 and 21. |
| sc | deepseek | 4 (sc.f7206_line4) | MISMATCH | IRS Form 7206 line 4 says 'Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established'; the restatement uses only net profit of this business. |
| sc | deepseek | 5 (sc.f7206_line5) | MISMATCH | IRS Form 7206 line 5 includes 'plus any other income allocable to the profitable businesses'; the restatement only totals net profits and excludes losses. |
| scope | deepseek | credits | UNCLEAR | The IRS text does not include Schedule 3 Part I or the instructions for the listed credits (Form 2441, Form 8880, Form 5695, Form 8962, Form 8863, etc.), so the scope question cannot be compared. |
| scope | deepseek | other_line16 | MISMATCH | The restatement includes CFC/PFIC ownership under Form 1040 line 16, but the IRS text says those interests affect the 'modified AGI of Form 8960 line 13' (MAGI), not line 16; line 16 instead involves items such as Form 8615, Schedule D, qualified dividends, Schedule J, and Form 2555. |
| scope | deepseek | schedule1 | UNCLEAR | The IRS text only references Form 1040 lines 8 and 10 as coming from Schedule 1; it does not include Schedule 1 line 10/26 or the listed income and adjustment items, so the restatement cannot be verified. |
| sli | deepseek | 6 | MISMATCH | The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5. |
| ssb | deepseek | 9 | MISMATCH | The IRS line 9 is conditional: “Is the amount on line 8 less than the amount on line 7? No. STOP None of your social security benefits are taxable... Yes. Subtract line 8 from line 7.” The restatement instead always subtracts and floors at zero, omitting the No/STOP condition. |
| u1250 | deepseek | 2 | MISMATCH | IRS line 2 says 'Enter the amount from Form 4797, line 26g, for the property for which you made an entry on line 1'; the restatement always enters div.screen $0 and does not exclude Form 4797 property. |
| u1250 | deepseek | 3 | MISMATCH | IRS line 3 says 'Subtract line 2 from line 1'; the restatement always enters div.screen $0, so it is wrong whenever line 1 or line 2 is nonzero. |
| u1250 | deepseek | 6 | MISMATCH | IRS line 6 says 'Add lines 3 through 5'; the restatement always enters div.screen $0, rather than adding lines 3 through 5. |
| u1250 | deepseek | 7 | MISMATCH | IRS line 7 says 'Enter the smaller of line 6 or the gain from Form 4797, line 7'; the restatement always enters div.screen $0 and does not exclude Form 4797 gain. |
| u1250 | deepseek | 9 | MISMATCH | IRS line 9 says 'Subtract line 8 from line 7. If zero or less, enter -0-'; the restatement always enters div.screen $0, so it is wrong when lines 7 or 8 are nonzero. |
| w2 | deepseek | 2 | MISMATCH | The restatement says to enter zero for box 2 on Forms W-2AS, W-2CM, W-2GU, or W-2VI, but the IRS text says: “For Forms W-2AS, W-2CM, W-2GU, or W-2VI, show the total American Samoa, CNMI, Guam, or U.S. Virgin Islands income tax withheld.” |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| asset | deepseek | (c) | MISMATCH | MISMATCH | IRS column (c) says: 'To find the basis for depreciation, multiply the cost or other basis of the property by the percentage of business/investment use. From that result, subtract any credits and deductions allocable to the property.' The restatement only multiplies cost by the business-use percentage and omits the required subtraction. |
| carloan | deepseek | 22(ii) | MISMATCH | MISMATCH | The IRS text says 'enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F),' but the restatement computes only the QPVLI part of Schedule C interest and omits other elsewhere-deducted QPVLI such as Schedule E or Schedule F. |
| dependent | deepseek | 2(d) | MISMATCH | MISMATCH | The IRS column (d) instruction says, 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' The helper instead includes expenses paid with dependent care benefits and only says Form 2441 subtracts the excluded benefits later. |
| f1040 | deepseek | 29 | UNCLEAR | MISMATCH | The eligibility test uses only expenses paid and dependent status, but Form 8863 instructions state, for example, 'You cannot claim an education credit ... if ... Your filing status is married filing separately' and impose other eligibility limits. |
| f1095a | deepseek | b_counted | MISMATCH | MISMATCH | The IRS rule is monthly: if more than one Form 1095-A shows coverage in a particular month from the same state, enter column B from only one form. The 'covers every month this one does' test can leave both partially overlapping same-state forms counted, double-counting the overlapping months. |
| f2441 | deepseek | 18 | MISMATCH | MISMATCH | Line 18 uses the same incomplete earned-income base, W-2 box 1 plus Worksheet B, instead of Form 1040 line 1z; it also excludes only line 1e rather than implementing the instruction that earned income doesn't include dependent care benefits shown on line 12. |
| f2441 | deepseek | 19 | MISMATCH | MISMATCH | Besides inheriting the incomplete earned-income definition, it sends every non-MFJ filer to line 18; for married filing separately the IRS says 'No. Enter your spouse's earned income on line 19.' |
| f2441 | deepseek | 4 | MISMATCH | MISMATCH | The restatement computes earned income from W-2 box 1, the line 1e share, and Worksheet B, but the instructions start with 'the amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z' and also include statutory employee Schedule C line 1; it omits other line 1z earned income. |
| f2441 | deepseek | 5 | MISMATCH | MISMATCH | The MFJ branch uses the same incomplete earned-income definition for the spouse; the instructions for lines 4 and 5 define earned income from Form 1040 line 1z and Schedule SE line 3 less Schedule 1 line 15, not just W-2 box 1 plus line 1e and Worksheet B. |
| f2441 | deepseek | CLW 2 | MISMATCH | MISMATCH | The program enters only Schedule 3 line 1, but the Credit Limit Worksheet line 2 is 'Schedule 3 (Form 1040), line 1 ... and line 6l (Form 8978, line 14).' |
| f4562 | deepseek | 22 | MISMATCH | MISMATCH | The restatement omits lines 15 and 16, lines 19g through 19j, and line 20. IRS line 22 says: 'Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21.' |
| f4562 | deepseek | 26(h) | MISMATCH | MISMATCH | The helper uses asset.dep_listed, built from line 19(g) and line 17 MACRS; Part III says 'Don’t include listed property,' while line 26(h) is the Part V depreciation deduction for listed property used more than 50% in a qualified business use. |
| f8863 | deepseek | 13 | MISMATCH | MISMATCH | IRS line 13 says $180,000 if married filing jointly, or $90,000 if single, head of household, or qualifying surviving spouse; the restatement adds $90,000 for married filing separately, although married filing separately cannot claim education credits. |
| f8863 | deepseek | 16 | MISMATCH | MISMATCH | IRS line 16 gives $20,000 for married filing jointly or $10,000 for single, head of household, or qualifying surviving spouse; the restatement adds married filing separately and reports line 16 whenever line 10 is positive even though line 15 says to skip line 16 when line 15 is zero or less. |
| f8863 | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 says '$180,000 if married filing jointly; or $90,000 if single, head of household, or qualifying surviving spouse'; the restatement also gives $90,000 for married filing separately, which the instructions say cannot claim an education credit. |
| f8863 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 says '$20,000 if married filing jointly; or $10,000 if single, head of household, or qualifying surviving spouse'; the restatement adds $10,000 for married filing separately, which cannot claim the credit. |
| f8880 | deepseek | (CLW 2) | MISMATCH | MISMATCH | The IRS says 'Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l'; the restatement adds only s3 lines 1, 2, and 3, omitting 6d and 6l. |
| f8889 | deepseek | 14b | MISMATCH | MISMATCH | Form 8889 line 14b also requires 'any excess contributions (and the earnings on those excess contributions) included on line 14a that were withdrawn by the due date of your return'; the restatement computes only the rollover portion and omits withdrawn excess contributions and earnings. |
| f8889 | deepseek | 7 | MISMATCH | MISMATCH | The line 7 worksheet counts months in which 'You or your spouse had family coverage under an HDHP and were, or were considered to be, an eligible individual on the first day of the month' and 'were not enrolled in Medicare for the month'; the restatement instead uses the broader count of all months the filer was an eligible individual, so it can overstate the additional contribution amount when so… |
| f8960 | deepseek | 5a | MISMATCH | MISMATCH | IRS says to combine 'Form 1040 or 1040-SR, line 7a, and Schedule 1 (Form 1040), line 4,' but the restatement uses only f1040 line 7a and omits Schedule 1 line 4. |
| f8962 | deepseek | 28 | MISMATCH | MISMATCH | The IRS line 28 instructions say that if you are self-employed and claiming the self-employed health insurance deduction, see Pub. 974 for the amount to enter; the restatement only uses the Table 5 limitation and has no adjustment or refusal for that case. |
| f8995 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 instructions say if you're not required to file Schedule D, your net capital gain is the amount on Form 1040 line 7a; the restatement uses only the smaller of Schedule D lines 15 and 16. |
| ftc | deepseek | regular_tax | MISMATCH | MISMATCH | IRS line 20 requires Form 1040 line 16 plus Schedule 2 line 1z 'less any tax included on line 16 from Form 4972' (and possible Form 8978 adjustment); the restatement only adds the two lines. |
| g28 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says 'Enter the total of all collectibles gain or (loss) from items you reported on Form 8949, Part II'; the restatement uses a $0 div helper with NonNegDollars, omitting that gain/loss. |
| g28 | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 says 'Enter the total of all collectibles gain or (loss) from Form 4684, line 4 (but only if Form 4684, line 15, is more than zero); Form 6252; Form 6781, Part II; and Form 8824'; the restatement is a $0 div helper and omits those sources and losses. |
| g28 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 says 'Enter the total of any collectibles gain reported to you on: Form 1099-DIV, box 2d; Form 2439, box 1d; and Schedule K-1 from a partnership, S corporation, estate, or trust'; the restatement only uses Form 1099-DIV box 2d. |
| g28 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 also includes 'Schedule K-1 (Form 1041), box 11, code D'; the restatement only takes Schedule D line 14. |
| household | deepseek | filing_status_conflict | MISMATCH | MISMATCH | It omits MFS: the IRS says 'Check the “Married filing separately” box... if you are married at the end of 2025 and file a separate return,' so MFS with married false and no 2025 spouse death is also a conflict. |
| household | deepseek | qss_eligible | MISMATCH | MISMATCH | It tells the filer to answer No if the child was presumed kidnapped, but Pub. 501 says 'You may be eligible to file as a qualifying surviving spouse even if the child... has been kidnapped'; it also repeats the TANF home-cost statement. |
| ira | deepseek | 1a | MISMATCH | MISMATCH | The IRS line asks 'Were you covered by a retirement plan' without requiring traditional IRA contributions; the restatement adds that condition and does not reflect the MFS spouse-plan deemed-coverage rule. |
| ira | deepseek | 2a | MISMATCH | MISMATCH | For married filing separately and living apart from the spouse all year, the IRS says 'enter $89,000'; the program uses $10,000 for all married-filing-separately cases. |
| ira | deepseek | 4 | MISMATCH | MISMATCH | The IRS says to add Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits Schedule 1 line 12, line 14, and line 23. |
| ira | deepseek | 9 | MISMATCH | MISMATCH | The IRS line includes earned income 'as a self-employed individual or a partner'; the restatement uses only Schedule C amounts and zeros anyone without a Schedule C. |
| qbi | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 is "Qualified business net (loss) carryforward from the prior year" shown with parentheses, and line 4 says "Combine lines 2 and 3," so the carryforward is a negative amount; the restatement instead says "entered as a positive amount." The line 3 instructions also require the "qualified portion" allowed in calculating taxable income in the current year, not merely prior-year line 16. |
| refund | deepseek | 1 | MISMATCH | MISMATCH | The IRS Exception says to use Pub. 525 instead of this worksheet if, among other things, "You received a refund in 2025 that is for a tax year other than 2024" or "You made your last payment of 2024 estimated state or local income tax in 2025"; the program has no refusal for those cases. |
| refund | deepseek | 6 | UNCLEAR | MISMATCH | IRS line 6 says "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and for MFS allows spouse boxes only if "your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent"; the restatement adds unspecified box amounts and allows spouse boxes for any MFS filer. |
| retirement | deepseek | (SMW 10) | MISMATCH | MISMATCH | Line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement always adds lines 6 and 8. |
| retirement | deepseek | (SMW 11) | MISMATCH | MISMATCH | Line 11 is part of the 'Do not complete the rest of this worksheet' branch for a pre-1987 annuity starting date, but the restatement always subtracts line 10 from line 2. |
| retirement | deepseek | (SMW 4) | MISMATCH | MISMATCH | Table 1 has separate numbers for an annuity starting date before November 19, 1996 (300/260/240/170/120) and after November 18, 1996 (360/310/260/210/160); the restatement uses only the after-November-18-1996 numbers. |
| retirement | deepseek | (SMW 8) | MISMATCH | MISMATCH | For a pre-1987 annuity starting date the worksheet says to enter the line 5 amount on line 8, not the smaller of line 5 or line 7 as the restatement does. |
| s1 | deepseek | 10 | MISMATCH | MISMATCH | IRS line 10 says 'Combine lines 1 through 7 and 9.' The restatement adds only lines 1, 2a, 3, 7, and 9, omitting lines 4 through 6. |
| s1 | deepseek | 25 | MISMATCH | MISMATCH | IRS line 25 says 'Total other adjustments. Add lines 24a through 24z.' The restatement enters only line 24a, omitting lines 24b through 24z. |
| s1 | deepseek | 26 | MISMATCH | MISMATCH | IRS line 26 says 'Add lines 11 through 23 and 25.' The restatement omits lines 12, 14, and 23 (among others) without a refusal naming them. |
| s179 | deepseek | 1 | UNCLEAR | MISMATCH | Worksheet 1 says to "Enter the smaller of line 1 or line 2 here" and then "Enter the amount from line 3 here and on Form 4562, line 1"; the restatement enters only the $2,500,000 maximum. |
| s179 | deepseek | 13 | UNCLEAR | MISMATCH | The line 5 instructions say: "If line 5 is zero... enter the carryover of any disallowed deduction from 2024 ... on line 13." The restatement leaves line 10 out when line 5 is zero and then computes line 13 from lines 9 and 10 only, so it drops that carryover. |
| s1a | deepseek | 36b | MISMATCH | MISMATCH | IRS line 36b applies only 'If you are married filing jointly'; the restatement checks only that the spouse was born before January 2, 1961 and has a valid SSN. |
| s3 | deepseek | 1 | MISMATCH | MISMATCH | The referenced ftc.credit uses ftc.regular_tax, which the program defines as Form 1040 line 16 plus Schedule 2 line 1z; the IRS says regular tax is that total 'less any tax included on line 16 from Form 4972.' |
| s8812 | deepseek | 18a | UNCLEAR | MISMATCH | The Earned Income Chart says a filer with net earnings from self-employment who uses either optional method enters the Earned Income Worksheet amount 'even if you are also taking the EIC,' and its Worksheet B branch is for filers who 'completed Worksheet B.' The restatement instead always uses Worksheet B line 4b whenever its self-employed helper is true. |
| s8812 | deepseek | 21 | UNCLEAR | MISMATCH | The Additional Medicare Tax and RRTA Tax Worksheet line 16 says 'Add lines 6, 7, 11, and 15' and enter on line 21. The restatement adds only worksheet lines 6 and 7, omitting Tier 1 RRTA lines 11 and 15, with no RRTA refusal. |
| sa | deepseek | 1 | MISMATCH | MISMATCH | The restatement omits the eligible category in the IRS instructions: 'Any person you could have claimed as a dependent except that you or your spouse if filing jointly can be claimed as a dependent on someone else's 2025 return.' |
| sales | deepseek | (e) | MISMATCH | MISMATCH | The IRS says "Box A or Box G" and "Box D or Box J" cover transactions with an amount shown for cost or other basis reported to the IRS; the program's "Basis reported to IRS" helper is only boxes A or D, so for boxes G/J it would enter the correct adjusted basis instead of the reported basis. |
| sales | deepseek | (g) | MISMATCH | MISMATCH | The IRS says "Enter in this column any necessary adjustments to gain (or loss)" and, for multiple codes, "enter the net adjustment in column (g)"; the restatement only adds code B and code W adjustments, omitting other necessary adjustments such as codes E, H, or L. |
| sb | deepseek | 4 | UNCLEAR | UNCLEAR | The provided IRS text contains no line 4 instruction or statement that line 4 is line 2 minus line 3, so the arithmetic cannot be verified from the text given. |
| scveh | deepseek | (b) | MISMATCH | MISMATCH | The IRS column (b) instruction says 'Enter the date the property was placed in service' and treats converted property as placed in service on the conversion date; the restatement asks only for the year. |
| scveh | deepseek | 13 | MISMATCH | MISMATCH | The IRS business/investment-use percentage for converted property must be figured only for the months used in business and multiplied by months/12; the restatement simply divides annual business miles by total miles without that conversion proration. |
| scveh | deepseek | 20a | MISMATCH | MISMATCH | The IRS says 'if you leased a vehicle for a term of 30 days or more, you may have to reduce your deduction by the inclusion amount'; the restatement computes only the business portion of lease payments and omits that reduction. |
| scveh | deepseek | 43 | MISMATCH | MISMATCH | IRS line 43 asks "When did you place your vehicle in service for business purposes? (month/day/year)"; the restatement asks only for the year. |
| scveh | deepseek | 9 (scveh.line9w) | MISMATCH | MISMATCH | Worksheet line 9 multiplies line 7 by the business/investment-use percentage; for a converted vehicle that percentage must be prorated by the months used in business, which the restatement's business-miles/total-miles calculation omits. |
| sd | deepseek | 20 | MISMATCH | MISMATCH | The form says if line 17 is No, skip lines 18 through 21 and go to line 22; the restatement evaluates line 20 from zeroed lines 18 and 19 without requiring line 17 to be Yes. |
| sdtw | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says to enter line 3 of the Foreign Earned Income Tax Worksheet instead when filing Form 2555; the restatement always uses Form 1040 line 15. |
| se | deepseek | 2 | MISMATCH | MISMATCH | IRS line 2 includes "Schedule K-1 (Form 1065), box 14, code A" and other income per instructions; restatement uses only this person Schedule C results. |
| se | deepseek | 3 | MISMATCH | MISMATCH | IRS line 3 says "Combine lines 1a, 1b, and 2"; restatement enters only the amount from line 2. |
| se | deepseek | 4b | MISMATCH | MISMATCH | IRS line 4b says "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"; restatement always enters zero. |
| se | deepseek | 5b | MISMATCH | MISMATCH | IRS line 5b says "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"; restatement always enters zero. |
| se | deepseek | 8d | MISMATCH | MISMATCH | IRS line 8d says "Add lines 8a, 8b, and 8c"; restatement enters only line 8a. |
| sli | deepseek | 3 | MISMATCH | MISMATCH | The IRS line says to total "Schedule 1, lines 11 through 20, and 23 and 25"; the restatement omits Schedule 1 line 23 (Archer MSA deduction). |
| sli | deepseek | 5 | MISMATCH | MISMATCH | The IRS says the deduction requires "any status except married filing separately" and line 5 lists only $85,000 for single/HOH/QSS and $170,000 for MFJ; assigning MFS $0 is not in the IRS text and does not exclude MFS. |
| u1250 | deepseek | 1 | MISMATCH | MISMATCH | IRS line 1 says to enter the smaller of Form 4797 line 22 or line 24 for the property, or go to line 4 if none; the restatement always enters div.screen $0 and does not exclude Form 4797 property. |
| u1250 | deepseek | 10 | MISMATCH | MISMATCH | IRS line 10 requires the amount of any gain from the sale or exchange of an interest in a partnership attributable to unrecaptured section 1250 gain; the restatement always enters div.screen $0 and does not exclude such gain. |
| u1250 | deepseek | 11 | MISMATCH | MISMATCH | IRS line 11 includes amounts reported as unrecaptured section 1250 gain on Schedule K-1, Form 1099-DIV, or Form 2439, or in connection with Form 1099-R; the restatement only uses Form 1099-DIV box 2b and omits the other sources. |
| u1250 | deepseek | 12 | MISMATCH | MISMATCH | IRS line 12 requires the total unrecaptured section 1250 gain from sales or other dispositions of section 1250 property held more than 1 year for which no Part I Form 4797 entry was made; the restatement always enters div.screen $0 and does not exclude such amounts. |
| u1250 | deepseek | 16 | MISMATCH | MISMATCH | IRS line 16 includes long-term capital loss carryovers from Schedule D line 14 and Schedule K-1 (Form 1041), box 11, code D; the restatement only uses Schedule D line 14, omitting the K-1 carryover. |
| u1250 | deepseek | 4 | MISMATCH | MISMATCH | IRS line 4 requires the total unrecaptured section 1250 gain included on line 26 or line 37 of Form(s) 6252 from installment sales; the restatement always enters div.screen $0 and does not exclude Form 6252 amounts. |
| u1250 | deepseek | 5 | MISMATCH | MISMATCH | IRS line 5 requires the total of any amounts reported on a Schedule K-1 from a partnership or S corporation as unrecaptured section 1250 gain; the restatement always enters div.screen $0 and does not exclude such K-1 amounts. |
| u1250 | deepseek | 8 | MISMATCH | MISMATCH | IRS line 8 says 'Enter the amount, if any, from Form 4797, line 8'; the restatement always enters div.screen $0 and does not exclude Form 4797 line 8 amounts. |

## Class M hand-work

| form | second family (model) | lines judged by both | both agree | raw agreement | noise / judged | eligibility | current yield | both disputed | Claude only | not judged by both |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aqee | deepseek (deepseek-flash) | 10 | 10 | 100.0% | 0/10 (0.0%) | pass | 0 | 0 | 0 | 0 |
| clcw | deepseek (deepseek-flash) | 31 | 31 | 100.0% | 0/34 (0.0%) | pass | 0 | 0 | 0 | 21 |
| clcw26 | deepseek (deepseek-flash) | 28 | 28 | 100.0% | 0/31 (0.0%) | pending | 0 | 0 | 0 | 24 |
| dependent | deepseek (deepseek-flash) | 12 | 12 | 100.0% | 0/12 (0.0%) | pass | 0 | 0 | 0 | 0 |
| eic | deepseek (deepseek-flash) | 27 | 27 | 100.0% | 0/29 (0.0%) | pending | 0 | 0 | 0 | 80 |
| f1040 | deepseek (deepseek-flash) | 304 | 304 | 100.0% | 0/304 (0.0%) | pending | 0 | 0 | 0 | 8 |
| f1095a | deepseek (deepseek-flash) | 47 | 46 | 97.9% | 1/47 (2.1%) | pending | 1 | 0 | 0 | 19 |
| f1095a | gpt (gpt-6-astra) | 47 | 47 | 100.0% | 0/47 (0.0%) | pending | 0 | 0 | 0 | 19 |
| f2441 | deepseek (deepseek-flash) | 138 | 137 | 99.3% | 0/152 (0.0%) | pending | 0 | 0 | 1 | 66 |
| f4952 | deepseek (deepseek-flash) | 52 | 52 | 100.0% | 0/52 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f5329 | deepseek (deepseek-flash) | 21 | 21 | 100.0% | 0/21 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f5695 | deepseek (deepseek-flash) | 340 | 338 | 99.4% | 2/343 (0.6%) | pass | 2 | 0 | 0 | 236 |
| f8863 | deepseek (deepseek-flash) | 65 | 65 | 100.0% | 0/65 (0.0%) | pending | 0 | 0 | 0 | 2 |
| f8880 | deepseek (deepseek-flash) | 45 | 45 | 100.0% | 0/48 (0.0%) | pending | 0 | 0 | 0 | 39 |
| f8889 | deepseek (deepseek-flash) | 135 | 132 | 97.8% | 0/135 (0.0%) | pass | 0 | 3 | 0 | 0 |
| f8960 | deepseek (deepseek-flash) | 75 | 75 | 100.0% | 0/75 (0.0%) | pass | 0 | 0 | 0 | 0 |
| f8962 | deepseek (deepseek-flash) | 171 | 162 | 94.7% | 0/171 (0.0%) | pass | 0 | 0 | 9 | 0 |
| g28 | deepseek (deepseek-flash) | 3 | 3 | 100.0% | 0/3 (0.0%) | pending | 0 | 0 | 0 | 11 |
| person | deepseek (deepseek-flash) | 8 | 7 | 87.5% | 1/8 (12.5%) | pending | 0 | 1 | 0 | 0 |
| retirement | deepseek (deepseek-flash) | 50 | 50 | 100.0% | 0/50 (0.0%) | pass | 0 | 0 | 0 | 0 |
| s2 | deepseek (deepseek-flash) | 36 | 36 | 100.0% | 0/36 (0.0%) | pass | 0 | 0 | 0 | 0 |
| s3 | deepseek (deepseek-flash) | 30 | 30 | 100.0% | 0/30 (0.0%) | pending | 0 | 0 | 0 | 10 |
| s8812 | deepseek (deepseek-flash) | 129 | 129 | 100.0% | 0/129 (0.0%) | pass | 0 | 0 | 0 | 5 |
| sd | deepseek (deepseek-flash) | 41 | 41 | 100.0% | 0/41 (0.0%) | pending | 0 | 0 | 0 | 97 |
| u1250 | deepseek (deepseek-flash) | 18 | 18 | 100.0% | 0/18 (0.0%) | pass | 0 | 0 | 0 | 18 |
| w2 | deepseek (deepseek-flash) | 39 | 39 | 100.0% | 0/39 (0.0%) | pass | 0 | 0 | 0 | 0 |
| **all** | | 1902 | 1885 | 99.1% | | | 3 | 4 | 10 | 655 |

Pending clcw26 [deepseek]: 5 missing expected lines.
Pending eic [deepseek]: 19 missing expected lines; 50 unexpected line keys.
Pending f1040 [deepseek]: 7 missing expected lines.
Pending f1095a [deepseek]: 19 unexpected line keys.
Pending f1095a [gpt]: 19 unexpected line keys.
Pending f2441 [deepseek]: 2 missing expected lines.
Pending f8863 [deepseek]: 1 missing expected lines.
Pending f8880 [deepseek]: 3 missing expected lines.
Pending g28 [deepseek]: 11 missing expected lines.
Pending person [deepseek]: model-error noise above 10%.
Pending s3 [deepseek]: 10 missing expected lines.
Pending sd [deepseek]: 32 missing expected lines.

### Independence yield

| form | second family | line | second family's verdict | second family's reason |
| --- | --- | --- | --- | --- |
| f1095a | deepseek | classm.f1095a.1 — f1095a[mkt_b].line33c | DISAGREE | model gave $1,578.00; work: Given line 33, column C. |
| f5695 | deepseek | classm.f5695.11 — 14 | DISAGREE | model gave $0.00; work: 9,055.00 − 600.00 energy credit − 8,455.00 child tax credit − other 0 = 0.00; zero or less, enter -0- |
| f5695 | deepseek | classm.f5695.6 — 14 | DISAGREE | model gave $0.00; work: 6855 - (2300 + 4555) = 0; zero or less, enter -0-. |

### Lines both families disputed

| form | second family | line | Claude | second family | second family's reason |
| --- | --- | --- | --- | --- | --- |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line12 | DISAGREE | DISAGREE | model gave $5,031.25; work: Line 8 minus line 11: 5,031.25 - 0.00 = 5,031.25. |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line7 | DISAGREE | DISAGREE | model gave $750.00; work: Age 55+, married, family coverage 9 months: 1,000 x 9/12 = 750.00. |
| f8889 | deepseek | classm.f8889.2 — person[taxpayer].f8889[hsa].line8 | DISAGREE | DISAGREE | model gave $5,031.25; work: Line 6 plus line 7: 4,281.25 + 750.00 = 5,031.25. |
| person | deepseek | classm.person.1 — person[taxpayer].wages | DISAGREE | DISAGREE | model gave $29,524.00; work: Total W-2 wages: $29,524.00 + $0.00 = $29,524.00. |
