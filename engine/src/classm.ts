// Class M jobs: for each document with printed lines, a small set of generated
// returns that together take every reachable branch of the document, with the
// values that flow into the document from elsewhere. An isolated model works
// the document by hand from those values and its archived pages
// (tools/transcription/classm.py); the agreements become class M fixtures.
// A keyed collection is worked once per entry: every computed line the
// evaluation reached for each entry, from the entry's own inputs. A shared
// definition is worked per instance (an amount and a filing status drawn from
// the generated returns): its gate tests and its result. A single document requests its printed
// lines only. Every job shows the worker, and its fixture keeps, only the answers the return's
// route reads, as an interview would ask them (routeJob).
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { evaluate, evaluateAll } from "./eval.js";
import type { EvalResult, Value } from "./eval.js";
import { sampleReturns } from "./generate.js";
import { loadInterview } from "./interview.js";
import { branchKeys, templateKey } from "./branches.js";
import { isHelperLine } from "./util.js";
import { loadCases } from "./fixtures.js";
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
  worked_scope?: "printed-irs-lines";
}


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
    case "keyed_lookup": for (const k of e["keys"] as string[]) out.refs.add(k); break;
    case "rate_lookup": out.refs.add(e["key"] as string); if (e["status"]) out.refs.add(e["status"] as string); break;
    case "prorate": out.refs.add(e["amount"] as string); out.refs.add(e["part"] as string); op(e["whole"] as Operand); break;
    case "percent_floor": out.refs.add(e["part"] as string); op(e["whole"] as Operand); break;
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
  const id = templateKey(key);
  for (const doc of data.forms) { const l = doc.lines.find((x) => x.id === id); if (l) return l.type === "Count"; }
  return false;
}

/** A printed line of a single document that its shown_when hides on this return: the form shows no amount there. */
function hiddenLine(l: Line, r: EvalResult): boolean {
  if (!l.shown_when) return false;
  const cond = r.derivations.get(l.shown_when)?.value;
  return cond?.kind === "bool" && !cond.value;
}

/** The ids a set of requested lines reads, following the document's own lines through their
 * expressions: the local lines visited and the foreign lines reached. Totals used only by
 * validation helpers are outside it, so they do not feed the document back into its review. */
function requestClosure(doc: FormDoc, requested: Line[]): Set<string> {
  const seen = new Set<string>();
  const visit = (id: string): void => {
    if (seen.has(id)) return;
    seen.add(id);
    const line = doc.lines.find((l) => l.id === id);
    if (!line) return;
    const refs = { refs: new Set<string>(), defs: false, sums: [] as { collection: string; field: string; where: Set<string> }[] };
    walk(line.expr as Expr, refs);
    for (const ref of refs.refs) visit(ref);
  };
  for (const line of requested) visit(line.id);
  return seen;
}

/** The supplied answers an evaluation read: the input keys it derived (an interview asks exactly these). */
function answersRead(r: EvalResult, inputs: Inputs): Set<string> {
  const out = new Set<string>();
  for (const [key, d] of r.derivations) if (d.op === "input" && key in inputs) out.add(key);
  return out;
}

