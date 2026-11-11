// How a fixture case's stated inputs become the inputs it is evaluated on. Only the fixture tooling calls this: the
// evaluator, the command-line program and the interview take inputs as given, and an input they are not given is
// unknown.
//
// 1. A fixture input may be stated relative to a year parameter, so that a boundary case stays on its boundary when
//    the parameter changes from year to year:
//      {"param": "medicare.threshold", "status": "mfj", "offset": -1}
//    is the parameter's value (for that filing status, if it has one per status) plus the offset in cents.
// 2. Every input the case does not state takes the test-data default of its template (fixtures/<year>/defaults.json,
//    and for the New York fixtures also fixtures/ny/<year>/defaults.json): each top-level form's inputs, each
//    collection's roster, and each input of every listed collection entry, down through nested collections. An
//    implicit collection's entry is filled only where the case lists its roster. A case states only the facts that
//    make its scenario non-default.
// 3. A default may be withheld under a condition on the case's other answers (`withheld` on the default): where the
//    condition holds, the input the case did not state is left out. Every condition is read on the inputs as they
//    stand after step 2, and a condition reads only inputs whose own default is unconditional, so the order in which
//    conditions are read cannot matter. A stated input is never withheld by a condition.
// 4. An input stated as null is withheld: it takes no default and is left out, so it is unknown.
// The class M and mutation files take no defaults (takesDefaults): their tools state every input their cases read.
//
// A condition is a list of tests that must all hold. A test reads one answer and compares it with constants:
//   {"input": "f1040.status", "in": ["mfj", "mfs"]}     the input's value is one of these (also "is": one value,
//                                                        "not": known and not this value)
//   {"count": "$f1095a", "is": 1}                        the number of entries the collection's roster lists
// For a default of a collection's input, a test reads a top-level form's input, or an input of the same entry or of
// an entry enclosing it; a count reads a top-level roster or the roster the entry (or an enclosing entry) is in. A
// test on an answer the case leaves unknown does not hold.
//
// The defaults file also declares consistency rules (`consistency`): each names tests that cannot all hold for one
// filer (`never`), with the reason. The build refuses a case that takes a default its other answers contradict by
// such a rule, and defaults that contradict one another (consistencyProblems).
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import type { CanonicalData, FormDoc, Inputs, Line, ParamsDoc } from "./types.js";
import { nyPath, yearPath } from "./year.js";

interface ParamRef { param: string; status?: string; offset: number }

/** Which defaults a case takes: the federal table, or the federal and New York tables. */
export type Jurisdiction = "federal" | "ny";

/** One test of a condition: `input` (an input template) or `count` (a roster template), compared by exactly one of
 * `is`, `in` and `not`. */
export interface Test { input?: string; count?: string; is?: unknown; in?: unknown[]; not?: unknown }
/** When a default is withheld (every test holds), and why the default is not a truthful answer there. */
export interface Withheld { when: Test[]; reason: string }
/** One default: `input` is an input template (`f1040.status`, `w2.box1`) or a roster template (`$w2`). */
export interface DefaultEntry { input: string; value: unknown; reason: string; withheld?: Withheld }
/** Answers that cannot all be given by one filer; `open`: the cases known to break the rule, each with its reason. */
export interface Rule { never: Test[]; reason: string; open?: Record<string, string> }
export interface DefaultsFile { tax_year: number; note?: string; defaults: DefaultEntry[]; consistency?: Rule[] }
export type DefaultTable = Map<string, Pick<DefaultEntry, "value" | "withheld">>;

/** The value of a default that is the entry's own key (person.role: `taxpayer` for person[taxpayer]); an entry whose
 * key is not a value of the input's enum takes no default. */
export const ENTRY_KEY = "$entry";

function isRef(v: unknown): v is ParamRef {
  return typeof v === "object" && v !== null && !Array.isArray(v) && typeof (v as ParamRef).param === "string";
}

