import { premiseDigest } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/mutate.js";
import { loadCanonical } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/canonical.js";
const d = loadCanonical();
for (const a of process.argv.slice(2)) console.log(premiseDigest(d, a.split(",")), a.slice(0, 80));