function computed(v: Value | undefined): boolean { return !!v && (v.kind === "money" || v.kind === "bool" || v.kind === "count" || v.kind === "enum" || v.kind === "rate"); }

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
  // A collection's lines are keyed per entry: buildCollectionJob gives their shared-definition results per entry.
  for (const line of entryLevel ? [] : defLines) {
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
  // A printed line the form does not show on this return (its shown_when is false) is no form value.
  const fill = doc.lines.filter((l) => !isHelperLine(l) && l.expr.op !== "input" && !defLines.includes(l) && !hiddenLine(l, r)).map((l) => ({ id: l.id, printed: l.printed, type: l.type, label: l.label }));
  if (fill.length === 0) return null;
  const project: Record<string, Value> = {};
  for (const l of fill) { const v = val(l.id); if (!computed(v)) return null; project[l.id] = v!; }
  // Printed lines only: the incoming values their calculation reads through the document's own
  // lines, not those that only its validation helpers read.
  const needed = requestClosure(doc, doc.lines.filter((l) => fill.some((f) => f.id === l.id)));
  return { id: `classm.${doc.id}.${n}`, doc: doc.id, inputs, status, given: given.filter((g) => needed.has(g.ref)), own_inputs, collections, fill, project, branches,
    worked_scope: "printed-irs-lines" };
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

/** A helper of an entry that is unknown because a printed table has no row for this entry's facts (the
 * 2019-only automobile limits for a later vehicle, say): the case does not use it, as a STOP leaves later
 * lines underived. A printed line that depended on it would be unknown too, and its case is not chosen. */
function unusedHelper(l: Line, v: Value): boolean { return isHelperLine(l) && v.kind === "unknown" && /^no row of /.test((v as { reason?: string }).reason ?? ""); }

/** Lines of a collection worked by hand: every computed line except year constants. */
function collectionFill(doc: FormDoc): Line[] { return doc.lines.filter((l) => l.expr.op !== "input" && l.expr.op !== "param"); }

/** A collection document worked once per entry, for one generated return. */
function buildCollectionJob(data: CanonicalData, doc: FormDoc, inputs: Inputs, r: EvalResult, n: number, branches: string[]): Job | null {
  // Keep the full dependency scan and candidate/branch rules. Only the requested
  // outputs change: an IRS form's printed values do not require guessing what
  // inactive implementation helpers or pre-division totals mean.
  const printedOnly = collectionFill(doc).some(line => !isHelperLine(line));
  const base = buildJob(data, { ...doc, lines: collectionFill(doc).concat(doc.lines.filter((l) => l.expr.op === "input")) }, inputs, r, n, branches, true);
  if (!base) return null;
  if (printedOnly) {
    // Supply incoming values needed by the printed calculation, including its
    // local helper expressions, but not totals used only by validation helpers.
    // Those totals can feed the document's own calculations back into its review.
    const needed = new Set<string>(), seen = new Set<string>();
    const visit = (id: string): void => {
      if (seen.has(id)) return;
      seen.add(id);
      const line = doc.lines.find(line => line.id === id);
      if (!line) { needed.add(id); return; }
      const refs = { refs: new Set<string>(), defs: false, sums: [] as { collection: string; field: string; where: Set<string> }[] };
      walk(line.expr as Expr, refs);
      for (const ref of refs.refs) visit(ref);
    };
    for (const line of collectionFill(doc).filter(line => !isHelperLine(line))) visit(line.id);
    base.given = base.given.filter(given => needed.has(given.ref));
  }
  const entries: Record<string, EntryField[]> = {};
  const fill: Job["fill"] = []; const project: Record<string, Value> = {};
  const inputLines = doc.lines.filter((l) => l.expr.op === "input");
  // Lines that take a shared definition's result (a person's Schedule SE lines): given per entry,
  // as a single document's are, not worked (the definition has its own class M review).
  const defIds = new Set(doc.lines.filter((l) => { const o = { refs: new Set<string>(), defs: false, sums: [] as { collection: string; field: string; where: Set<string> }[] }; walk(l.expr as Expr, o); return o.defs; }).map((l) => l.id));
  // Fields of an enclosing entry the document reads (a business reading its person's Schedule SE, say):
  // given with the entry, since the entry-level hand-work cannot see the enclosing document.
  const enclosingRefs = new Set<string>();
  for (const line of doc.lines) {
    const out = { refs: new Set<string>(), defs: false, sums: [] as { collection: string; field: string; where: Set<string> }[] };
    walk(line.expr as Expr, out);
    for (const ref of out.refs) {
      const owner = data.forms.find((d) => d.collection && d.id !== doc.id && d.lines.some((x) => x.id === ref));
      if (owner) enclosingRefs.add(ref);
    }
  }
  for (const [entry, fields] of entriesOf(doc.id, r)) {
    entries[entry] = [];
    for (const l of inputLines) {
      const key = fields.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
      if (!computed(v)) continue; // an input the entry does not carry
      entries[entry]!.push({ field: l.id, label: l.label, value: v! });
    }
    for (const ref of [...enclosingRefs].sort()) {
      const [collection, field] = ref.split(".") as [string, string];
      const m = entry.match(new RegExp(`^(.*?${collection}\\[[^\\]]+\\])`));
      if (!m) continue;
      const v = r.derivations.get(`${m[1]}.${field}`)?.value;
      if (!computed(v)) continue;
      const label = data.forms.find((d) => d.id === collection)!.lines.find((x) => x.id === ref)!.label;
      entries[entry]!.push({ field: ref, label: `${label} (of the enclosing ${collection} entry, given)`, value: v! });
    }
    for (const id of [...defIds].sort()) {
      const key = fields.get(id); const v = key ? r.derivations.get(key)?.value : undefined;
      if (!key || !v) continue;
      if (!computed(v)) return null;
      const line = doc.lines.find((x) => x.id === id)!;
      entries[entry]!.push({ field: id, label: `${line.label} (result of the shared computation, given rather than worked)`, value: v });
    }
    // The lines the evaluation reached for this entry: a test settled early leaves the rest
    // underived, as a STOP in the printed flow chart ends the hand-work.
    for (const l of collectionFill(doc)) {
      if (printedOnly && isHelperLine(l)) continue;
      if (defIds.has(l.id)) continue;
      const key = fields.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
      if (!key || !v) continue;
      if (unusedHelper(l, v)) continue;
      // A printed line the form does not report for this entry (its shown_when is false) is no form value.
      if (l.shown_when) {
        const condKey = fields.get(l.shown_when); const cond = condKey ? r.derivations.get(condKey)?.value : undefined;
        if (cond?.kind === "bool" && !cond.value) continue;
      }
      if (!computed(v)) return null;
      fill.push({ id: key, printed: key, type: l.type, label: l.label, entry });
      project[key] = v;
    }
  }
  if (fill.length === 0) return null;
  return { ...base, kind: "collection", own_inputs: [], entries, fill, project,
    ...(printedOnly ? { worked_scope: "printed-irs-lines" as const } : {}) };
}

/** Gate tests and the result of a shared definition: the lines a hand calculation decides. */
function defFill(def: FormDoc): Line[] { return def.lines.filter((l, i) => l.expr.op !== "input" && (l.type === "Bool" || i === def.lines.length - 1 || /^\d+[a-z]?$/.test(l.printed))); }

/** A definition's parameters (its input lines): an amount and a filing status, or the lines a form binds. */
function defParams(def: FormDoc): Line[] { return def.lines.filter((l) => l.expr.op === "input"); }

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
  const params = defParams(def).map((l) => ({ line: l, value: r.derivations.get(lines.get(l.id) ?? "")?.value }));
  if (params.some((p) => !computed(p.value))) return null;
  const statusParam = params.find((p) => p.line.id === "status");
  const status = statusParam ? statusParam.value : { kind: "enum", value: String(inputs["f1040.status"]) } as Value;
  const fill: Job["fill"] = []; const project: Record<string, Value> = {};
  for (const l of defFill(def)) {
    const key = lines.get(l.id); const v = key ? r.derivations.get(key)?.value : undefined;
    if (!key || !computed(v)) return null;
    fill.push({ id: key, printed: l.id, type: l.type, label: l.label });
    project[key] = v!;
  }
  const given: Given[] = params.filter((p) => p.line.id !== "status").map((p) => ({ ref: p.line.id, doc: def.id, printed: p.line.id === "amount" ? "(a)" : p.line.printed, label: p.line.label, value: p.value! }));
  return { id: `classm.${def.id}.${n}`, doc: def.id, kind: "def", inputs, status: (status as { value: string }).value, given, own_inputs: [], collections: {}, fill, project, branches };
}