export function defaultsPath(j: Jurisdiction): string {
  return j === "ny" ? nyPath("fixtures", "defaults.json") : yearPath("fixtures", "defaults.json");
}

export function readDefaultsFile(path: string): DefaultsFile {
  return JSON.parse(readFileSync(path, "utf8")) as DefaultsFile;
}

export function tableOf(...files: DefaultsFile[]): DefaultTable {
  return new Map(files.flatMap((f) => f.defaults.map((d) => [d.input, { value: d.value, ...(d.withheld ? { withheld: d.withheld } : {}) }] as const)));
}

const tables = new Map<string, DefaultTable>();
/** The year's default table for a jurisdiction, read once per process. */
export function defaultTable(j: Jurisdiction): DefaultTable {
  const key = defaultsPath(j);
  let t = tables.get(key);
  if (!t) {
    const files = [defaultsPath("federal"), ...(j === "ny" ? [defaultsPath("ny")] : [])].filter((p) => existsSync(p));
    t = tableOf(...files.map(readDefaultsFile));
    tables.set(key, t);
  }
  return t;
}

/** Parameter-relative inputs replaced by their values; every other input as stated (nulls included). */
export function resolveParams(inputs: Record<string, unknown>, params: ParamsDoc, where = "fixture"): Inputs {
  const out: Record<string, unknown> = {};
  for (const [key, v] of Object.entries(inputs)) {
    if (!isRef(v)) { out[key] = v; continue; }
    const entry = params.values[v.param];
    const base = v.status === undefined ? entry?.value : (entry?.value as Record<string, unknown> | undefined)?.[v.status];
    if (typeof base !== "number" || !Number.isSafeInteger(v.offset)) {
      throw new Error(`${where}: input ${key} refers to ${v.param}${v.status ? `[${v.status}]` : ""}, which is not a dollar amount`);
    }
    out[key] = base + v.offset;
  }
  return out as Inputs;
}

export const isNyDoc = (doc: { id: string }): boolean => doc.id.startsWith("ny_");

/** The default of one input line for one entry (`entry` null on a top-level form); undefined when it has none. */
function lineDefault(data: CanonicalData, table: DefaultTable, line: Line, entry: string | null): unknown {
  if (!table.has(line.id)) return undefined;
  const v = table.get(line.id)!.value;
  if (v !== ENTRY_KEY) return structuredClone(v);
  const values = line.type.startsWith("Enum(") ? data.params.enums[line.type.slice(5, -1)]?.values ?? [] : [];
  return entry !== null && values.includes(entry) ? entry : undefined;
}

/** Where a test is read: the key prefix of each collection entry it is read within, by document id (the entry whose
 * default or rule is in question and the entries enclosing it). */
type Frames = ReadonlyMap<string, string>;

/** A collection's document preceded by the documents of the collections enclosing it, outermost first; none for a
 * top-level form. */
function chainOf(data: CanonicalData, doc: FormDoc): FormDoc[] {
  if (!doc.collection) return [];
  const parent = doc.collection.parent ? data.forms.find((d) => d.id === doc.collection!.parent) : undefined;
  return [...(parent ? chainOf(data, parent) : []), doc];
}

/** One set of frames per entry of the innermost collection of `scope` (a chainOf) that the inputs list, each with the
 * entries enclosing it; one empty set when `scope` is empty. */
function sitesOf(scope: FormDoc[], inputs: Inputs): Frames[] {
  let sites: Map<string, string>[] = [new Map()];
  for (const doc of scope) {
    sites = sites.flatMap((frames) => {
      const parent = doc.collection!.parent ? frames.get(doc.collection!.parent) : undefined;
      const roster = inputs[`$${doc.id}${parent ? "@" + parent : ""}`];
      return (Array.isArray(roster) ? roster as string[] : []).map((e) => new Map([...frames, [doc.id, `${parent ? parent + "." : ""}${doc.id}[${e}]`]]));
    });
  }
  return sites;
}

