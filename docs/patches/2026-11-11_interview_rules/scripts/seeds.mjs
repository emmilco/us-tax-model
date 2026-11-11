// usage: node seeds.mjs <repo> <profile full|ny> <seed> <n> [dumpIndex]
// Generates n returns with the given fast-check seed (the tool's own sampleReturns / nyReturnArbitrary), walks each in
// bank order (runTask kind walk) and in 5 random orders (kind random), and prints one JSON line per return.
import { pathToFileURL } from "node:url";
import { writeFileSync } from "node:fs";
const [repo, profile, seedS, nS, dump] = process.argv.slice(2);
const seed = Number(seedS), n = Number(nS);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js");
const gen = await imp("generate.js");
const { questionTemplate } = await imp("interview.js");
const fc = (await import(pathToFileURL(`${repo}/node_modules/fast-check/lib/fast-check.js`).href).catch(() => import(pathToFileURL(`${repo}/node_modules/fast-check/lib/esm/fast-check.js`).href)));
const ctx = ir.loadContext();
const t0 = performance.now();
const returns = profile === "full" ? gen.sampleReturns(ctx.data, n, seed) : (fc.default ?? fc).sample(gen.nyReturnArbitrary(ctx.data), { seed, numRuns: n });
const tGen = performance.now() - t0;
const T = (ks) => [...new Set(ks.map(questionTemplate))].sort();
returns.forEach((inputs, i) => {
  if (dump !== undefined && Number(dump) === i) writeFileSync(`/tmp/f1095a/out/return_${profile}_${seed}_${i}.json`, JSON.stringify(inputs, null, 1));
  const c = { id: `generated.${i}`, inputs };
  const t1 = performance.now();
  const r = ir.runTask(ctx, { kind: "walk", profile, c });
  const row = { profile, seed, i, kind: r.kind, f1095a: (inputs["$f1095a"] ?? []).length, uniform: (inputs["$f1095a"] ?? []).map((k) => inputs[`f1095a[${k}].uniform`]) };
  if (r.kind === "walked") {
    row.status = r.w.status; row.states = r.w.states; row.early = T(r.leaks.flat()); row.bad = r.bad;
    if (r.classes) { row.outOfOrder = Object.fromEntries(Object.entries(r.classes.outOfOrder).map(([k, by]) => [k, by])); row.askedUnread = r.classes.askedUnread; row.readUnasked = r.classes.readUnasked; }
    if (process.env.SKIP_REFUSED && r.w.status !== "complete") { row.ms = Math.round(performance.now() - t1); console.log(JSON.stringify(row)); return; }
    const o = ir.runTask(ctx, { kind: "order", profile, group: "g", c, w: r.w });
    row.orderErrors = o.errors;
    row.reached = []; row.randomErrors = []; row.randomEarly = [];
    for (let s = 0; s < 5; s++) {
      const x = ir.runTask(ctx, { kind: "random", profile, group: "g", c, w: r.w, seed: seed * 1000 + i + s * 100003 });
      row.reached.push(...x.reached); row.randomErrors.push(...x.errors); row.randomEarly.push(...T(x.leaks.flat()));
    }
    row.reached = [...new Set(row.reached)].sort(); row.randomEarly = [...new Set(row.randomEarly)].sort();
    const sub = ir.runTask(ctx, { kind: "subsets", profile, w: r.w, seed: seed * 7919 + i });
    row.subsetEarly = T(sub.leaks.flat());
  } else row.detail = r.kind === "unanswered" ? r.input : r.error;
  row.ms = Math.round(performance.now() - t1);
  console.log(JSON.stringify(row));
});
console.error(`seed ${seed} ${profile}: ${n} returns, generate ${(tGen / 1000).toFixed(1)} s, total ${((performance.now() - t0) / 1000).toFixed(1)} s`);
