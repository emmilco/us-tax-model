import { readFileSync, writeFileSync } from "node:fs";
import { m1Probe } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/_m1_mutate.js";
const spec = JSON.parse(readFileSync(process.argv[2], "utf8"));
const { out, inputs } = m1Probe(spec);
console.log(JSON.stringify(out, null, 1));
if (process.argv[3]) writeFileSync(process.argv[3], JSON.stringify(inputs, null, 1));
