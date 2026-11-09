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
// 3. An input stated as null is withheld: it takes no default and is left out, so it is unknown.
// The class M and mutation files take no defaults (takesDefaults): their tools state every input their cases read.
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import type { CanonicalData, FormDoc, Inputs, Line, ParamsDoc } from "./types.js";
import { nyPath, yearPath } from "./year.js";

interface ParamRef { param: string; status?: string; offset: number }

/** Which defaults a case takes: the federal table, or the federal and New York tables. */
export type Jurisdiction = "federal" | "ny";

/** One default: `input` is an input template (`f1040.status`, `w2.box1`) or a roster template (`$w2`). */
export interface DefaultEntry { input: string; value: unknown; reason: string }
export interface DefaultsFile { tax_year: number; note?: string; defaults: DefaultEntry[] }
export type DefaultTable = Map<string, unknown>;

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
  return new Map(files.flatMap((f) => f.defaults.map((d) => [d.input, d.value] as const)));
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
  const v = table.get(line.id);
  if (v !== ENTRY_KEY) return structuredClone(v);
  const values = line.type.startsWith("Enum(") ? data.params.enums[line.type.slice(5, -1)]?.values ?? [] : [];
  return entry !== null && values.includes(entry) ? entry : undefined;
}

/** The inputs with every unstated input given its default (see the head of this file); nulls are kept here. */
export function applyDefaults(data: CanonicalData, inputs: Inputs, table: DefaultTable, j: Jurisdiction): Inputs {
  const out: Inputs = { ...inputs };
  const docs = data.forms.filter((d) => j === "ny" || !isNyDoc(d));
  const fill = (doc: FormDoc, prefix: string, entry: string | null): void => {
    for (const line of doc.lines) {
      if (line.expr.op !== "input") continue;
      const key = prefix + line.id.slice(doc.id.length);
      if (key in out) continue;
      const v = lineDefault(data, table, line, entry);
      if (v !== undefined) out[key] = v;
    }
    for (const child of docs.filter((d) => d.collection?.parent === doc.id)) collection(child, prefix);
  };
  const collection = (doc: FormDoc, parent: string | null): void => {
    const rk = `$${doc.id}${parent ? "@" + parent : ""}`;
    if (!(rk in out) && !doc.collection!.implicit && table.has(`$${doc.id}`)) out[rk] = structuredClone(table.get(`$${doc.id}`));
    const roster = out[rk];
    if (!Array.isArray(roster)) return;
    for (const e of roster as string[]) fill(doc, `${parent ? parent + "." : ""}${doc.id}[${e}]`, e);
  };
  for (const doc of docs) {
    if (!doc.collection) fill(doc, doc.id, null);
    else if (!doc.collection.parent) collection(doc, null);
  }
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

/** The default tables' build check: every template has exactly one default, in its jurisdiction's file; no default
 * names anything else; each value is one the input accepts; each reason is one line. A jurisdiction given as null
 * (the year has no fixtures for it) is not checked. */
export function defaultsProblems(data: CanonicalData, files: Record<Jurisdiction, DefaultsFile | null>): string[] {
  const errors: string[] = [];
  const need = defaultTemplates(data);
  const seen = new Map<string, Jurisdiction>();
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
      if (typeof d.reason !== "string" || !d.reason.trim() || d.reason.includes("\n")) errors.push(`${where}: ${d.input} needs a one-line reason`);
      const bad = valueProblem(data, n.line, d.value);
      if (bad) errors.push(`${where}: ${d.input}: ${bad}`);
    }
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
