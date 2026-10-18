// Class M jobs: for each document with printed lines, a small set of generated
// returns that together take every reachable branch of the document, with the
// values that flow into the document from elsewhere. An isolated model works
// the document by hand from those values and its archived pages
// (tools/transcription/classm.py); the agreements become class M fixtures.
// A keyed collection is worked once per entry: every computed line the
// evaluation reached for each entry, from the entry's own inputs. A shared
// definition is worked per instance (an amount and a filing status drawn from
// the generated returns): its gate tests and its result.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { evaluateAll } from "./eval.js";
import type { EvalResult, Value } from "./eval.js";
import { sampleReturns } from "./generate.js";
import { branchKeys } from "./branches.js";
import type { CanonicalData, Expr, FormDoc, Inputs, Line, Operand, TestExpr } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const SEED = 7;

interface Given { ref: string; doc: string; printed: string; label: string; value: Value; note?: string }
interface EntryField { field: string; label: string; value: Value }
interface Job {
  id: string;
  doc: string;
  inputs: Inputs;
  status: string;
  given: Given[];
  own_inputs: { id: string; printed: string; source: string; value: Value }[];
  collections: Record<string, Record<string, EntryField[]>>;
  fill: { id: string; printed: string; type: string; label: string; entry?: string }[];
  project: Record<string, Value>;
  branches: string[];
  /** "collection": the document is worked once per entry; "def": one instance of a shared definition. */
  kind?: "collection" | "def";
  entries?: Record<string, EntryField[]>;
}

function isHelper(line: Line): boolean { return line.printed.startsWith("("); }

/** Every operand string in an expression, with the def references and collection sums seen. */
function walk(expr: Expr | TestExpr, out: { refs: Set<string>; defs: boolean; sums: { collection: string; field: string; where: Set<string> }[] }): void {
  const op = (o: Operand | undefined) => { if (typeof o === "string") out.refs.add(o); };
  const e = expr as Record<string, unknown> & { op: string };
  switch (e.op) {
    case "copy": if (typeof e["from"] === "string") out.refs.add(e["from"] as string); else { out.defs = true; for (const v of Object.values((e["from"] as { bind: Record<string, Operand> }).bind)) op(v); } break;
    case "sum": case "smaller_of": case "larger_of": for (const r of e["of"] as string[]) out.refs.add(r); break;
    case "subtract": case "subtract_floor0": out.refs.add(e["from"] as string); op(e["take"] as Operand); break;
    case "multiply_rate": out.refs.add(e["amount"] as string); op(e["rate"] as Operand); break;
    case "table_lookup": case "bracket_schedule": out.refs.add(e["key"] as string); out.refs.add(e["status"] as string); break;
    case "round": out.refs.add(e["of"] as string); break;
    case "multiply_count": out.refs.add(e["amount"] as string); out.refs.add(e["count"] as string); break;
    case "choose": for (const alt of e["alternatives"] as { guard: TestExpr; then: unknown }[]) { walk(alt.guard, out); if (typeof alt.then === "string") out.refs.add(alt.then); else { out.defs = true; for (const v of Object.values((alt.then as { bind: Record<string, Operand> }).bind)) op(v); } } break;
    case "sum_over": { const w = new Set<string>(); if (e["where"]) { const inner = { refs: w, defs: false, sums: [] }; walk(e["where"] as TestExpr, inner); } out.sums.push({ collection: e["collection"] as string, field: e["field"] as string, where: w }); break; }
    case "test": {
      if ("all" in e) for (const t of e["all"] as TestExpr[]) walk(t, out);
      else if ("any" in e) for (const t of e["any"] as TestExpr[]) walk(t, out);
      else if ("not" in e) walk(e["not"] as TestExpr, out);
      else for (const k of ["eq", "ne", "lt", "le", "gt", "ge"]) { const pair = e[k] as [Operand, Operand] | undefined; if (pair) { op(pair[0]); op(pair[1]); } }
      break;
    }
    default: break;
  }
}

