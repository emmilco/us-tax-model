// Lane m4 scratch driver: the mutation judgement of engine/dist/mutate.js for a subset of mutants (by first
// document segment of the mutant's location, or by an id list), spread over child processes. It loads a copy of
// mutate.js that also exports the internals the full run keeps private; the judgement itself is mutate.js's own.
//   node mut.mjs [--ny] --docs f5695,sc,ny_* [--ids FILE] [--jobs 4] [--out FILE.json]
import { readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { spawn } from "node:child_process";
const ARGV = [...process.argv];
const ROOT = resolve(import.meta.dirname, "../../../..");
const DIST = join(ROOT, "engine/dist");
const arg = (k, d) => { const i = process.argv.indexOf(k); return i < 0 ? d : process.argv[i + 1]; };
const shard = arg("--shard");
const tmp = join(DIST, "_m4mutate.js");
if (!shard) {
  const src = readFileSync(join(DIST, "mutate.js"), "utf8");
  writeFileSync(tmp, src + "\nexport { outcome as _outcome, judgingCases as _judgingCases, selectMutants as _selectMutants, EQUIVALENT_IF as _EQ, OPEN_DEFECT_SURVIVORS as _OPEN, ANSWERED_ONLY as _AO };\n");
}
const M = await import(tmp);
const { loadCanonical } = await import(join(DIST, "canonical.js"));
const docs = (arg("--docs", "") || "").split(",").filter(Boolean);
const idsFile = arg("--ids");
const ids = idsFile ? new Set(readFileSync(idsFile, "utf8").split("\n").map((s) => s.trim()).filter(Boolean)) : null;
const first = (where) => where.replace(/\[[^\]]*\]/g, "").split(".")[0];
const mineWhere = (where) => docs.some((d) => (d.endsWith("*") ? first(where).startsWith(d.slice(0, -1)) : first(where) === d));
const mine = (m) => (ids ? ids.has(m.id) : mineWhere(m.where));

const baseline = loadCanonical();
const all = M._selectMutants(M.mutations(baseline));
const muts = all.filter(mine);

if (shard) {
  const [i, n] = shard.split("/").map(Number);
  const cases = M._judgingCases(baseline);
  const out = [];
  for (let k = i; k < muts.length; k += n) out.push([muts[k].id, M._outcome(baseline, cases, muts[k])]);
  process.stdout.write(JSON.stringify(out));
} else {
  const jobs = Number(arg("--jobs", "4"));
  const passthru = ARGV.slice(2).filter((a, k, xs) => a !== "--jobs" && xs[k - 1] !== "--jobs" && a !== "--out" && xs[k - 1] !== "--out");
  const results = await Promise.all(Array.from({ length: jobs }, (_, i) => new Promise((done, fail) => {
    const p = spawn(process.execPath, [import.meta.filename, ...passthru, "--shard", `${i}/${jobs}`], { stdio: ["ignore", "pipe", "inherit"] });
    let s = ""; p.stdout.on("data", (d) => (s += d));
    p.on("exit", (c) => (c === 0 ? done(JSON.parse(s)) : fail(new Error(`shard ${i} exit ${c}`))));
  })));
  const outcome = new Map(results.flat());
  const byId = new Map(muts.map((m) => [m.id, m]));
  const survivors = muts.filter((m) => outcome.get(m.id) === "survives");
  const unexplained = [], explained = [];
  for (const s of survivors) {
    const r = M.equivalenceReason(baseline, s);
    if (r || s.id in M._OPEN) explained.push(s); else unexplained.push(s);
  }
  // Stale arguments about these mutants (same tests as staleEquivalences, restricted to this subset).
  const survivorIds = new Set(survivors.map((s) => s.id));
  const stale = [];
  for (const [id, c] of Object.entries(M._EQ)) {
    const m = byId.get(id);
    if (!m) { const known = all.find((x) => x.id === id); if (!known && (ids ? ids.has(id) : docs.some((d) => id.includes(`.${d.replace("*", "")}`)))) stale.push(`${id}: no mutant has this id`); continue; }
    if (!survivorIds.has(id)) stale.push(`${id}: killed`);
    else if (c.reads !== undefined && c.reads !== m.replacement) stale.push(`${id}: reads ${m.replacement}, argument says ${c.reads}`);
    else if (!c.holds(baseline)) stale.push(`${id}: no longer holds`);
  }
  const summary = { mutants: muts.length, check: [...outcome.values()].filter((o) => o === "check").length,
    killed: [...outcome.values()].filter((o) => o !== "survives" && o !== "check").length, survivors: survivors.length,
    explained: explained.length, unexplained: unexplained.length, stale: stale.length };
  console.log(JSON.stringify(summary));
  for (const s of stale) console.log(`STALE ${s}`);
  for (const s of unexplained) console.log(`OPEN ${s.id}\t${s.kind}\t${s.where}\t${s.note ?? ""}`);
  const out = arg("--out");
  if (out) writeFileSync(out, JSON.stringify({ summary, stale, unexplained: unexplained.map((s) => ({ id: s.id, kind: s.kind, where: s.where, note: s.note })), outcomes: Object.fromEntries(outcome) }, null, 1));
}