/** The document an input template or roster template (`$id`) belongs to. */
function ownerOf(data: CanonicalData, template: string): FormDoc | undefined {
  if (template.startsWith("$")) return data.forms.find((d) => d.id === template.slice(1) && d.collection);
  return data.forms.find((d) => d.lines.some((l) => l.id === template && l.expr.op === "input"));
}

/** The key under which a case's inputs hold the answer a test reads; null when the test cannot be read from here. */
function testKey(data: CanonicalData, test: Test, frames: Frames): string | null {
  const template = test.input ?? test.count ?? "";
  const doc = ownerOf(data, template);
  if (!doc) return null;
  if (test.count !== undefined) {
    const parent = doc.collection!.parent;
    return !parent ? template : frames.has(parent) ? `${template}@${frames.get(parent)}` : null;
  }
  return !doc.collection ? template : frames.has(doc.id) ? frames.get(doc.id) + template.slice(doc.id.length) : null;
}

const sameValue = (a: unknown, b: unknown): boolean => JSON.stringify(a) === JSON.stringify(b);

/** Whether a test holds on the inputs; a test on an answer that is unknown (absent, or stated as null) does not. */
function testHolds(data: CanonicalData, test: Test, inputs: Inputs, frames: Frames): boolean {
  const key = testKey(data, test, frames);
  const raw = key === null ? undefined : inputs[key];
  const v = test.count === undefined ? raw : Array.isArray(raw) ? raw.length : undefined;
  if (v === undefined || v === null) return false;
  if ("is" in test) return sameValue(v, test.is);
  if ("in" in test) return (test.in ?? []).some((x) => sameValue(v, x));
  return !sameValue(v, test.not);
}

/** The inputs with every unstated input given its default, less the defaults whose withholding condition holds (see
 * the head of this file); nulls are kept here. */
export function applyDefaults(data: CanonicalData, inputs: Inputs, table: DefaultTable, j: Jurisdiction): Inputs {
  const out: Inputs = { ...inputs };
  const docs = data.forms.filter((d) => j === "ny" || !isNyDoc(d));
  const conditional: { key: string; when: Test[]; frames: Frames }[] = [];
  const fill = (doc: FormDoc, prefix: string, entry: string | null, frames: Frames): void => {
    for (const line of doc.lines) {
      if (line.expr.op !== "input") continue;
      const key = prefix + line.id.slice(doc.id.length);
      if (key in out) continue;
      const v = lineDefault(data, table, line, entry);
      if (v === undefined) continue;
      out[key] = v;
      const withheld = table.get(line.id)!.withheld;
      if (withheld) conditional.push({ key, when: withheld.when, frames });
    }
    for (const child of docs.filter((d) => d.collection?.parent === doc.id)) collection(child, prefix, frames);
  };
  const collection = (doc: FormDoc, parent: string | null, frames: Frames): void => {
    const rk = `$${doc.id}${parent ? "@" + parent : ""}`;
    if (!(rk in out) && !doc.collection!.implicit && table.has(`$${doc.id}`)) out[rk] = structuredClone(table.get(`$${doc.id}`)!.value);
    const roster = out[rk];
    if (!Array.isArray(roster)) return;
    for (const e of roster as string[]) {
      const prefix = `${parent ? parent + "." : ""}${doc.id}[${e}]`;
      fill(doc, prefix, e, new Map([...frames, [doc.id, prefix]]));
    }
  };
  for (const doc of docs) {
    if (!doc.collection) fill(doc, doc.id, null, new Map());
    else if (!doc.collection.parent) collection(doc, null, new Map());
  }
  // Every condition is decided on the filled inputs before any default is removed.
  for (const c of conditional.filter((c) => c.when.every((t) => testHolds(data, t, out, c.frames)))) delete out[c.key];
  return out;
}

