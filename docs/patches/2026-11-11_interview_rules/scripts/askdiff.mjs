// usage: node askdiff.mjs <base repo> <patched repo> <returns.json>: per return, the questions asked in bank order by one and not the other
import { pathToFileURL } from "node:url";
import { readFileSync } from "node:fs";
const [A, B, file] = process.argv.slice(2);
const load = async (repo) => { const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href); const ir = await imp("interview-rules.js"); const gen = await imp("generate.js"); return { ir, gen, ctx: ir.loadContext() }; };
const a = await load(A), b = await load(B);
for (const [seed, i] of JSON.parse(readFileSync(file, "utf8"))) {
  const inputs = a.gen.sampleReturns(a.ctx.data, i + 1, seed)[i];
  const c = { id: "x", inputs };
  const ra = a.ir.runTask(a.ctx, { kind: "walk", profile: "full", c }), rb = b.ir.runTask(b.ctx, { kind: "walk", profile: "full", c });
  if (ra.kind !== "walked" || rb.kind !== "walked") continue;
  const ka = new Set(ra.w.events.map((e) => e.input)), kb = new Set(rb.w.events.map((e) => e.input));
  const onlyA = [...ka].filter((k) => !kb.has(k)), onlyB = [...kb].filter((k) => !ka.has(k));
  if (onlyA.length || onlyB.length) console.log(`${seed}.${i} ${ra.w.status}: no longer asked ${JSON.stringify(onlyA)}; newly asked ${JSON.stringify(onlyB)}`);
}
