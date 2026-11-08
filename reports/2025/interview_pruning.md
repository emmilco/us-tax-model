# Interview pruning opportunities

Written by `node engine/dist/main.js interview-rules --write-pruning`. Each template below is a question the interview asks in bank order
that the complete return's evaluation then does not read: a later answer made it moot. Asking it is allowed (only reachability hides a
question), so these are not failures; each is a conjunction to rewrite as a nested choose, or an order that asks the deciding question
late. They are held in `walked_unused` of `tools/interview_rules_baseline.json`, so a new one fails until it is listed.

Over 78 complete returns (the Stage 5 and New York fixtures, generated returns and the minimal returns).

| Template | Returns | First return: input |
|---|---|---|
| `dependent.canada_mexico` | 7 | ny: New York fixtures: ny.schedule.hoh.95000: dependent[parent].canada_mexico |
| `dependent.disabled` | 2 | ny: New York fixtures: ny.status.qss.140000: dependent[daughter].disabled |
| `dependent.gross_income` | 2 | ny: New York fixtures: ny.status.qss.140000: dependent[daughter].gross_income |
| `dependent.months` | 5 | ny: New York fixtures: ny.schedule.hoh.95000: dependent[parent].months |
| `dependent.multiple_support` | 2 | ny: New York fixtures: ny.status.qss.140000: dependent[daughter].multiple_support |
| `dependent.supported` | 2 | ny: New York fixtures: ny.status.qss.140000: dependent[daughter].supported |
| `eic.qc_of_another` | 4 | minimal: full: every gate closed: eic.qc_of_another |
| `household.home_cost` | 5 | ny: New York fixtures: ny.schedule.hoh.95000: household.home_cost |
| `person.sav_excess` | 4 | ny: New York fixtures: ny.official.tax_table_38275: person[spouse].sav_excess |
| `person.work_ssn` | 18 | ny: New York fixtures: ny.official.tax_table_38275: person[spouse].work_ssn |
| `s8812.combat_pay` | 76 | full: Stage 5 fixtures: stage5.return.owed: s8812.combat_pay |