/** A fixture case's inputs as it is evaluated: parameters resolved, defaults applied, withheld (null) inputs left out. */
export function resolveInputs(inputs: Record<string, unknown>, data: CanonicalData, where: string, j: Jurisdiction, table: DefaultTable = defaultTable(j)): Inputs {
  const stated = resolveParams(inputs, data.params, where);
  const out = applyDefaults(data, stated, table, j);
  for (const [k, v] of Object.entries(out)) if (v === null) delete out[k];
  return out;
}

/** The templates that need a default, each with the jurisdiction whose file holds it: every input line of every form,
 * and the roster of every collection that is not implicit. */
export function defaultTemplates(data: CanonicalData): Map<string, { j: Jurisdiction; line: Line | null }> {
  const out = new Map<string, { j: Jurisdiction; line: Line | null }>();
  for (const doc of data.forms) {
    const j: Jurisdiction = isNyDoc(doc) ? "ny" : "federal";
    if (doc.collection && !doc.collection.implicit) out.set(`$${doc.id}`, { j, line: null });
    for (const line of doc.lines) if (line.expr.op === "input") out.set(line.id, { j, line });
  }
  return out;
}

/** The problems with one condition (a default's `withheld.when`, or a rule's `never`), each prefixed with `where`.
 * `own`: the template the condition belongs to (a default's input; null for a rule). A test must name a declared
 * input or roster of jurisdiction `j` or the federal one, read by exactly one of `is`, `in` and `not` with values the
 * answer can take; no answer is tested twice; the collections the tests (and `own`) read lie on one line of nested
 * collections; and a default's condition reads neither its own input nor an input whose default is conditional. */
function conditionProblems(data: CanonicalData, where: string, tests: unknown, own: string | null, j: Jurisdiction, conditionalInputs: ReadonlySet<string>): string[] {
  if (!Array.isArray(tests) || tests.length === 0) return [`${where}: a condition is a list of at least one test`];
  const errors: string[] = [];
  const need = defaultTemplates(data);
  const seen = new Set<string>();
  // The collection entries the condition is read within: for a default, its own entry and those enclosing it; for a
  // rule, the longest line of nested collections among its tests.
  let scope: string[] = own !== null && ownerOf(data, own) ? chainOf(data, ownerOf(data, own)!).map((d) => d.id) : [];
  const startsWith = (long: string[], short: string[]): boolean => short.every((id, i) => long[i] === id);
  const within = (c: string[]): boolean => {
    if (startsWith(scope, c)) return true;
    if (own !== null || !startsWith(c, scope)) return false;
    scope = c;
    return true;
  };
  for (const t of tests as Test[]) {
    if (typeof t !== "object" || t === null || Array.isArray(t)) { errors.push(`${where}: a test is an object`); continue; }
    const template = t.input ?? t.count;
    const what = `${where}: the test on ${String(template)}`;
    const ops = (["is", "in", "not"] as const).filter((k) => k in t);
    if (typeof template !== "string" || (t.input === undefined) === (t.count === undefined) || Object.keys(t).some((k) => !["input", "count", "is", "in", "not"].includes(k))) { errors.push(`${where}: a test names one "input" or one "count" and compares it by "is", "in" or "not"`); continue; }
    if (ops.length !== 1) { errors.push(`${what} needs exactly one of "is", "in" and "not"`); continue; }
    if (seen.has(template)) errors.push(`${what} is the second on that answer; a condition tests an answer once`);
    seen.add(template);
    const n = need.get(template);
    const doc = ownerOf(data, template);
    if (!n || !doc || (t.count !== undefined) !== (n.line === null)) { errors.push(`${what}: ${template} is not a declared ${t.count !== undefined ? "roster" : "input"}`); continue; }
    if (n.j === "ny" && j !== "ny") errors.push(`${what} reads a New York answer from the federal defaults`);
    const values = "in" in t ? t.in : ["is" in t ? t.is : t.not];
    if (!Array.isArray(values) || values.length === 0 || new Set(values.map((v) => JSON.stringify(v))).size !== values.length) { errors.push(`${what}: "in" is a list of distinct values`); continue; }
    for (const v of values) {
      const bad = n.line === null ? (typeof v === "number" && Number.isSafeInteger(v) && v >= 0 ? null : "a count is a whole number, 0 or more")
        : v === ENTRY_KEY ? "not a value an answer takes" : valueProblem(data, n.line, v);
      if (bad) errors.push(`${what}: ${JSON.stringify(v)}: ${bad}; the test can never hold as meant`);
    }
    // A count reads the roster an entry is in (from the entry enclosing that roster); an input is read from its entry.
    const read = (t.count !== undefined ? chainOf(data, doc).slice(0, -1) : chainOf(data, doc)).map((d) => d.id);
    if (!within(read)) errors.push(`${what} reads an entry of ${read[read.length - 1]}, which ${own ?? "the rule's other tests"} cannot be read beside (only a top-level answer, the same entry or an entry enclosing it)`);
    if (own === null) continue;
    if (template === own) errors.push(`${what} reads the default's own input`);
    else if (conditionalInputs.has(template)) errors.push(`${what} reads an input whose own default is conditional, which is resolved later; a condition reads only unconditional defaults and stated answers`);
    if (t.count !== undefined && scope.includes(doc.id) && !("not" in t) && values.every((v) => v === 0)) errors.push(`${what} can never hold: the roster lists the entry itself`);
  }
  return errors;
}

