// usage: node order_status.mjs <repo> <seed> <i> <key> <json value> [more key value ...]
// The generated return with the given answers changed: its status walked in bank order, and in the tool's 5 random
// orders over the same answers (runTask kind random, which reports "a random answering order gives a different status").
import { pathToFileURL } from "node:url";
const [repo, seedS, iS, ...kv] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js"); const gen = await imp("generate.js");
const ctx = ir.loadContext();
const seed = Number(seedS), i = Number(iS);
const inputs = { ...gen.sampleReturns(ctx.data, i + 1, seed)[i] };
for (let k = 0; k < kv.length; k += 2) inputs[kv[k]] = JSON.parse(kv[k + 1]);
const c = { id: `s${seed}.${i}`, inputs };
const r = ir.runTask(ctx, { kind: "walk", profile: "full", c });
console.log(`bank order: ${r.kind === "walked" ? r.w.status + ", " + r.w.events.length + " questions; asked the changed key(s): " + kv.filter((_, n) => n % 2 === 0).map((k) => `${k} ${r.w.events.some((e) => e.input === k)}`).join(", ") : r.kind}`);
if (r.kind === "walked") for (let s = 0; s < 5; s++) { const x = ir.runTask(ctx, { kind: "random", profile: "full", group: "g", c, w: r.w, seed: seed * 1000 + i + s * 100003 }); console.log(`random order ${s}: ${x.errors.length ? x.errors.join("; ") : "same status and values"}`); }
// A directed order: the same answers, asked in bank order except that the changed key(s) are put off for as long as any other question is open.
if (r.kind === "walked") {
  const { replay } = await imp("interview.js");
  const config = ctx.configs.full;
  const given = replay(config, [{ version: 1, tax_year: config.tax_year }, ...r.w.events]);
  const keys = new Set(kv.filter((_, n) => n % 2 === 0));
  const bank = ir.bankOrder(config);
  const w2 = ir.walk(ctx.data, config, (k) => (k in given ? { value: given[k] } : undefined), (open) => { const rest = open.filter((k) => !keys.has(k)); return bank(rest.length ? rest : open); }, 800, () => {}, () => {});
  console.log(`directed order (changed key last): ${w2.status}, ${w2.events.length} questions; asked the changed key(s): ${[...keys].map((k) => `${k} ${w2.events.some((e) => e.input === k)}`).join(", ")}; values ${w2.valuesKey === r.w.valuesKey ? "same" : "DIFFERENT"} as bank order`);
}
