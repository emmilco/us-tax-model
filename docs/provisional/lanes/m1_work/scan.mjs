import { m1Scan } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/_m1_mutate.js";
const [keys, filt] = [process.argv[2].split(","), process.argv[3]];
for (const r of m1Scan(keys, filt)) console.log(r.join(" | "));