const oneLine = (s: unknown): boolean => typeof s === "string" && !!s.trim() && !s.includes("\n");

/** The default tables' build check: every template has exactly one default, in its jurisdiction's file; no default
 * names anything else; each value is one the input accepts; each reason is one line; each withholding condition and
 * consistency rule is well formed (conditionProblems) and has a one-line reason. A jurisdiction given as null
 * (the year has no fixtures for it) is not checked. */
export function defaultsProblems(data: CanonicalData, files: Record<Jurisdiction, DefaultsFile | null>): string[] {
  const errors: string[] = [];
  const need = defaultTemplates(data);
  const seen = new Map<string, Jurisdiction>();
  const conditionalInputs = new Set((["federal", "ny"] as const).flatMap((j) => (files[j]?.defaults ?? []).filter((d) => d.withheld !== undefined).map((d) => d.input)));
  for (const j of ["federal", "ny"] as const) {
    const f = files[j];
    const where = j === "ny" ? "fixtures/ny/<year>/defaults.json" : "fixtures/<year>/defaults.json";
    if (!f) continue;
    for (const d of f.defaults) {
      const n = need.get(d.input);
      if (seen.has(d.input)) { errors.push(`${where}: ${d.input} has more than one default`); continue; }
      seen.set(d.input, j);
      if (!n) { errors.push(`${where}: ${d.input} is not a declared input or roster`); continue; }
      if (n.j !== j) errors.push(`${where}: ${d.input} belongs in the ${n.j} defaults`);
      if (!oneLine(d.reason)) errors.push(`${where}: ${d.input} needs a one-line reason`);
      const bad = valueProblem(data, n.line, d.value);
      if (bad) errors.push(`${where}: ${d.input}: ${bad}`);
      if (d.withheld === undefined) continue;
      if (n.line === null) { errors.push(`${where}: ${d.input}: a roster's default cannot be withheld`); continue; }
      if (Object.keys(d.withheld).sort().join() !== "reason,when" || !oneLine(d.withheld.reason)) errors.push(`${where}: ${d.input}: "withheld" holds "when" (the tests) and a one-line "reason"`);
      errors.push(...conditionProblems(data, `${where}: ${d.input} withheld`, d.withheld.when, d.input, j, conditionalInputs));
    }
    (f.consistency ?? []).forEach((r, i) => {
      const at = `${where}: consistency rule ${i + 1}`;
      if (Object.keys(r).some((k) => !["never", "reason", "open"].includes(k)) || !oneLine(r.reason)) errors.push(`${at} holds "never" (the tests), a one-line "reason" and optionally "open"`);
      if (r.open !== undefined && (typeof r.open !== "object" || r.open === null || Array.isArray(r.open) || !Object.values(r.open).every(oneLine))) errors.push(`${at}: "open" maps a case id to a one-line reason`);
      if (Array.isArray(r.never) && (r.never.length < 2 || !r.never.some((t) => t?.input !== undefined))) errors.push(`${at} needs at least two tests, one of them on an input`);
      errors.push(...conditionProblems(data, at, r.never, null, j, conditionalInputs));
    });
  }
  for (const [t, n] of need) if (!seen.has(t) && files[n.j]) errors.push(`${n.j === "ny" ? "fixtures/ny/<year>" : "fixtures/<year>"}/defaults.json: ${t} has no default`);
  return errors;
}