/** The lines that call shared definition `def`: the roots that reach its instances. */
function defCallers(data: CanonicalData, def: string): Set<string> {
  const out = new Set<string>();
  const calls = (e: unknown): boolean => {
    if (Array.isArray(e)) return e.some(calls);
    if (!e || typeof e !== "object") return false;
    const o = e as Record<string, unknown>;
    return o["def"] === def || Object.values(o).some(calls);
  };
  for (const doc of [...data.forms, ...data.defs]) for (const l of doc.lines) if (calls(l.expr)) out.add(l.id);
  return out;
}

const readIds = new WeakMap<CanonicalData, Set<string>>();
/** Every line id some line's expression reads (a collection field summed included). */
function staticallyRead(data: CanonicalData): Set<string> {
  if (!readIds.has(data)) {
    const out = new Set<string>();
    for (const d of [...data.forms, ...data.defs]) for (const l of d.lines) {
      const o = { refs: new Set<string>(), defs: false, sums: [] as { collection: string; field: string; where: Set<string> }[] };
      walk(l.expr as Expr, o);
      for (const r of o.refs) out.add(r);
      for (const s of o.sums) { out.add(s.field); for (const w of s.where) out.add(w); }
    }
    readIds.set(data, out);
  }
  return readIds.get(data)!;
}

/** The derivation keys of collection `doc` that some route reads: those another document's
 * evaluated lines read, the lines nothing reads (its outputs), and what they read in turn.
 * A helper only an untaken alternative reads (the month-by-month total of a uniform Form 1095-A)
 * is outside it. */