function roundInputs(inputs: Inputs, data: CanonicalData): Inputs {
  // Whole-dollar amounts, so the hand-work and the project share the page's units.
  const out: Inputs = {};
  for (const [k, v] of Object.entries(inputs)) out[k] = typeof v === "number" && !k.startsWith("$") && !isCount(k, data) ? Math.round(v / 100) * 100 : v;
  return out;
}
function isCount(key: string, data: CanonicalData): boolean {
  const id = key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, (m) => m.split(".").filter(Boolean).at(-1)!.split("[")[0] + ".");
  for (const doc of data.forms) { const l = doc.lines.find((x) => x.id === id); if (l) return l.type === "Count"; }
  return false;
}

function computed(v: Value | undefined): boolean { return !!v && (v.kind === "money" || v.kind === "bool" || v.kind === "count" || v.kind === "enum"); }

function docKeys(doc: FormDoc): string[] {
  const keys: string[] = [];
  for (const line of doc.lines) {
    const e = line.expr as Expr;
    if (e.op === "choose") e.alternatives.forEach((_, i) => keys.push(`${line.id}#${i}`));
    if (line.type === "Bool") keys.push(`${line.id}:false`, `${line.id}:true`);
    if (e.op === "subtract_floor0") keys.push(`${line.id}:floor`, `${line.id}:positive`);
    if (e.op === "smaller_of" || e.op === "larger_of") keys.push(`${line.id}:left`, `${line.id}:right`);
  }
  return keys;
}

function buildJob(data: CanonicalData, doc: FormDoc, inputs: Inputs, r: EvalResult, n: number, branches: string[], entryLevel = false): Job | null {
  const byId = new Map<string, { doc: FormDoc; line: Line }>();
  for (const d of data.forms) for (const l of d.lines) byId.set(l.id, { doc: d, line: l });
  const refs = new Set<string>(); const sums: { collection: string; field: string; where: Set<string> }[] = [];
  const defLines: Line[] = [];
  for (const line of doc.lines) {
    const out = { refs: new Set<string>(), defs: false, sums: [] as typeof sums };
    walk(line.expr as Expr, out);
    for (const x of out.refs) refs.add(x);
    sums.push(...out.sums);
    if (out.defs) defLines.push(line);
  }
  const given: Given[] = [];
  const val = (id: string) => r.derivations.get(id)?.value;
  for (const ref of [...refs].sort()) {
    const hit = byId.get(ref);
    if (!hit || hit.doc.id === doc.id) continue;
    if (hit.doc.collection) continue; // collection fields are given per entry below
    const v = val(ref);
    if (!computed(v)) return null;
    given.push({ ref, doc: hit.doc.id, printed: hit.line.printed, label: hit.line.label, value: v! });
  }
  for (const line of defLines) {
    const v = val(line.id);
    if (!computed(v)) return null;
    given.push({ ref: line.id, doc: doc.id, printed: line.printed, label: line.label, value: v!, note: "result of the shared tax computation (Tax Table or Tax Computation Worksheet), given rather than worked" });
  }
  const status = inputs["f1040.status"] as string;
  const own_inputs = entryLevel ? [] : doc.lines.filter((l) => l.expr.op === "input").map((l) => ({ id: l.id, printed: l.printed, source: (l.expr as { source: string }).source, value: val(l.id)! }));
  if (own_inputs.some((o) => !computed(o.value))) return null;
  // Collections: every entry of each summed collection, with the summed field and the fields its filter reads.
  const collections: Record<string, Record<string, EntryField[]>> = {};
  for (const s of sums) {
    const cdoc = data.forms.find((d) => d.id === s.collection)!;
    const fields = new Set<string>([s.field, ...s.where]);
    // Entries are the derivation keys of the form `<prefix>.<collection>[<key>].<field>`.
    for (const [key, der] of r.derivations) {
      const m = key.match(new RegExp(`^(.*${s.collection}\\[[^\\]]+\\])\\.([a-z0-9_]+)$`));
      if (!m) continue;
      const fid = `${s.collection}.${m[2]}`;
      if (!fields.has(fid)) continue;
      const entry = m[1]!;
      const label = cdoc.lines.find((l) => l.id === fid)?.label ?? fid;
      (collections[s.collection] ??= {})[entry] ??= [];
      if (!computed(der.value)) return null;
      collections[s.collection]![entry]!.push({ field: fid, label, value: der.value });
    }
  }
  if (entryLevel) return { id: `classm.${doc.id}.${n}`, doc: doc.id, inputs, status, given, own_inputs: [], collections, fill: [], project: {}, branches };
  const fill = doc.lines.filter((l) => !isHelper(l) && l.expr.op !== "input" && !defLines.includes(l)).map((l) => ({ id: l.id, printed: l.printed, type: l.type, label: l.label }));
  const project: Record<string, Value> = {};
  for (const l of fill) { const v = val(l.id); if (!computed(v)) return null; project[l.id] = v!; }
  return { id: `classm.${doc.id}.${n}`, doc: doc.id, inputs, status, given, own_inputs, collections, fill, project, branches };
}

