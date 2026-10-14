# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and a deterministic set of 200 generated inputs were evaluated
by both independently written evaluators; every line of f1040 and qdcg was compared
(money cents, booleans, enums; unknowns compared by kind).

| Metric | Value |
| --- | --- |
| Cases | 259 |
| Line values compared | 8547 |
| Cases with differences | 0 |
| Result | **agreement on every value** |