function liveInCollection(data: CanonicalData, doc: FormDoc, r: EvalResult): Set<string> {
  const own = new Set(doc.lines.map((l) => l.id));
  const read = staticallyRead(data);
  const stack: string[] = [];
  for (const [key, d] of r.derivations) {
    const id = templateKey(key);
    if (own.has(id)) { if (!read.has(id)) stack.push(key); continue; }
    for (const o of d.operands) if (own.has(templateKey(o.ref))) stack.push(o.ref);
  }
  const live = new Set<string>();
  while (stack.length) {
    const key = stack.pop()!;
    if (live.has(key)) continue;
    live.add(key);
    for (const o of r.derivations.get(key)?.operands ?? []) if (own.has(templateKey(o.ref))) stack.push(o.ref);
  }
  return live;
}

/** Restrict a built job to the route the return takes, as an interview would ask it.
 * - Answers shown to the worker (the document's own inputs, an entry's input fields) are those the
 *   requested lines read; the generator answers every route so every line computes, and a worker
 *   shown the other route's answers copies them.
 * - A helper of an unprinted collection that no route reads (liveInCollection: the month-by-month
 *   totals of a uniform Form 1095-A) is not requested.
 * - The fixture holds only the answers the interview asks on this return (its targets' route) or
 *   the requested lines read, so it never carries an answer the interview cannot give.
 * The values requested and the targets' values must be the same on the restricted answers; if not,
 * the fixture keeps every answer and the problem is reported. Branches are those the restricted
 * answers take. */
