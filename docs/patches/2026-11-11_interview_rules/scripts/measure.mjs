// usage: node measure.mjs <repo> <returns.json> <out.json>
// returns.json: [[seed, i], ...] generated federal returns to recheck. Writes, per return: status, questions asked in
// bank order, the unread / out-of-order / random-reached / early templates and order errors; and for the standard
// interview-length set of the full profile (Stage 5 whole-return fixtures, the 12 seed-11 generated returns, the
// minimal returns) the questions asked in bank order.
import { pathToFileURL } from "node:url";
import { readFileSync, writeFileSync } from "node:fs";
const [repo, file, outFile] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js"); const gen = await imp("generate.js");
const { questionTemplate, inputMeta } = await imp("interview.js");
const ctx = ir.loadContext(); const { data, configs } = ctx; const config = configs.full;
const T = (ks) => [...new Set(ks.map(questionTemplate))].sort();
const want = JSON.parse(readFileSync(file, "utf8"));
const bySeed = new Map(); for (const [s, i] of want) (bySeed.get(s) ?? bySeed.set(s, []).get(s)).push(i);
const out = { returns: {}, standard: {} };
for (const [seed, idx] of bySeed) {
  const rs = gen.sampleReturns(data, Math.max(...idx) + 1, seed);
  for (const i of idx) {
    const c = { id: `s${seed}.${i}`, inputs: rs[i] };
    const r = ir.runTask(ctx, { kind: "walk", profile: "full", c });
    const row = { kind: r.kind };
    if (r.kind === "walked") {
      row.status = r.w.status; row.asked = r.w.events.length; row.valuesKey = r.w.valuesKey; row.early = T(r.leaks.flat());
      row.unread = r.classes ? T(r.classes.askedUnread) : []; row.out = r.classes ? T(Object.keys(r.classes.outOfOrder)) : [];
      row.reached = []; row.randomEarly = []; row.errors = [];
      for (let s = 0; s < 5; s++) { const x = ir.runTask(ctx, { kind: "random", profile: "full", group: "g", c, w: r.w, seed: seed * 1000 + i + s * 100003 }); row.reached.push(...T(x.reached)); row.randomEarly.push(...T(x.leaks.flat())); row.errors.push(...x.errors); }
      row.reached = [...new Set(row.reached)].sort(); row.randomEarly = [...new Set(row.randomEarly)].sort();
    } else row.detail = r.kind === "unanswered" ? r.input : r.error;
    out.returns[`${seed}.${i}`] = row;
  }
}
const std = [...ir.fixtureCases("full", data).map((c) => ({ id: c.id, t: { kind: "walk", profile: "full", c } })),
  ...gen.sampleReturns(data, 12, 11).map((inputs, i) => ({ id: `generated.${i}`, t: { kind: "walk", profile: "full", c: { id: `generated.${i}`, inputs } } })),
  { id: "minimal.closed", t: { kind: "minimal", profile: "full", open: null } }];
const closed = ir.runTask(ctx, std.at(-1).t);
if (closed.kind === "walked") {
  const asked = new Map(closed.w.events.map((e) => [e.input, e.value]));
  for (const g of [...ir.existenceGates(data).keys()].sort()) {
    if (!asked.has(g)) continue;
    const meta = inputMeta(data, g);
    for (const value of meta.type === "Bool" ? [true] : (meta.values ?? []).filter((v) => v !== asked.get(g))) std.push({ id: `minimal.${g}=${value}`, t: { kind: "minimal", profile: "full", open: { input: g, value } } });
  }
}
for (const { id, t } of std) { const r = ir.runTask(ctx, t); out.standard[id] = r.kind === "walked" ? { status: r.w.status, asked: r.w.events.length, valuesKey: r.w.valuesKey } : { status: r.kind }; }
writeFileSync(outFile, JSON.stringify(out));
console.log(`measured ${Object.keys(out.returns).length} returns and ${Object.keys(out.standard).length} standard walks`);
