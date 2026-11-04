// Scratch mutation harness (not shipped). Usage:
//   MUTATE_TIER=2 node /tmp/mut2/h.mjs run <idsfile|ALL> <out.jsonl> [workers]
//   MUTATE_TIER=2 node /tmp/mut2/h.mjs witness <id> [samples]
//   MUTATE_TIER=2 node /tmp/mut2/h.mjs ids
import { Worker, isMainThread, parentPort, workerData } from "node:worker_threads";
import { readFileSync, writeFileSync } from "node:fs";
const ROOT = "/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/agent-a6e970022fe3a8b6b/";
const WT = ROOT + "engine/dist/";
if (isMainThread) process.chdir(ROOT);
const { mutations, equivalenceReason } = await import(WT + "mutate.js");
const { loadCanonical } = await import(WT + "canonical.js");
const { evaluate, allTargets } = await import(WT + "eval.js");
const { loadCases } = await import(WT + "fixtures.js");
const { runChecks } = await import(WT + "check.js");
const { stableStringify } = await import(WT + "util.js");

const normal = (v) => v.kind === "refusal" ? stableStringify(v) : v.kind === "unknown" ? "unknown" : v.kind === "money" ? `money:${v.cents}`
  : v.kind === "rate" ? `rate:${v.num}/${v.den}` : `${v.kind}:${JSON.stringify(v.value)}`;
