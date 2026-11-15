// Lane m3 helper: run the mutation check only on the mutants whose location is in the named documents, the same way
// engine/src/mutate.ts judges them (checker, then every federal fixture case), and print each survivor with whether
// an equivalence argument (keyed or structural) explains it. Usage:
//   node docs/provisional/lanes/m3/mutate_subset.mjs [--workers N] [--ids FILE] doc1 doc2 ...
// Not a substitute for `node engine/dist/main.js mutate`: it does not run the self-tests or the staleness check.
import { Worker, isMainThread, parentPort, workerData } from "node:worker_threads";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
const ROOT = resolve(import.meta.dirname, "../../../..");
const dist = (m) => import(resolve(ROOT, "engine/dist", m));

async function load(docs, ids) {
  const { loadCanonical } = await dist("canonical.js");
  const { mutations, equivalenceReason } = await dist("mutate.js");
  const baseline = loadCanonical();
  let muts = mutations(baseline).filter((m) => !/\bny[_.]/.test(m.where) && docs.has(m.where.split(".")[0]));
  if (ids) muts = muts.filter((m) => ids.has(m.id));
  return { baseline, muts, equivalenceReason };
}

if (isMainThread) {
  const args = process.argv.slice(2);
  let workers = 4, idsFile;
  const docs = new Set();
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--workers") workers = Number(args[++i]);
    else if (args[i] === "--ids") idsFile = args[++i];
    else docs.add(args[i]);
  }
  const ids = idsFile ? new Set(readFileSync(idsFile, "utf8").split(/\s+/).filter(Boolean)) : undefined;
  const { baseline, muts, equivalenceReason } = await load(docs, ids);
  const shares = await Promise.all(Array.from({ length: workers }, (_, index) => new Promise((done, fail) => {
    const w = new Worker(new URL(import.meta.url), { workerData: { index, count: workers, docs: [...docs], ids: ids ? [...ids] : null } });
    w.once("message", done); w.once("error", fail);
  })));
  const out = new Array(muts.length);
  for (const s of shares) for (const [i, o] of s) out[i] = o;
  let surv = 0, expl = 0;
  const lines = [];
  muts.forEach((m, i) => {
    if (out[i] !== "survives") return;
    surv++;
    const r = equivalenceReason(baseline, m);
    if (r) { expl++; return; }
    lines.push(`UNEXPLAINED ${m.id} | ${m.where} | ${m.note ?? ""}`);
  });
  muts.forEach((m, i) => { if (process.env.SHOW_ALL) lines.push(`${out[i]} ${m.id}`); });
  console.log(lines.join("\n"));
  console.log(`subset: ${muts.length} mutants in ${[...docs].join(",")}; ${surv} survive; ${expl} explained; ${surv - expl} unexplained`);
} else {
  const { index, count, docs, ids } = workerData;
  const { baseline, muts } = await load(new Set(docs), ids ? new Set(ids) : undefined);
  const { evaluate, allTargets } = await dist("eval.js");
  const { loadFixtureCases } = await dist("fixture-inputs.js");
  const { runChecks } = await dist("check.js");
  const { stableStringify } = await dist("util.js");
  const normal = (v) => v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
    : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;
  const cases = loadFixtureCases("federal", baseline).map((c) => {
    const expected = Object.keys(c.expect ?? {});
    const named = new Set(allTargets(baseline, c.inputs));
    return { ...c, targets: expected.every((t) => named.has(t)) ? expected : null };
  });
  const res = [];
  for (let i = index; i < muts.length; i += count) {
    const data = JSON.parse(JSON.stringify(baseline));
    muts[i].apply(data);
    if (runChecks(data).errors.length > 0) { res.push([i, "check"]); continue; }
    const kills = (c) => {
      const result = evaluate(data, c.inputs, c.targets ?? allTargets(data, c.inputs));
      for (const [key, expected] of Object.entries(c.expect ?? {})) {
        const der = result.derivations.get(key);
        if (!der || normal(der.value) !== normal(expected)) return true;
      }
      return false;
    };
    res.push([i, cases.some(kills) ? "fixtures" : "survives"]);
  }
  parentPort.postMessage(res);
}