function valueProblem(data: CanonicalData, line: Line | null, v: unknown): string | null {
  if (line === null) return Array.isArray(v) && v.every((k) => typeof k === "string" && /^[a-zA-Z0-9_-]+$/.test(k)) && new Set(v).size === v.length ? null : "a roster default is a list of distinct entry keys";
  if (line.type === "Bool") return typeof v === "boolean" ? null : "not a Bool";
  if (line.type.startsWith("Enum(")) {
    if (v === ENTRY_KEY) return null;
    return data.params.enums[line.type.slice(5, -1)]?.values.includes(v as string) ? null : `not a value of ${line.type}`;
  }
  if (typeof v !== "number" || !Number.isSafeInteger(v)) return `not a ${line.type}`;
  return line.type !== "Dollars" && v < 0 ? `negative ${line.type}` : null;
}

/** The key in a rule's `open` list that stands for the defaults alone, rather than for a case. */
export const DEFAULTS_ALONE = "(defaults)";

/** The collections a rule is read within: the longest line of nested collections among its tests (none for a rule
 * on top-level answers alone). */
function ruleScope(data: CanonicalData, rule: Rule): FormDoc[] {
  let scope: FormDoc[] = [];
  for (const t of rule.never) {
    const doc = ownerOf(data, t.input ?? t.count ?? "");
    const c = !doc ? [] : t.count !== undefined ? chainOf(data, doc).slice(0, -1) : chainOf(data, doc);
    if (c.length > scope.length) scope = c;
  }
  return scope;
}

/** Where every test of a rule holds on the inputs: for each such entry of the rule's scope, the keys the tests read. */
function ruleHolds(data: CanonicalData, rule: Rule, inputs: Inputs): string[][] {
  return sitesOf(ruleScope(data, rule), inputs).filter((frames) => rule.never.every((t) => testHolds(data, t, inputs, frames)))
    .map((frames) => rule.never.map((t) => testKey(data, t, frames)!));
}

/** Whether the defaults alone break a rule: a filer who states nothing but one entry of each collection the rule is
 * read within (where the defaults list none). */
function defaultsBreak(data: CanonicalData, rule: Rule, table: DefaultTable, j: Jurisdiction): boolean {
  const stated: Inputs = {};
  let prefix = "";
  for (const doc of ruleScope(data, rule)) {
    const rk = `$${doc.id}${prefix ? "@" + prefix : ""}`;
    const roster = applyDefaults(data, stated, table, j)[rk];
    const listed = Array.isArray(roster) && roster.length > 0;
    if (!listed) stated[rk] = ["entry"];
    prefix = `${prefix ? prefix + "." : ""}${doc.id}[${listed ? (roster as string[])[0] : "entry"}]`;
  }
  return ruleHolds(data, rule, applyDefaults(data, stated, table, j)).length > 0;
}