const canon = (k) => { const m = /\|inst:([^#]+)#/.exec(k); if (m) return `DEF:${m[1]}`; const s = k.replace(/\[[^\]]*\]/g, "").split("."); return s.slice(-2).join("."); };

function setup() {
  const baseline = loadCanonical();
  const cases = loadCases().cases;
  const muts = mutations(baseline);
  const derived = cases.map((c) => new Set([...evaluate(baseline, c.inputs, allTargets(baseline, c.inputs)).derivations.keys()].map(canon)));
  const defOf = new Map(); for (const d of baseline.defs) for (const l of d.lines) defOf.set(l.id, d.id);
  return { baseline, cases, muts, derived, defOf };
}
function outcome(S, m) {
  const data = JSON.parse(JSON.stringify(S.baseline));
  m.apply(data);
  if (runChecks(data).errors.length) return "check";
  const line = m.where.slice(m.where.indexOf(".") + 1);
  const def = S.defOf.get(line) ?? (S.baseline.defs.some((d) => d.id === m.where.split(".")[0]) ? m.where.split(".")[0] : undefined);
  const key = def ? `DEF:${def}` : line;
  const isParam = m.id.startsWith("param.") || m.id.startsWith("table.");
  for (let i = 0; i < S.cases.length; i++) {
    if (!isParam && !S.derived[i].has(key)) continue;
    const c = S.cases[i];
    const r = evaluate(data, c.inputs, allTargets(data, c.inputs));
    for (const [k, exp] of Object.entries(c.expect ?? {})) { const d = r.derivations.get(k); if (!d || normal(d.value) !== normal(exp)) return "fixtures"; }
  }
  return "survives";
}
const mode = process.argv[2];
if (!isMainThread && workerData.wbatch) {
  // Batch witness: for each mutant, the pool cases where a printed line differs.
  const { ids, index, n, pool } = workerData;
  const baseline = loadCanonical();
  const printed = new Map(); for (const d of [...baseline.forms, ...baseline.defs]) for (const l of d.lines) printed.set(l.id, l.printed !== "(helper)");
  const base = pool.map((c) => { try { return evaluate(baseline, c.inputs, allTargets(baseline, c.inputs)); } catch { return null; } });
  const defOf = new Map(); for (const d of baseline.defs) for (const l of d.lines) defOf.set(l.id, d.id);
  const muts = new Map(mutations(baseline).map((m) => [m.id, m]));
  const out = [];
  for (let i = index; i < ids.length; i += n) {
    const m = muts.get(ids[i]); const data = JSON.parse(JSON.stringify(baseline)); m.apply(data);
    const line = m.where.slice(m.where.indexOf(".") + 1); const key = defOf.get(line) ? `DEF:${defOf.get(line)}` : line;
    let hits = 0, helperOnly = 0; const examples = [];
    for (let j = 0; j < pool.length; j++) {
      const a = base[j]; if (!a) continue;
      if (![...a.derivations.keys()].some((k) => canon(k) === key)) continue;
      let b; try { b = evaluate(data, pool[j].inputs, allTargets(data, pool[j].inputs)); } catch { continue; }
      const diffs = [];
      for (const [k, d] of a.derivations) { const e = b.derivations.get(k); const x = normal(d.value), y = e ? normal(e.value) : "MISSING"; if (x !== y) diffs.push({ k, p: printed.get(canon(k)) ?? true, x: x.slice(0, 70), y: y.slice(0, 70) }); }
      if (!diffs.length) continue;
      const pd = diffs.filter((d) => d.p);
      if (pd.length) { hits++; if (examples.length < 2) examples.push({ c: pool[j].id, d: pd.slice(0, 6) }); } else helperOnly++;
    }
    out.push({ id: m.id, note: m.note, hits, helperOnly, examples });
  }
  parentPort.postMessage(out);
} else if (!isMainThread && workerData.fuzz) {
  // Fuzz around corpus cases: remove, flip or re-enumerate one input that the mutated line depends on.
  const { ids, index, n, pool, maxCases } = workerData;
  const baseline = loadCanonical();
  const all = [...baseline.forms, ...baseline.defs].flatMap((d) => d.lines);
  const byId = new Map(all.map((l) => [l.id, l]));
  const printed = new Map(all.map((l) => [l.id, l.printed !== "(helper)"]));
  const ids2 = new Set(all.map((l) => l.id));
  const refsOf = (node, out = []) => { if (typeof node === "string") { if (ids2.has(node)) out.push(node); } else if (Array.isArray(node)) node.forEach((x) => refsOf(x, out)); else if (node && typeof node === "object") for (const [k, v] of Object.entries(node)) if (!["ref", "collection", "const", "cite", "type", "op", "unit", "rule", "source", "label"].includes(k)) refsOf(v, out); return out; };
  const deps = (roots) => { const seen = new Set(); const st = [...roots]; while (st.length) { const x = st.pop(); if (seen.has(x)) continue; seen.add(x); const l = byId.get(x); if (!l) continue; st.push(...refsOf(l.expr), ...(l.refuses ?? []).map((r) => r.when)); if (l.expr.op === "sum_over") { const f = l.expr.field; if (f) st.push(f); } } return seen; };
  const muts = new Map(mutations(baseline).map((m) => [m.id, m]));
  const out = [];
  for (let i = index; i < ids.length; i += n) {
    const m = muts.get(ids[i]); const data = JSON.parse(JSON.stringify(baseline)); m.apply(data);
    const line = m.where.slice(m.where.indexOf(".") + 1);
    const [, x, y] = /^(\S+) -> (\S+) /.exec(m.note);
    const L = byId.get(line);
    const rel = deps([x, y, ...refsOf(L.expr), ...(L.refuses ?? []).map((r) => r.when)]);
    let tried = 0, hits = 0; const examples = []; let casesUsed = 0;
    for (const c of pool) {
      if (casesUsed >= maxCases || examples.length >= 2) break;
      let a; try { a = evaluate(baseline, c.inputs, allTargets(baseline, c.inputs)); } catch { continue; }
      if (![...a.derivations.keys()].some((k) => canon(k) === line)) continue;
      casesUsed++;
      const variants = [];
      for (const [k, v] of Object.entries(c.inputs)) {
        if (k.startsWith("$") || !rel.has(canon(k))) continue;
        const l = byId.get(canon(k));
        const del = { ...c.inputs }; delete del[k]; variants.push([`drop ${k}`, del]);
        if (typeof v === "boolean") variants.push([`flip ${k}`, { ...c.inputs, [k]: !v }]);
        if (l && l.type.startsWith("Enum(")) for (const e of baseline.params.enums[l.type.slice(5, -1)].values) if (e !== v) variants.push([`${k}=${e}`, { ...c.inputs, [k]: e }]);
        if (typeof v === "number") for (const nv of [0, v * 2 + 100000, Math.floor(v / 2)]) if (nv !== v && (l?.type === "Dollars" || nv >= 0)) variants.push([`${k}=${nv}`, { ...c.inputs, [k]: nv }]);
      }
      for (const [label, inputs] of variants) {
        tried++;
        let b0, b1; try { b0 = evaluate(baseline, inputs, allTargets(baseline, inputs)); b1 = evaluate(data, inputs, allTargets(data, inputs)); } catch { continue; }
        const pd = [];
        for (const [k, d] of b0.derivations) { if (!(printed.get(canon(k)) ?? true)) continue; const e = b1.derivations.get(k); const p = normal(d.value), q = e ? normal(e.value) : "MISSING"; if (p !== q) pd.push({ k, x: p.slice(0, 70), y: q.slice(0, 70) }); }
        if (pd.length) { hits++; if (examples.length < 2) examples.push({ c: c.id, v: label, d: pd.slice(0, 5) }); break; }
      }
    }
    out.push({ id: m.id, note: m.note, tried, hits, casesUsed, examples });
  }
  parentPort.postMessage(out);
} else if (!isMainThread) {
  const S = setup(); const { index, n, ids } = workerData;
  const want = ids ? new Set(ids) : null;
  const sel = S.muts.filter((m) => !want || want.has(m.id));
  const rows = [];
  for (let i = index; i < sel.length; i += n) {
    const m = sel[i]; const o = outcome(S, m);
    rows.push({ id: m.id, note: m.note, outcome: o, reason: o === "survives" ? (equivalenceReason(S.baseline, m) ?? null) : undefined });
  }
  parentPort.postMessage(rows);
} else if (mode === "run") {
  const idsArg = process.argv[3], out = process.argv[4], n = Number(process.argv[5] ?? 12);
  const ids = idsArg === "ALL" ? null : readFileSync(idsArg, "utf8").split("\n").filter(Boolean);
  const res = await Promise.all(Array.from({ length: n }, (_, index) => new Promise((ok, fail) => {
    const w = new Worker(new URL(import.meta.url), { workerData: { index, n, ids } });
    w.once("message", ok); w.once("error", fail);
  })));
  const rows = res.flat();
  writeFileSync(out, rows.map((r) => JSON.stringify(r)).join("\n") + "\n");
  const c = {};
  for (const r of rows) { const k = r.outcome + (r.outcome === "survives" ? (r.reason ? ":equiv" : ":UNEXPLAINED") : ""); c[k] = (c[k] ?? 0) + 1; }
  console.log(rows.length, JSON.stringify(c));
} else if (mode === "why") {
  const S = setup(); const m = S.muts.find((x) => x.id === process.argv[3]);
  const data = JSON.parse(JSON.stringify(S.baseline)); m.apply(data);
  console.log("checks", runChecks(data).errors.slice(0, 3));
  let n = 0;
  for (const c of S.cases) {
    const r = evaluate(data, c.inputs, allTargets(data, c.inputs));
    const b = evaluate(S.baseline, c.inputs, allTargets(S.baseline, c.inputs));
    for (const [k, exp] of Object.entries(c.expect ?? {})) { const d = r.derivations.get(k); const e = b.derivations.get(k); if (!d || normal(d.value) !== normal(exp)) { console.log(c.id, k, "exp", normal(exp).slice(0, 80), "mut", d ? normal(d.value).slice(0, 80) : "MISSING", "base", e ? normal(e.value).slice(0, 80) : "MISSING"); if (++n > 5) process.exit(0); } }
  }
} else if (mode === "explain") {
  const baseline = loadCanonical(); const muts = new Map(mutations(baseline).map((m) => [m.id, m]));
  const rows = readFileSync(process.argv[3], "utf8").split("\n").filter(Boolean).map((l) => JSON.parse(l)).filter((r) => r.outcome === "survives");
  let un = 0;
  for (const r of rows) {
    const reason = equivalenceReason(baseline, muts.get(r.id));
    if (!reason) { un++; console.log("UNEXPLAINED", r.id, r.note); }
    else if (process.env.V) console.log("EQ", r.id, reason.slice(0, Number(process.env.V)));
  }
  console.log(`survivors ${rows.length}, unexplained ${un}`);
} else if (mode === "wbatch") {
  const ids = readFileSync(process.argv[3], "utf8").split("\n").filter(Boolean);
  const ns = Number(process.argv[5] ?? 0), n = Number(process.argv[6] ?? 12);
  const baseline = loadCanonical();
  let pool = loadCases().cases.map((c) => ({ id: c.id, inputs: c.inputs }));
  if (ns) { const { sampleReturns } = await import(WT + "generate.js"); pool = pool.concat(sampleReturns(baseline, ns, Number(process.env.SEED ?? 7)).map((inputs, i) => ({ id: `gen${i}`, inputs }))); }
  if (process.env.EXTRA) pool = pool.concat(JSON.parse(readFileSync(process.env.EXTRA, "utf8")));
  const res = await Promise.all(Array.from({ length: n }, (_, index) => new Promise((ok, fail) => {
    const w = new Worker(new URL(import.meta.url), { workerData: { wbatch: true, ids, index, n, pool } });
    w.once("message", ok); w.once("error", fail);
  })));
  const rows = res.flat();
  writeFileSync(process.argv[4], rows.map((r) => JSON.stringify(r)).join("\n") + "\n");
  for (const r of rows) console.log(r.hits, r.helperOnly, r.id);
} else if (mode === "fuzz") {
  const ids = readFileSync(process.argv[3], "utf8").split("\n").filter(Boolean);
  const n = Number(process.argv[5] ?? 12), maxCases = Number(process.argv[6] ?? 25);
  const pool = loadCases().cases.map((c) => ({ id: c.id, inputs: c.inputs }));
  const res = await Promise.all(Array.from({ length: n }, (_, index) => new Promise((ok, fail) => {
    const w = new Worker(new URL(import.meta.url), { workerData: { fuzz: true, ids, index, n, pool, maxCases } });
    w.once("message", ok); w.once("error", fail);
  })));
  const rows = res.flat();
  writeFileSync(process.argv[4], rows.map((r) => JSON.stringify(r)).join("\n") + "\n");
  for (const r of rows) console.log(r.hits, r.tried, r.casesUsed, r.id, r.examples[0] ? `${r.examples[0].c} | ${r.examples[0].v} | ${r.examples[0].d.map((d) => d.k + " " + d.x.slice(0, 30) + "=>" + d.y.slice(0, 30)).join("; ")}` : "");
} else if (mode === "fcheck") {
  // Check mutation.json cases (id prefix) against the baseline, then which given mutants they kill.
  const baseline = loadCanonical(); const prefix = process.argv[3];
  const cases = loadCases().cases.filter((c) => c.id.startsWith(prefix));
  for (const c of cases) {
    const r = evaluate(baseline, c.inputs, allTargets(baseline, c.inputs));
    const bad = Object.entries(c.expect ?? {}).filter(([k, e]) => { const d = r.derivations.get(k); return !d || normal(d.value) !== normal(e); });
    console.log(bad.length ? "MISMATCH" : "ok", c.id, bad.map(([k, e]) => `${k}: expected ${normal(e).slice(0, 60)} got ${normal(r.derivations.get(k)?.value ?? { kind: "unknown" }).slice(0, 90)}`).join(" | "));
  }
  if (process.argv[4]) {
    const want = readFileSync(process.argv[4], "utf8").split("\n").filter(Boolean);
    const muts = new Map(mutations(baseline).map((m) => [m.id, m]));
    for (const id of want) {
      const m = muts.get(id); const data = JSON.parse(JSON.stringify(baseline)); m.apply(data);
      const killers = cases.filter((c) => { const r = evaluate(data, c.inputs, allTargets(data, c.inputs)); return Object.entries(c.expect ?? {}).some(([k, e]) => { const d = r.derivations.get(k); return !d || normal(d.value) !== normal(e); }); }).map((c) => c.id);
      console.log(killers.length ? "KILLED" : "survives", id, killers.slice(0, 3).join(","));
    }
  }
} else if (mode === "sound") {
  // Every killed mutant that a rule accepts as equivalent is a soundness failure of that rule.
  const baseline = loadCanonical(); const muts = mutations(baseline);
  let bad = 0, n = 0;
  const rows = process.argv[3] ? new Map(readFileSync(process.argv[3], "utf8").split("\n").filter(Boolean).map((l) => JSON.parse(l)).map((r) => [r.id, r.outcome])) : null;
  for (const m of muts) {
    if (rows && rows.get(m.id) !== "fixtures") continue;
    n++;
    const r = equivalenceReason(baseline, m);
    if (r) { bad++; console.log("ACCEPTED-BUT-KILLED", m.id, r.slice(0, 100)); }
  }
  console.log(`checked ${n} killed mutants, accepted ${bad}`);
} else if (mode === "ids") {
  console.log(mutations(loadCanonical()).map((m) => m.id).join("\n"));
} else if (mode === "witness") {
  const id = process.argv[3]; const ns = Number(process.argv[4] ?? 0);
  const baseline = loadCanonical(); const cases = loadCases().cases;
  const m = mutations(baseline).find((x) => x.id === id); if (!m) { console.log("no such mutant"); process.exit(1); }
  const data = JSON.parse(JSON.stringify(baseline)); m.apply(data);
  const printed = new Map(); for (const d of [...baseline.forms, ...baseline.defs]) for (const l of d.lines) printed.set(l.id, l.printed !== "(helper)");
  let pool = cases.map((c) => ({ id: c.id, inputs: c.inputs }));
  if (ns) { const { sampleReturns } = await import(WT + "generate.js"); pool = pool.concat(sampleReturns(baseline, ns, Number(process.env.SEED ?? 7)).map((inputs, i) => ({ id: `gen${i}`, inputs }))); }
  let shown = 0, anyDiff = 0, printedCases = 0;
  const helperOnly = [];
  for (const c of pool) {
    let a, b;
    try { a = evaluate(baseline, c.inputs, allTargets(baseline, c.inputs)); b = evaluate(data, c.inputs, allTargets(data, c.inputs)); } catch (e) { continue; }
    const diffs = [];
    for (const [k, d] of a.derivations) { const e = b.derivations.get(k); const x = normal(d.value), y = e ? normal(e.value) : "MISSING"; if (x !== y) diffs.push({ k, printed: printed.get(canon(k)) ?? "?", x: x.slice(0, 90), y: y.slice(0, 90) }); }
    if (!diffs.length) continue; anyDiff++;
    const pd = diffs.filter((d) => d.printed !== false);
    if (pd.length) printedCases++;
    if (pd.length && shown < Number(process.env.SHOW ?? 2)) { shown++; console.log("CASE", c.id, "printed diffs:"); for (const d of pd.slice(0, 14)) console.log("  ", d.k, d.x, "=>", d.y); }
    if (!pd.length && helperOnly.length < 1) helperOnly.push({ id: c.id, diffs: diffs.slice(0, 6) });
  }
  if (!shown && helperOnly.length) console.log("helper-only example", JSON.stringify(helperOnly[0]));
  console.log(`cases with any diff: ${anyDiff}; with printed diffs: ${printedCases}`);
}
