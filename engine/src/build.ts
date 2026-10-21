// Build: read the authored YAML, resolve citations against the source
// manifest, write canonical JSON, validate against the schema, and run the
// static checks. Fails with a non-zero exit on any error.

import { mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { Ajv2020 } from "ajv/dist/2020.js";
import type { ValidateFunction } from "ajv";
import { stableStringify } from "./util.js";
import { type InterviewData } from "./interview.js";
import { checkInterview, checkSalesInterview } from "./interview-check.js";
import { runChecks } from "./check.js";
import { YEAR, yearPath } from "./year.js";
import type {
  CanonicalData,
  CiteAuthored,
  CiteFilled,
  FormDoc,
  ParamsDoc,
  RegisterDoc,
  TableDoc,
} from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const MANIFEST_PATH = yearPath("sources", "manifest.json");
const SCHEMA_PATH = join(ROOT, "schema", "data.schema.json");
const FORMS_DIR = yearPath("forms");
const TABLES_DIR = yearPath("tables");
const PARAMS_PATH = join(ROOT, "params", `${YEAR}.yaml`);
const REGISTER_PATH = join(ROOT, "ambiguities", `${YEAR}.yaml`);
const OUT_DIR = yearPath("canonical");

interface BankQuestion { input: string; order: number; help: string; prompt?: string; cite?: CiteAuthored }
interface QuestionBank { tax_year: number; frames: Record<string, string>; questions: BankQuestion[] }
interface InterviewProfile { tax_year: number; targets: string[]; initial: InterviewData["initial"]; cite: CiteAuthored; questions: string[] | "all" }

interface ManifestEntry {
  id: string;
  file: string;
  sha256: string;
  revision: string | null;
  revision_status?: string;
}

export function runBuild(): { data: CanonicalData | null; errors: string[]; stats: string[] } {
  const errors: string[] = [];
  const stats: string[] = [];

  const manifest = new Map<string, ManifestEntry>();
  for (const entry of (JSON.parse(readFileSync(MANIFEST_PATH, "utf-8")).documents as ManifestEntry[])) {
    manifest.set(entry.id, entry);
  }

  const fillCite = (cite: CiteAuthored | undefined, taxYear: number, where: string): CiteFilled => {
    const fallback: CiteFilled = { doc: "?", tax_year: taxYear, revision: "?", locator: "?", snapshot: "?" };
    if (!cite || typeof cite.doc !== "string" || typeof cite.locator !== "string") {
      errors.push(`${where}: missing cite (doc and locator are required)`);
      return fallback;
    }
    const source = manifest.get(cite.doc);
    if (!source) {
      errors.push(`${where}: cite doc '${cite.doc}' not in sources/${YEAR}/manifest.json`);
      return { ...fallback, doc: cite.doc, locator: cite.locator };
    }
    if (!source.revision) {
      errors.push(`${where}: source '${cite.doc}' has no inspected revision in the manifest`);
    }
    const filled: CiteFilled = {
      doc: cite.doc,
      tax_year: taxYear,
      revision: source.revision ?? "?",
      locator: cite.locator,
      snapshot: source.sha256,
    };
    if (cite.quote !== undefined) filled.quote = cite.quote;
    return filled;
  };

  const loadFormOrDef = (path: string): FormDoc | null => {
    const raw = parseYaml(readFileSync(path, "utf-8")) as { form?: unknown; def?: unknown };
    const key = raw.form !== undefined ? "form" : raw.def !== undefined ? "def" : null;
    if (!key) {
      errors.push(`${path}: expected a top-level 'form:' or 'def:' key`);
      return null;
    }
    const doc = (raw as Record<string, FormDoc>)[key]!;
    const taxYear = doc.tax_year;
    if (doc.collection) doc.collection.cite = fillCite(doc.collection.cite, taxYear, `${doc.id} collection`);
    for (const line of doc.lines ?? []) {
      for (const refusal of line.refuses ?? []) refusal.cite = fillCite(refusal.cite, taxYear, `${line.id} refusal`);
      line.cite = fillCite(line.cite as unknown as CiteAuthored, taxYear, `${doc.id}.${line.id}`);
    }
    return doc;
  };

  // Forms and defs
  const forms: FormDoc[] = [];
  const defs: FormDoc[] = [];
  for (const name of readdirSync(FORMS_DIR).filter((f) => f.endsWith(".yaml")).sort()) {
    const doc = loadFormOrDef(join(FORMS_DIR, name));
    if (!doc) continue;
    if (doc.kind === "def") defs.push(doc);
    else forms.push(doc);
  }

  // Parameters
  const paramsRaw = parseYaml(readFileSync(PARAMS_PATH, "utf-8")) as { params: ParamsDoc };
  const params = paramsRaw.params;
  for (const [name, entry] of Object.entries(params.values)) {
    entry.cite = fillCite(entry.cite as unknown as CiteAuthored, params.tax_year, `param ${name}`);
  }
  for (const [name, en] of Object.entries(params.enums)) {
    en.cite = fillCite(en.cite as unknown as CiteAuthored, params.tax_year, `enum ${name}`);
  }

  // Tables
  const tables: TableDoc[] = [];
  for (const name of readdirSync(TABLES_DIR).filter((f) => f.endsWith(".yaml")).sort()) {
    const raw = parseYaml(readFileSync(join(TABLES_DIR, name), "utf-8")) as { table: TableDoc };
    const table = raw.table;
    table.cite = fillCite(table.cite as unknown as CiteAuthored, table.tax_year, `table ${table.id}`);
    tables.push(table);
  }

  // Ambiguity register
  const registerRaw = parseYaml(readFileSync(REGISTER_PATH, "utf-8")) as { register: RegisterDoc };
  const register = registerRaw.register;
  for (const entry of register.entries) {
    entry.cite = fillCite(entry.cite as unknown as CiteAuthored, register.tax_year, `register ${entry.id}`);
  }

  // Interview: one question bank for the year, and profiles that name the inputs they ask.
  // A question's prompt is its collection's frame followed by the form line's question text
  // (`source`), and its citation the line's (a roster question's, its collection's), unless the
  // bank states its own; stating one equal to the derived value is an error, so copies of form
  // data do not creep back into the interview.
  const bank = (parseYaml(readFileSync(join(ROOT, "interview", `questions-${YEAR}.yaml`), "utf8")) as { bank: QuestionBank }).bank;
  const bankByInput = new Map(bank.questions.map((q) => [q.input, q]));
  if (bankByInput.size !== bank.questions.length) errors.push("question bank: duplicate inputs");
  const resolveQuestion = (q: BankQuestion): InterviewData["questions"][number] | null => {
    const where = `question ${q.input}`;
    let derivedPrompt: string | undefined;
    let derivedCite: CiteFilled | undefined;
    if (q.input.startsWith("$")) {
      const doc = forms.find((d) => d.collection && "$" + d.id === q.input);
      if (!doc) { errors.push(`${where}: undeclared collection`); return null; }
      derivedCite = doc.collection!.cite;
    } else {
      const doc = forms.find((d) => d.lines.some((l) => l.id === q.input && l.expr.op === "input"));
      const line = doc?.lines.find((l) => l.id === q.input);
      if (!doc || !line) { errors.push(`${where}: undeclared input`); return null; }
      derivedPrompt = (bank.frames[doc.id] ?? "") + (line.expr as { source: string }).source;
      derivedCite = line.cite;
    }
    if (q.prompt !== undefined && q.prompt === derivedPrompt) errors.push(`${where}: prompt repeats the form line's; remove it from the bank`);
    const cite = q.cite === undefined ? derivedCite : fillCite(q.cite, YEAR, where);
    if (q.cite !== undefined && stableStringify(cite) === stableStringify(derivedCite)) errors.push(`${where}: cite repeats the form line's; remove it from the bank`);
    const prompt = q.prompt ?? derivedPrompt;
    if (!prompt || !q.help || !Number.isSafeInteger(q.order)) { errors.push(`invalid ${where}`); return null; }
    return { input: q.input, prompt, help: q.help, order: q.order, cite: cite! };
  };
  const resolved = new Map(bank.questions.flatMap((q) => { const r = resolveQuestion(q); return r ? [[q.input, r] as const] : []; }));
  const loadProfile = (file: string, name: string): InterviewData => {
    const profile = (parseYaml(readFileSync(join(ROOT, "interview", file), "utf8")) as { interview: InterviewProfile }).interview;
    const inputs = profile.questions === "all" ? bank.questions.map((q) => q.input) : profile.questions;
    if (new Set(inputs).size !== inputs.length) errors.push(`${name}: duplicate questions`);
    for (const input of inputs) if (!bankByInput.has(input)) errors.push(`${name}: question ${input} is not in the question bank`);
    return {
      tax_year: profile.tax_year, targets: profile.targets, initial: profile.initial,
      cite: fillCite(profile.cite, YEAR, name),
      questions: inputs.flatMap((input) => resolved.get(input) ?? []),
    };
  };
  const interview = loadProfile(`${YEAR}.yaml`, "interview");
  const salesInterview = loadProfile(`sales-${YEAR}.yaml`, "sales interview");
  const stage4Interview = loadProfile(`stage4-${YEAR}.yaml`, "Stage 4 interview");
  const fullInterview = loadProfile(`full-${YEAR}.yaml`, "full interview");
  // Every document under the year's directories must state that year.
  const stated: [string, number][] = [
    ["sources manifest", (JSON.parse(readFileSync(MANIFEST_PATH, "utf-8")) as { tax_year: number }).tax_year],
    ["params", params.tax_year], ["ambiguity register", register.tax_year],
    ["question bank", bank.tax_year], ["interview", interview.tax_year], ["sales interview", salesInterview.tax_year],
    ["Stage 4 interview", stage4Interview.tax_year], ["full interview", fullInterview.tax_year],
    ...[...forms, ...defs].map((d): [string, number] => [d.id, d.tax_year]),
    ...tables.map((t): [string, number] => [`table ${t.id}`, t.tax_year]),
  ];
  for (const [what, year] of stated) if (year !== YEAR) errors.push(`${what}: tax_year ${year}, but the build is for ${YEAR}`);
  const data: CanonicalData = { forms, defs, params, tables, register };

  // Schema validation on the canonical form.
  const schema = JSON.parse(readFileSync(SCHEMA_PATH, "utf-8")) as {
    $defs: Record<string, unknown>;
    $schema: string;
  };
  const ajv = new Ajv2020({ allErrors: true, strict: false });
  const validateWith = (defName: string) =>
    ajv.compile({ $schema: schema.$schema, $defs: schema.$defs, $ref: `#/$defs/${defName}` });

  const formFileValidator = validateWith("formFile");
  const defFileValidator = validateWith("defFile");
  const paramsValidator = validateWith("paramsFile");
  const tableValidator = validateWith("tableFile");
  const registerValidator = validateWith("registerFile");

  const validate = (validator: ValidateFunction, value: unknown, what: string) => {
    if (!validator(value)) {
      errors.push(`${what}: schema validation failed: ${ajv.errorsText(validator.errors).slice(0, 500)}`);
    }
  };
  validate(validateWith("interview"), interview, "interview");
  validate(validateWith("interview"), salesInterview, "sales interview");
  validate(validateWith("interview"), stage4Interview, "Stage 4 interview");
  validate(validateWith("interview"), fullInterview, "full interview");
  for (const doc of forms) validate(formFileValidator, { form: doc }, `form ${doc.id}`);
  for (const doc of defs) validate(defFileValidator, { def: doc }, `def ${doc.id}`);
  validate(paramsValidator, { params }, "params");
  for (const table of tables) validate(tableValidator, { table }, `table ${table.id}`);
  validate(registerValidator, { register }, "register");

  // Static checks (references, acyclicity, types, guards, citations).
  const checkResult = runChecks(data);
  errors.push(...checkResult.errors);
  stats.push(...checkResult.stats);

  // A line no other line reads must be an interview target or say why it is shown (display);
  // a line marked display must not be read. Unread helpers are how dead logic hides. Every line
  // of every confirmed collection entry is evaluated and printed in the entry's section of the
  // values sheet, so display holds there as on any other form.
  {
    const docs = [...data.forms, ...data.defs];
    const ids = new Set(docs.flatMap((d) => d.lines.map((l) => l.id)));
    const read = new Set<string>();
    const walk = (n: unknown): void => {
      if (typeof n === "string") { if (ids.has(n)) read.add(n); return; }
      if (Array.isArray(n)) { n.forEach(walk); return; }
      if (n && typeof n === "object") for (const [k, v] of Object.entries(n)) if (!["cite", "source", "label", "op", "ref"].includes(k)) walk(v);
    };
    for (const d of docs) for (const l of d.lines) { walk(l.expr); for (const r of l.refuses ?? []) read.add(r.when); if (l.shown_when) read.add(l.shown_when); }
    const targets = new Set([interview, salesInterview, stage4Interview, fullInterview].flatMap((i) => i.targets));
    const asked = new Set([interview, salesInterview, stage4Interview, fullInterview].flatMap((i) => i.questions.map((q) => q.input)));
    for (const d of data.forms) if (d.collection?.implicit && asked.has(`$${d.id}`)) errors.push(`${d.id}: an implicit collection's entry is never asked, but an interview asks $${d.id}`);
    for (const d of data.forms) for (const l of d.lines) {
      if (String(l.printed).startsWith("(") === false) continue; // printed lines are the form's own lines
      const unread = !read.has(l.id) && !targets.has(l.id);
      if (unread && !l.display) errors.push(`${d.id}.${l.id}: no line reads this ${l.expr.op} line and it is not an interview target; remove it or say why it is shown (display)`);
      if (!unread && l.display) errors.push(`${d.id}.${l.id}: marked display but read by another line or an interview target`);
    }
  }
  if (errors.length === 0) errors.push(...checkInterview(data, interview), ...checkSalesInterview(data, salesInterview), ...checkSalesInterview(data, stage4Interview, "stage4"), ...checkSalesInterview(data, fullInterview, "stage5"));
  stats.push("interview: Stage 2 finite domains checked; Stage 3 fixture paths checked for reachability, termination and answer-order invariance (not exhaustive)");

  // Write canonical output.
  if (errors.length === 0) {
    rmSync(OUT_DIR, { recursive: true, force: true });
    mkdirSync(join(OUT_DIR, "tables"), { recursive: true });
    for (const doc of forms) {
      writeFileSync(join(OUT_DIR, `${doc.id}.json`), stableStringify({ form: doc }));
    }
    for (const doc of defs) {
      writeFileSync(join(OUT_DIR, `${doc.id}.json`), stableStringify({ def: doc }));
    }
    writeFileSync(join(OUT_DIR, "interview.json"), stableStringify(interview));
    writeFileSync(join(OUT_DIR, "interview-sales.json"), stableStringify(salesInterview));
    writeFileSync(join(OUT_DIR, "interview-stage4.json"), stableStringify(stage4Interview));
    writeFileSync(join(OUT_DIR, "interview-full.json"), stableStringify(fullInterview));
    writeFileSync(join(OUT_DIR, "params.json"), stableStringify({ params }));
    for (const table of tables) {
      writeFileSync(join(OUT_DIR, "tables", `${table.id}.json`), stableStringify({ table }));
    }
    writeFileSync(join(OUT_DIR, "register.json"), stableStringify({ register }));
    stats.push(`canonical output written to canonical/${YEAR}/`);
  }

  return { data, errors, stats };
}