/** A case file's case with its jurisdiction, as the consistency check reads it. */
export interface CheckedCase { id: string; file: string; j: Jurisdiction; inputs: Record<string, unknown> }

/** The fixtures' consistency check, on the rules the defaults files declare (a rule of the federal file is read on
 * every case, one of the New York file on the New York cases; cases that take no defaults are not read).
 * - The defaults alone must break no rule (defaultsBreak).
 * - A case breaks a rule where every test of the rule holds on the case's resolved inputs and at least one answer
 *   read is a default the case took, not one it stated. Where the defaults alone break the rule, an entry that takes
 *   every answer the rule reads from the defaults is that same finding and is not counted again.
 * - Each is a problem unless the rule lists it as open (`open`: a case id, or DEFAULTS_ALONE, with its reason); an
 *   open entry that no longer breaks its rule is a problem too.
 * - A withholding condition that holds in no case is a problem. */
export function consistencyProblems(data: CanonicalData, files: Record<Jurisdiction, DefaultsFile | null>, cases: CheckedCase[]): string[] {
  const errors: string[] = [];
  const present = (["federal", "ny"] as const).flatMap((j) => files[j] ? [files[j]] : []);
  const table = { federal: tableOf(...(files.federal ? [files.federal] : [])), ny: tableOf(...present) };
  const rules = (["federal", "ny"] as const).flatMap((j) => (files[j]?.consistency ?? []).map((rule, i) => {
    const name = `${j === "ny" ? "fixtures/ny/<year>" : "fixtures/<year>"}/defaults.json: consistency rule ${i + 1}`;
    return { rule, j, name, alone: defaultsBreak(data, rule, table[j], j), broken: new Set<string>() };
  }));
  for (const r of rules) {
    const open = r.rule.open?.[DEFAULTS_ALONE] !== undefined;
    if (r.alone && !open) errors.push(`${r.name}: the defaults alone break it (${r.rule.never.map((t) => t.input ?? t.count).join(", ")}): ${r.rule.reason} Withhold a default under a condition, or list ${DEFAULTS_ALONE} as open with the reason.`);
    if (!r.alone && open) errors.push(`${r.name}: lists ${DEFAULTS_ALONE} as open, but the defaults alone do not break the rule; remove it from the list`);
  }
  const conditional = present.flatMap((f) => f.defaults.filter((d) => d.withheld));
  const fired = new Set<string>();
  const unconditional = (t: DefaultTable): DefaultTable => new Map([...t].map(([k, d]) => [k, { value: d.value }]));
  for (const c of cases) {
    if (!takesDefaults(c.file)) continue;
    const stated = resolveParams(c.inputs, data.params, c.id);
    const filled = applyDefaults(data, stated, table[c.j], c.j);
    // A condition has held in the case where the default is taken without the conditions and absent with them.
    const whole = conditional.length ? applyDefaults(data, stated, unconditional(table[c.j]), c.j) : filled;
    for (const d of conditional) {
      if (fired.has(d.input)) continue;
      const keys = sitesOf(chainOf(data, ownerOf(data, d.input)!), whole).map((frames) => testKey(data, { input: d.input }, frames)!);
      if (keys.some((k) => k in whole && !(k in filled))) fired.add(d.input);
    }
    for (const r of rules) {
      if (r.j === "ny" && c.j !== "ny") continue;
      for (const keys of ruleHolds(data, r.rule, filled)) {
        const taken = keys.filter((k) => !(k in stated));
        if (taken.length === 0 || (r.alone && taken.length === keys.length)) continue;
        r.broken.add(c.id);
        if (r.rule.open?.[c.id] !== undefined) continue;
        const against = keys.filter((k) => k in stated).map((k) => `${k} ${JSON.stringify(filled[k])}`).join(", ") || "its other defaults";
        errors.push(`${c.id}: takes the default of ${taken.map((k) => `${k} (${JSON.stringify(filled[k])})`).join(" and ")} against ${against}; ${r.name}: ${r.rule.reason} State the answer the scenario means, or withhold it (null).`);
      }
    }
  }
  for (const r of rules) for (const id of Object.keys(r.rule.open ?? {})) if (id !== DEFAULTS_ALONE && !r.broken.has(id)) errors.push(`${r.name}: lists ${id} as open, but no such case breaks the rule; remove it from the list`);
  for (const d of conditional) if (!fired.has(d.input)) errors.push(`${d.input}: its withholding condition holds in no case that takes the default; remove the condition or correct it`);
  return errors;
}