/** The entries of collection `id` in a result: entry prefix -> field id -> derivation key. */
function entriesOf(id: string, r: EvalResult): Map<string, Map<string, string>> {
  const out = new Map<string, Map<string, string>>();
  const re = new RegExp(`^((?:.*\\.)?${id}\\[[^\\]]+\\])\\.([a-z0-9_]+)$`);
  for (const key of r.derivations.keys()) {
    const m = key.match(re);
    if (!m) continue;
    if (!out.has(m[1]!)) out.set(m[1]!, new Map());
    out.get(m[1]!)!.set(`${id}.${m[2]}`, key);
  }
  return out;
}

/** Lines of a collection worked by hand: every computed line except year constants. */
function collectionFill(doc: FormDoc): Line[] { return doc.lines.filter((l) => l.expr.op !== "input" && l.expr.op !== "param"); }

/** A collection document worked once per entry, for one generated return. */
function buildCollectionJob(data: CanonicalData, doc: FormDoc, inputs: Inputs, r: EvalResult, n: number, branches: string[]): Job | null {
  const base = buildJob(data, { ...doc, lines: collectionFill(doc).concat(doc.lines.filter((l) => l.expr.op === "input")) }, inputs, r, n, branches, true);
  if (!base) return null;
  const entries: Record<string, EntryField[]> = {};
  const fill: Job["fill"] = []; const project: Record<string, Value> = {};
  const inputLines = doc.lines.filter((l) => l.expr.op === "input");
  for (const [entry, fields] of entriesOf(doc.id, r)) {
    entries[entry] = [];
    for (const l of inputLines) {
      const key = fields.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
      if (!computed(v)) continue; // an input the entry does not carry
      entries[entry]!.push({ field: l.id, label: l.label, value: v! });
    }
    // The lines the evaluation reached for this entry: a test settled early leaves the rest
    // underived, as a STOP in the printed flow chart ends the hand-work.
    for (const l of collectionFill(doc)) {
      const key = fields.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
      if (!key || !v) continue;
      if (!computed(v)) return null;
      fill.push({ id: key, printed: key, type: l.type, label: l.label, entry });
      project[key] = v;
    }
  }
  if (fill.length === 0) return null;
  return { ...base, kind: "collection", own_inputs: [], entries, fill, project };
}

/** Gate tests and the result of a shared definition: the lines a hand calculation decides. */
function defFill(def: FormDoc): Line[] { return def.lines.filter((l, i) => l.expr.op !== "input" && (l.type === "Bool" || i === def.lines.length - 1)); }

