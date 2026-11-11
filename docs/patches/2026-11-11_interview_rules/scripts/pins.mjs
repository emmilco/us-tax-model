// usage: node pins.mjs <base repo> <patched repo>: of the pinned mutation arguments in the base's engine/src/mutate.ts
// (premise line lists with a 16-hex digest), how many hold on the base data and how many of those move on the patched data
import { pathToFileURL } from "node:url";
import { readFileSync } from "node:fs";
const [A, B] = process.argv.slice(2);
const load = async (repo) => { const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href); const { loadCanonical } = await imp("canonical.js"); const m = await imp("mutate.js"); return { data: loadCanonical(), premiseDigest: m.premiseDigest }; };
const a = await load(A), b = await load(B);
const src = readFileSync(`${A}/engine/src/mutate.ts`, "utf8");
const re = /\[((?:\s*"[^"\]]+"\s*,?)+)\]\s*,\s*"([0-9a-f]{16})"/g;
let m, n = 0, live = 0, moved = []; const seen = new Set();
while ((m = re.exec(src))) {
  const lines = [...m[1].matchAll(/"([^"]+)"/g)].map((x) => x[1]); const digest = m[2];
  const k = lines.join(",") + digest; if (seen.has(k)) continue; seen.add(k); n++;
  if (a.premiseDigest(a.data, lines) !== digest) continue;
  live++;
  if (b.premiseDigest(b.data, lines) !== digest) moved.push(lines.join(", "));
}
console.log(`pins: ${n} distinct premise lists found in mutate.ts, ${live} hold on the base data, ${moved.length} of those move on the patched data`);
for (const x of moved) console.log(`   un-pinned: premises ${x}`);