/** Every case of both jurisdictions' fixtures as stated, for consistencyProblems. */
export function checkedCases(): CheckedCase[] {
  return ([["federal", yearPath("fixtures")], ["ny", nyPath("fixtures")]] as const).flatMap(([j, dir]) => !existsSync(dir) ? [] : caseFiles(dir)
    .flatMap((file) => (JSON.parse(readFileSync(join(dir, file), "utf8")) as { cases: StatedCase[] }).cases.map((c) => ({ id: c.id, file, j, inputs: c.inputs }))));
}

/** A fixture case as its file states it; `walk` names the interview profile whose path the case is (the build's
 * interview path checks and interview-rules walk it). */
export type WalkProfile = "social-security" | "sales" | "stage4" | "full";
export interface StatedCase { id: string; walk?: WalkProfile; covers: string[]; evidence: string; evidence_note?: string; inputs: Record<string, unknown>; expect?: Record<string, unknown> }

/** The case files of a fixtures directory: every .json file in it except the defaults table. */
export function caseFiles(dir: string): string[] {
  return readdirSync(dir).filter((f) => f.endsWith(".json") && f !== "defaults.json").sort();
}

/** Whether a case file's cases take the defaults: the class M files (classm*.json) and the mutation file
 * (mutation.json) do not, since the tools that write them state every input their cases' routes read. */
export function takesDefaults(file: string): boolean {
  return !file.startsWith("classm") && file !== "mutation.json";
}

/** A case's inputs as its file's cases are evaluated on (resolveInputs; without defaults where the file takes none). */
export function resolveCase(c: { id: string; inputs: Record<string, unknown> }, file: string, data: CanonicalData, j: Jurisdiction, table?: DefaultTable): Inputs {
  return resolveInputs(c.inputs, data, c.id, j, takesDefaults(file) ? table ?? defaultTable(j) : new Map());
}

/** Every case of one jurisdiction's fixtures, with the file it is in, its inputs resolved. */
export function loadFixtureCases(j: Jurisdiction, data: CanonicalData): (Omit<StatedCase, "inputs"> & { inputs: Inputs; file: string })[] {
  const dir = j === "ny" ? nyPath("fixtures") : yearPath("fixtures");
  return caseFiles(dir).flatMap((f) => (JSON.parse(readFileSync(join(dir, f), "utf8")) as { cases: StatedCase[] }).cases
    .map((c) => ({ ...c, file: f, inputs: resolveCase(c, f, data, j) })));
}

/** The federal cases an interview profile walks: those whose `walk` names it. */
export function walkedCases(profile: WalkProfile, data: CanonicalData): { id: string; inputs: Inputs }[] {
  return loadFixtureCases("federal", data).filter((c) => c.walk === profile);
}

/** The year's defaults files for the build check: a jurisdiction with fixtures and no defaults file has an empty one. */
export function yearDefaultsFiles(): Record<Jurisdiction, DefaultsFile | null> {
  const one = (j: Jurisdiction, dir: string): DefaultsFile | null =>
    !existsSync(dir) ? null : existsSync(defaultsPath(j)) ? readDefaultsFile(defaultsPath(j)) : { tax_year: 0, defaults: [] };
  return { federal: one("federal", yearPath("fixtures")), ny: one("ny", nyPath("fixtures")) };
}
