import { m1Run } from "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/provisional-m1/engine/dist/_m1_mutate.js";
const forms = (process.argv[2] ?? "person,ira,f5329,f8606,f8880,f8889,retirement,ssb").split(",");
const r = await m1Run(forms);
console.log(`mine: ${r.total} mutants, killed ${r.killed}, equivalent ${r.equivalent.length}, unexplained ${r.unexplained.length}, stale ${r.stale.length}`);
for (const u of r.unexplained) console.log("UNEXPLAINED " + u);
for (const s of r.stale) console.log("STALE " + s);
