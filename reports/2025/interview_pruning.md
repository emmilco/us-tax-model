# Interview pruning opportunities

Written by `node engine/dist/main.js interview-rules --write-pruning`. Each template below is a question the interview asks in bank order
that the complete return's evaluation then does not read: a later answer made it moot. Asking it is allowed (only reachability hides a
question), so these are not failures; each is a conjunction to rewrite as a nested choose, or an order that asks the deciding question
late. They are held in `walked_unused` of `tools/interview_rules_baseline.json`, so a new one fails until it is listed.

Over 78 complete returns (the Stage 5 and New York fixtures, generated returns and the minimal returns).

| Template | Returns | First return: input |
|---|---|---|
