// usage: node timing.mjs <repo> <seed> <n>: CPU time of the bank-order walk and of one random traversal, per generated return
import { pathToFileURL } from "node:url";
const [repo, seedS, nS] = process.argv.slice(2);
const imp = (f) => import(pathToFileURL(`${repo}/engine/dist/${f}`).href);
const ir = await imp("interview-rules.js"); const gen = await imp("generate.js");
const ctx = ir.loadContext();
let tw = 0, tr = 0, nr = 0, complete = 0;
const rs = gen.sampleReturns(ctx.data, Number(nS), Number(seedS));
for (const [i, inputs] of rs.entries()) {
  const c = { id: `g${i}`, inputs };
  let t = process.cpuUsage(); const r = ir.runTask(ctx, { kind: "walk", profile: "full", c }); tw += process.cpuUsage(t).user;
  if (r.kind !== "walked") continue;
  if (r.w.status === "complete") complete++;
  t = process.cpuUsage(); ir.runTask(ctx, { kind: "random", profile: "full", group: "g", c, w: r.w, seed: 1 }); tr += process.cpuUsage(t).user; nr++;
}
console.log(`${rs.length} returns (${complete} complete): bank-order walk ${(tw / 1e6 / rs.length).toFixed(2)} s CPU each; one random traversal ${(tr / 1e6 / nr).toFixed(2)} s CPU each`);
