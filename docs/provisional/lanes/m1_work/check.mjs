import { readFileSync, writeFileSync } from "node:fs";
import { m1Check } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/_m1_mutate.js";
const specs = JSON.parse(readFileSync(process.argv[2], "utf8"));
const res = m1Check(specs);
for (const r of res) { const { inputs, ...rest } = r; console.log(JSON.stringify(rest, null, 1)); }
if (process.argv[3]) writeFileSync(process.argv[3], JSON.stringify(res.map((r) => ({ id: r.id, inputs: r.inputs })), null, 1));