interface DefInstance { prefix: string; caseIndex: number; keys: Set<string> }

/** Instances of shared definition `def` in a result: instance prefix -> local line id -> derivation key. */
function instancesOf(def: FormDoc, r: EvalResult): Map<string, Map<string, string>> {
  const out = new Map<string, Map<string, string>>();
  const marker = `inst:${def.id}#`;
  for (const key of r.derivations.keys()) {
    const at = key.lastIndexOf(marker);
    if (at < 0) continue;
    const close = key.indexOf("}.", at);
    if (close < 0) continue;
    const prefix = key.slice(0, close + 1), local = key.slice(close + 2);
    if (prefix.indexOf("|inst:", at) >= 0) continue; // a line of another definition nested inside this instance
    if (!out.has(prefix)) out.set(prefix, new Map());
    out.get(prefix)!.set(local, key);
  }
  return out;
}

function buildDefJob(def: FormDoc, inputs: Inputs, r: EvalResult, inst: DefInstance, n: number, branches: string[]): Job | null {
  const lines = instancesOf(def, r).get(inst.prefix)!;
  const amount = r.derivations.get(lines.get("amount")!)?.value, status = r.derivations.get(lines.get("status")!)?.value;
  if (!computed(amount) || !computed(status)) return null;
  const fill: Job["fill"] = []; const project: Record<string, Value> = {};
  for (const l of defFill(def)) {
    const key = lines.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
    if (!key || !computed(v)) return null;
    fill.push({ id: key, printed: l.id, type: l.type, label: l.label });
    project[key] = v!;
  }
  const given: Given[] = [{ ref: "amount", doc: def.id, printed: "(a)", label: def.lines.find((l) => l.id === "amount")!.label, value: amount! }];
  return { id: `classm.${def.id}.${n}`, doc: def.id, kind: "def", inputs, status: (status as { value: string }).value, given, own_inputs: [], collections: {}, fill, project, branches };
}

