// Re-pin the keyed arguments' premise digests after a change to premiseDigest that is meant to move no argument's
// standing. Phase "before" (run with the old engine/dist): records, for each keyed argument with premises, the digest
// its premises have now. Phase "after" (run with the new engine/dist): for each recorded digest that appears as a
// literal in engine/src/mutate.ts, writes the new digest of the same premises in its place.
// An argument whose literal did not equal its premises' old digest (already stale) is left alone, and reported.
// Usage, from the repository root: node docs/provisional/lanes/g1-t3_work/repin.mjs before|after
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
process.argv.push("--year", "2025");
const root = process.cwd();
const { loadCanonical } = await import(resolve(root, "engine/dist/canonical.js"));
const M = await import(resolve(root, "engine/dist/mutate.js"));
const data = loadCanonical();
const phase = process.argv[2];
const state = "/tmp/repin-state.json";
const src = resolve(root, "engine/src/mutate.ts");
const entries = Object.entries(M.EQUIVALENT_IF).filter(([, c]) => c.premises);
if (phase === "before") {
  const text = readFileSync(src, "utf8");
  const out = entries.map(([id, c]) => ({ id, premises: c.premises, old: M.premiseDigest(data, c.premises) }));
  for (const e of out) if (!text.includes(`"${e.old}"`)) console.log(`not current (left alone): ${e.id}`);
  writeFileSync(state, JSON.stringify(out));
  console.log(`recorded ${out.length} arguments`);
} else if (phase === "after") {
  let text = readFileSync(src, "utf8");
  const recorded = JSON.parse(readFileSync(state, "utf8"));
  const map = new Map();
  for (const e of recorded) {
    const now = M.premiseDigest(data, e.premises);
    if (map.has(e.old) && map.get(e.old) !== now) throw new Error(`digest ${e.old} maps to two new digests`);
    map.set(e.old, now);
  }
  let n = 0;
  for (const [o, nw] of map) if (text.includes(`"${o}"`)) { text = text.split(`"${o}"`).join(`"${nw}"`); n++; }
  writeFileSync(src, text);
  console.log(`replaced ${n} digest literals`);
} else throw new Error("phase: before or after");