function routeJob(data: CanonicalData, doc: FormDoc, job: Job, fullResult: EvalResult, targetsReach: EvalResult, targets: string[], problems: string[]): Job | null {
  if (job.kind === "collection" && !job.worked_scope) {
    const live = liveInCollection(data, doc, fullResult);
    job.fill = job.fill.filter((f) => live.has(f.id));
    if (job.fill.length === 0) return null;
    job.project = Object.fromEntries(job.fill.map((f) => [f.id, job.project[f.id]!]));
  }
  const full = job.inputs;
  // A definition's instance is reached through the lines that call it.
  const callers = job.kind === "def" ? defCallers(data, doc.id) : null;
  const roots = callers
    ? [...evaluateAll(data, full).derivations.keys()].filter((k) => !k.includes("|inst:") && callers.has(templateKey(k)))
    : job.fill.map((f) => f.id);
  const requested = answersRead(evaluate(data, full, roots), full);
  job.own_inputs = job.own_inputs.filter((o) => requested.has(o.id));
  if (job.entries) {
    const inputFields = new Set(doc.lines.filter((l) => l.expr.op === "input").map((l) => l.id));
    for (const [entry, fields] of Object.entries(job.entries))
      job.entries[entry] = fields.filter((f) => !inputFields.has(f.field) || requested.has(`${entry}.${f.field.slice(doc.id.length + 1)}`));
  }
  const asked = answersRead(targetsReach, full);
  const pruned: Inputs = Object.fromEntries(Object.entries(full).filter(([k]) => k.startsWith("$") || k === "f1040.status" || asked.has(k) || requested.has(k)));
  const r = evaluateAll(data, pruned);
  const same = (a: Value | undefined, b: Value | undefined) => JSON.stringify(a) === JSON.stringify(b);
  const changed = job.fill.filter((f) => !same(r.derivations.get(f.id)?.value, job.project[f.id]))
    .concat(targets.filter((t) => !same(r.derivations.get(t)?.value, targetsReach.derivations.get(t)?.value)).map((t) => ({ id: t } as Job["fill"][number])));
  if (changed.length > 0) {
    problems.push(`${job.id}: restricting the answers to the interview's route changed ${changed.slice(0, 3).map((f) => f.id).join(", ")}; every answer kept`);
    return job;
  }
  job.inputs = pruned;
  const keys = new Set(docKeys(doc));
  const taken = new Set<string>();
  for (const d of r.derivations.values()) { const b = branchKeys(d); for (const k of [...b.sides, ...b.guards]) if (keys.has(k)) taken.add(k); }
  if (job.kind === "def") {
    // Instance branch keys are local to the definition, as the selection counts them.
    const first = Object.keys(job.project)[0]!;
    const prefix = first.slice(0, first.lastIndexOf("}.") + 1);
    for (const [local, key] of instancesOf(doc, r).get(prefix) ?? new Map<string, string>()) {
      const b = branchKeys(r.derivations.get(key)!);
      for (const k of [...b.sides, ...b.guards]) { const lk = local + k.slice(k.search(/[:#][^:#]*$/)); if (keys.has(lk)) taken.add(lk); }
    }
  }
  job.branches = [...keys].filter((k) => taken.has(k));
  return job;
}

export function classmJobs(args: string[]): void {
  let only: string[] | null = null; let corpusSize = 2000; let out = join(ROOT, ".classm", "jobs.json");
  let includeFixtures = false;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--docs") only = (args[++i] ?? "").split(",").filter(Boolean);
    else if (args[i] === "--corpus") corpusSize = Number(args[++i]);
    else if (args[i] === "--out") out = args[++i]!;
    else if (args[i] === "--include-fixtures") includeFixtures = true;
  }
  const data = loadCanonical();
  // Narrow regimes can disappear from a random corpus after a validation fix.
  // Seed with existing non-M facts as well; expected values never enter a job.
  const seeds = includeFixtures ? loadCases().cases
    .filter((c) => c.evidence !== "M" && (!only || c.covers.some((id) => only.includes(id))))
    .map((c) => c.inputs) : [];
  const corpus = [...sampleReturns(data, corpusSize, SEED), ...seeds].map((c) => roundInputs(c, data));
  const results = corpus.map((inputs) => evaluateAll(data, inputs));
  const keysPerCase = results.map((r) => { const s = new Set<string>(); for (const d of r.derivations.values()) { const b = branchKeys(d); for (const k of [...b.sides, ...b.guards]) s.add(k); } return s; });
  const jobs: Job[] = [];
  const summary: string[] = [];
  // The interview's targets, evaluated lazily, give the route a return takes: the answers it asks.
  const targets = loadInterview("full").targets;
  const reach = new Map<number, EvalResult>();
  const targetsReach = (i: number): EvalResult => { if (!reach.has(i)) reach.set(i, evaluate(data, corpus[i]!, targets)); return reach.get(i)!; };
  const problems: string[] = [];
  const routedCover = (built: Job[]): number => new Set(built.flatMap((j) => j.branches)).size;
  for (const doc of data.forms) {
    if (only && !only.includes(doc.id)) continue;
    const isCollection = !!doc.collection;
    if (isCollection ? collectionFill(doc).length === 0 : !doc.lines.some((l) => !isHelperLine(l) && l.expr.op !== "input")) continue;
    const keys = docKeys(doc);
    // Candidate cases: the document's printed lines all computed; for a collection, at least one
    // entry, every entry's worked lines computed.
    const candidates = corpus.map((_, i) => i).filter((i) => {
      // A declared filing flag means the form is actually used. Do not ask a
      // source reader to fill an unfiled form and credit incidental zeroes.
      if (doc.lines.some((l) => l.id === `${doc.id}.filing` && l.type === "Bool")) {
        const filing = results[i]!.derivations.get(`${doc.id}.filing`)?.value;
        if (filing?.kind !== "bool" || !filing.value) return false;
      }
      if (!isCollection) return doc.lines.filter((l) => !isHelperLine(l) && !hiddenLine(l, results[i]!)).every((l) => computed(results[i]!.derivations.get(l.id)?.value));
      const entries = entriesOf(doc.id, results[i]!);
      // Every value derived for an entry must be computed: a refusal anywhere in the entry (a
      // screen held on a constant line included) puts the case outside the hand-worked scope.
      const r = results[i]!;
      return entries.size > 0 && [...entries.values()].every((f) =>
        [...f.values()].every((key) => r.derivations.get(key)?.value.kind !== "refusal") &&
        collectionFill(doc).every((l) => { const v = r.derivations.get(f.get(l.id) ?? "")?.value; return !v || computed(v) || unusedHelper(l, v); }));
    });
    // ...and only cases a job can be built from (everything the document reads computed, the
    // fields of the collections it sums included): otherwise the greedy choice below can settle on
    // the richest returns, those where a summed entry refuses, and build nothing.
    const buildable = candidates.filter((i) => (isCollection ? buildCollectionJob : buildJob)(data, doc, corpus[i]!, results[i]!, 0, []) !== null);
    candidates.splice(0, candidates.length, ...buildable);
    const reachable = new Set(keys.filter((k) => candidates.some((i) => keysPerCase[i]!.has(k))));
    const covered = new Set<string>(); const chosen: number[] = [];
    while (covered.size < reachable.size) {
      let best = -1, gain = 0;
      for (const i of candidates) { let g = 0; for (const k of reachable) if (!covered.has(k) && keysPerCase[i]!.has(k)) g++; if (g > gain) { gain = g; best = i; } }
      if (best < 0) break;
      chosen.push(best); for (const k of keysPerCase[best]!) if (reachable.has(k)) covered.add(k);
    }
    // A document with no branch of its own (copies and sums) is still worked once, on the case
    // whose worked lines carry the most nonzero amounts (a case of zeros would test no arithmetic).
    if (keys.length === 0 && candidates.length > 0) {
      const nonzero = (i: number): number => {
        const r = results[i]!; let count = 0;
        const lines = isCollection ? collectionFill(doc) : doc.lines.filter((l) => !isHelperLine(l));
        const keysOf = isCollection ? [...entriesOf(doc.id, r).values()].flatMap((f) => lines.map((l) => f.get(l.id) ?? "")) : lines.map((l) => l.id);
        for (const key of keysOf) { const v = r.derivations.get(key)?.value; if (v?.kind === "money" && v.cents !== 0) count++; }
        return count;
      };
      let best = candidates[0]!, bestCount = nonzero(best);
      for (const i of candidates) { const c = nonzero(i); if (c > bestCount) { best = i; bestCount = c; } }
      chosen.push(best);
    }
    // Adding and subtracting a supplied amount has no control-flow branch.
    // Still work a positive example for each own money input when one exists;
    // otherwise grace-period carry-ins and forfeitures can all stay zero.
    if (!isCollection) for (const line of doc.lines.filter((l) => l.expr.op === "input" &&
        (l.type === "Dollars" || l.type === "NonNegDollars"))) {
      const positive = (i: number): boolean => {
        const v = results[i]!.derivations.get(line.id)?.value;
        return v?.kind === "money" && v.cents > 0;
      };
      if (!chosen.some(positive)) {
        const extra = candidates.find(positive);
        if (extra !== undefined) chosen.push(extra);
      }
    }
    let n = 0;
    const built: Job[] = [];
    for (const i of chosen) {
      const branches = keys.filter((k) => keysPerCase[i]!.has(k));
      const made = isCollection ? buildCollectionJob(data, doc, corpus[i]!, results[i]!, ++n, branches) : buildJob(data, doc, corpus[i]!, results[i]!, ++n, branches);
      const job = made && routeJob(data, doc, made, results[i]!, targetsReach(i), targets, problems);
      if (job) built.push(job); else n--;
    }
    jobs.push(...built);
    summary.push(`${doc.id}: ${n} case(s) cover ${routedCover(built)}/${keys.length} branches on the interview's route (${covered.size} with every answer; ${keys.length - reachable.size} not reachable by a computed case)`);
  }
  // Shared definitions: instances (an amount and a filing status) drawn from the corpus, chosen to
  // take every reachable branch of the definition.
  for (const def of data.defs) {
    if (only && !only.includes(def.id)) continue;
    const keys = docKeys(def);
    const instances: DefInstance[] = []; const seen = new Set<string>();
    results.forEach((r, caseIndex) => {
      for (const [prefix, lines] of instancesOf(def, r)) {
        const params = defParams(def).map((l) => r.derivations.get(lines.get(l.id) ?? "")?.value);
        const sig = JSON.stringify(params);
        if (params.some((v) => !computed(v)) || seen.has(sig)) continue;
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
    const built: Job[] = [];
    for (const x of chosen) {
      const made = buildDefJob(def, corpus[x.caseIndex]!, results[x.caseIndex]!, x, ++n, keys.filter((k) => x.keys.has(k)));
      const job = made && routeJob(data, def, made, results[x.caseIndex]!, targetsReach(x.caseIndex), targets, problems);
      if (job) built.push(job); else n--;
    }
    jobs.push(...built);
    summary.push(`${def.id}: ${n} instance(s) cover ${routedCover(built)}/${keys.length} branches on the interview's route (${covered.size} with every answer; ${keys.length - reachable.size} not reachable by a computed instance)`);
  }
  mkdirSync(join(out, ".."), { recursive: true });
  // With --docs, the other documents' jobs are kept as they are.
  let kept: Job[] = [];
  if (only && existsSync(out)) kept = (JSON.parse(readFileSync(out, "utf8")) as { jobs: Job[] }).jobs.filter((j) => !only!.includes(j.doc));
  writeFileSync(out, JSON.stringify({ seed: SEED, corpus: corpusSize, jobs: [...kept, ...jobs] }, null, 1));
  for (const s of summary) console.log(s);
  for (const p of problems) console.error(`classm: ${p}`);
  console.log(`classm: ${jobs.length} jobs -> ${out}`);
}