export function classmJobs(args: string[]): void {
  let only: string[] | null = null; let corpusSize = 2000; let out = join(ROOT, ".classm", "jobs.json");
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--docs") only = (args[++i] ?? "").split(",").filter(Boolean);
    else if (args[i] === "--corpus") corpusSize = Number(args[++i]);
    else if (args[i] === "--out") out = args[++i]!;
  }
  const data = loadCanonical();
  const corpus = sampleReturns(data, corpusSize, SEED).map((c) => roundInputs(c, data));
  const results = corpus.map((inputs) => evaluateAll(data, inputs));
  const keysPerCase = results.map((r) => { const s = new Set<string>(); for (const d of r.derivations.values()) { const b = branchKeys(d); for (const k of [...b.sides, ...b.guards]) s.add(k); } return s; });
  const jobs: Job[] = [];
  const summary: string[] = [];
  for (const doc of data.forms) {
    if (only && !only.includes(doc.id)) continue;
    const isCollection = !!doc.collection;
    if (isCollection ? collectionFill(doc).length === 0 : !doc.lines.some((l) => !isHelper(l) && l.expr.op !== "input")) continue;
    const keys = docKeys(doc);
    // Candidate cases: the document's printed lines all computed; for a collection, at least one
    // entry, every entry's worked lines computed.
    const candidates = corpus.map((_, i) => i).filter((i) => {
      if (!isCollection) return doc.lines.filter((l) => !isHelper(l)).every((l) => computed(results[i]!.derivations.get(l.id)?.value));
      const entries = entriesOf(doc.id, results[i]!);
      // Every value derived for an entry must be computed: a refusal anywhere in the entry (a
      // screen held on a constant line included) puts the case outside the hand-worked scope.
      const r = results[i]!;
      return entries.size > 0 && [...entries.values()].every((f) =>
        [...f.values()].every((key) => r.derivations.get(key)?.value.kind !== "refusal") &&
        collectionFill(doc).every((l) => { const v = r.derivations.get(f.get(l.id) ?? "")?.value; return !v || computed(v); }));
    });
    const reachable = new Set(keys.filter((k) => candidates.some((i) => keysPerCase[i]!.has(k))));
    const covered = new Set<string>(); const chosen: number[] = [];
    while (covered.size < reachable.size) {
      let best = -1, gain = 0;
      for (const i of candidates) { let g = 0; for (const k of reachable) if (!covered.has(k) && keysPerCase[i]!.has(k)) g++; if (g > gain) { gain = g; best = i; } }
      if (best < 0) break;
      chosen.push(best); for (const k of keysPerCase[best]!) if (reachable.has(k)) covered.add(k);
    }
    let n = 0;
    for (const i of chosen) {
      const branches = keys.filter((k) => keysPerCase[i]!.has(k));
      const job = isCollection ? buildCollectionJob(data, doc, corpus[i]!, results[i]!, ++n, branches) : buildJob(data, doc, corpus[i]!, results[i]!, ++n, branches);
      if (job) jobs.push(job); else n--;
    }
    summary.push(`${doc.id}: ${n} case(s) cover ${covered.size}/${keys.length} branches (${keys.length - reachable.size} not reachable by a computed case)`);
  }
  // Shared definitions: instances (an amount and a filing status) drawn from the corpus, chosen to
  // take every reachable branch of the definition.
  for (const def of data.defs) {
    if (only && !only.includes(def.id)) continue;
    const keys = docKeys(def);
    const instances: DefInstance[] = []; const seen = new Set<string>();
    results.forEach((r, caseIndex) => {
      for (const [prefix, lines] of instancesOf(def, r)) {
        const amount = r.derivations.get(lines.get("amount") ?? "")?.value, status = r.derivations.get(lines.get("status") ?? "")?.value;
        const sig = JSON.stringify([amount, status]);
        if (!computed(amount) || seen.has(sig)) continue;
        seen.add(sig);
        const ks = new Set<string>();
        for (const [local, key] of lines) {
          const b = branchKeys(r.derivations.get(key)!);
          for (const k of [...b.sides, ...b.guards]) ks.add(local + k.slice(k.search(/[:#][^:#]*$/)));
        }
        instances.push({ prefix, caseIndex, keys: ks });
      }
    });
    const reachable = new Set(keys.filter((k) => instances.some((x) => x.keys.has(k))));
    const covered = new Set<string>(); const chosen: DefInstance[] = [];
    while (covered.size < reachable.size) {
      let best: DefInstance | null = null, gain = 0;
      for (const x of instances) { let g = 0; for (const k of reachable) if (!covered.has(k) && x.keys.has(k)) g++; if (g > gain) { gain = g; best = x; } }
      if (!best) break;
      chosen.push(best); for (const k of best.keys) if (reachable.has(k)) covered.add(k);
    }
    let n = 0;
    for (const x of chosen) {
      const job = buildDefJob(def, corpus[x.caseIndex]!, results[x.caseIndex]!, x, ++n, keys.filter((k) => x.keys.has(k)));
      if (job) jobs.push(job); else n--;
    }
    summary.push(`${def.id}: ${n} instance(s) cover ${covered.size}/${keys.length} branches (${keys.length - reachable.size} not reachable by a computed instance)`);
  }
  mkdirSync(join(out, ".."), { recursive: true });
  // With --docs, the other documents' jobs are kept as they are.
  let kept: Job[] = [];
  if (only && existsSync(out)) kept = (JSON.parse(readFileSync(out, "utf8")) as { jobs: Job[] }).jobs.filter((j) => !only!.includes(j.doc));
  writeFileSync(out, JSON.stringify({ seed: SEED, corpus: corpusSize, jobs: [...kept, ...jobs] }, null, 1));
  for (const s of summary) console.log(s);
  console.log(`classm: ${jobs.length} jobs -> ${out}`);
}
