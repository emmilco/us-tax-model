// Build: read the authored YAML, resolve citations against the source
// manifest, write canonical JSON, validate against the schema, and run the
// static checks. Fails with a non-zero exit on any error.

import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { Ajv2020 } from "ajv/dist/2020.js";
import type { ValidateFunction } from "ajv";
import { isMarkedLine, stableStringify } from "./util.js";
import { entrySyntax, type InterviewData, type RosterChoice } from "./interview.js";
import { checkInterview, checkSalesInterview } from "./interview-check.js";
import { defaultsProblems, loadFixtureCases, walkedCases, yearDefaultsFiles } from "./fixture-inputs.js";
import { runChecks } from "./check.js";
import { isStructured, parseStructured, textSummary } from "./text.js";
import { YEAR, nyPath, yearPath } from "./year.js";
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
// The New York tree (decision C1): sources/ny/<year>/, forms/ny/<year>/, tables/ny/<year>/,
// params/ny/<year>.yaml, ambiguities/ny/<year>.yaml. Each part is optional, so a tree without
// New York data builds exactly as before. New York parameters, register entries, documents and
// tables are named `ny.` / `ny_`; they are checked with the federal data in one canonical build
// and written to files of their own (ny_*.json, tables/ny_*.json, params-ny.json,
// register-ny.json), so every federal canonical file is byte-identical with or without them.
const NY_MANIFEST_PATH = nyPath("sources", "manifest.json");
const NY_FORMS_DIR = nyPath("forms");
const NY_TABLES_DIR = nyPath("tables");
const NY_PARAMS_PATH = join(ROOT, "params", "ny", `${YEAR}.yaml`);
const NY_REGISTER_PATH = join(ROOT, "ambiguities", "ny", `${YEAR}.yaml`);

interface BankQuestion { input: string; order: number; help?: string; prompt?: string; cite?: CiteAuthored; choices?: RosterChoice[]; value_labels?: Record<string, string> }
interface QuestionBank { tax_year: number; frames: Record<string, string>; questions: BankQuestion[] }
interface InterviewProfile { tax_year: number; targets: string[]; initial: InterviewData["initial"]; cite: CiteAuthored; questions: string[] | "all"; questions_from?: string; targets_from?: string }

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
  const nyManifestYear = existsSync(NY_MANIFEST_PATH) ? (JSON.parse(readFileSync(NY_MANIFEST_PATH, "utf-8")) as { tax_year: number }).tax_year : YEAR;
  if (existsSync(NY_MANIFEST_PATH)) {
    for (const entry of (JSON.parse(readFileSync(NY_MANIFEST_PATH, "utf-8")).documents as ManifestEntry[])) {
      if (!entry.id.startsWith("ny_")) errors.push(`sources/ny/${YEAR}/manifest.json: document id '${entry.id}' must start with ny_`);
      if (manifest.has(entry.id)) errors.push(`sources/ny/${YEAR}/manifest.json: document id '${entry.id}' is also a federal document`);
      manifest.set(entry.id, entry);
    }
  }

  const fillCite = (cite: CiteAuthored | undefined, taxYear: number, where: string): CiteFilled => {
    const fallback: CiteFilled = { doc: "?", tax_year: taxYear, revision: "?", locator: "?", snapshot: "?" };
    if (!cite || typeof cite.doc !== "string" || typeof cite.locator !== "string") {
      errors.push(`${where}: missing cite (doc and locator are required)`);
      return fallback;
    }
    const source = manifest.get(cite.doc);
    if (!source) {
      errors.push(`${where}: cite doc '${cite.doc}' not in sources/${YEAR}/manifest.json or sources/ny/${YEAR}/manifest.json`);
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
  const federalDocIds = new Set([...forms, ...defs].map((d) => d.id));
  if (existsSync(NY_FORMS_DIR)) {
    for (const name of readdirSync(NY_FORMS_DIR).filter((f) => f.endsWith(".yaml")).sort()) {
      const doc = loadFormOrDef(join(NY_FORMS_DIR, name));
      if (!doc) continue;
      if (!doc.id.startsWith("ny_")) errors.push(`forms/ny/${YEAR}/${name}: document id '${doc.id}' must start with ny_`);
      if (federalDocIds.has(doc.id)) errors.push(`forms/ny/${YEAR}/${name}: document id '${doc.id}' is also a federal document`);
      if (doc.kind === "def") defs.push(doc);
      else forms.push(doc);
    }
  }

  // Structured text (text.ts): a line break is allowed only in the text shown as a question or help, and there
  // only in the Markdown subset. A structured label is referred to by its first line, which must name one line.
  for (const doc of [...forms, ...defs]) {
    const textField = (where: string, text: unknown) => {
      if (typeof text !== "string") return;
      for (const p of parseStructured(text).problems) errors.push(`${where}: structured text ${p}`);
    };
    const stray = (where: string, node: unknown, allowed: ReadonlySet<string>): void => {
      if (Array.isArray(node)) { node.forEach((v) => stray(where, v, new Set())); return; }
      if (!node || typeof node !== "object") return;
      for (const [k, v] of Object.entries(node)) {
        if (typeof v === "string") { if (v.includes("\n") && !allowed.has(k)) errors.push(`${where}: '${k}' has a line break; only label, an input's source and note may be structured text`); }
        else if (k !== "lines") stray(where, v, k === "expr" && (v as { op?: string }).op === "input" ? new Set(["source"]) : new Set());
      }
    };
    stray(doc.id, doc, new Set(["note"]));
    textField(`${doc.id} note`, doc.note);
    for (const line of doc.lines ?? []) {
      stray(line.id, line, new Set(["label", "note"]));
      textField(`${line.id} label`, line.label);
      textField(`${line.id} note`, line.note);
      if (line.expr?.op === "input") textField(`${line.id} source`, (line.expr as { source?: unknown }).source);
      if (isStructured(line.label) && doc.lines.some((o) => o !== line && textSummary(o.label) === textSummary(line.label))) {
        errors.push(`${line.id} label: its first line "${textSummary(line.label)}" names another line of ${doc.id} too; a structured label is referred to by its first line`);
      }
    }
  }

  // Parameters
  const paramsRaw =parseYaml(readFileSync(PARAMS_PATH, "utf-8")) as { params: ParamsDoc };
  const params = paramsRaw.params;
  for (const [name, entry] of Object.entries(params.values)) {
    entry.cite = fillCite(entry.cite as unknown as CiteAuthored, params.tax_year, `param ${name}`);
  }
  for (const [name, en] of Object.entries(params.enums)) {
    en.cite = fillCite(en.cite as unknown as CiteAuthored, params.tax_year, `enum ${name}`);
  }

  // New York parameters: a document of their own, every name prefixed `ny.`, merged into the
  // checked data but written to params-ny.json.
  let nyParams: ParamsDoc | null = null;
  if (existsSync(NY_PARAMS_PATH)) {
    nyParams = (parseYaml(readFileSync(NY_PARAMS_PATH, "utf-8")) as { params: ParamsDoc }).params;
    nyParams.enums ??= {};
    for (const [name, entry] of Object.entries(nyParams.values)) {
      if (!name.startsWith("ny.")) errors.push(`params/ny/${YEAR}.yaml: parameter '${name}' must start with ny.`);
      if (name in params.values) errors.push(`params/ny/${YEAR}.yaml: parameter '${name}' is also federal`);
      entry.cite = fillCite(entry.cite as unknown as CiteAuthored, nyParams.tax_year, `param ${name}`);
    }
    for (const [name, en] of Object.entries(nyParams.enums)) {
      if (!name.startsWith("ny_")) errors.push(`params/ny/${YEAR}.yaml: enum '${name}' must start with ny_`);
      if (name in params.enums) errors.push(`params/ny/${YEAR}.yaml: enum '${name}' is also federal`);
      en.cite = fillCite(en.cite as unknown as CiteAuthored, nyParams.tax_year, `enum ${name}`);
    }
  }

  // Tables
  const tables: TableDoc[] = [];
  const loadTables = (dir: string, ny: boolean) => {
    for (const name of readdirSync(dir).filter((f) => f.endsWith(".yaml")).sort()) {
      const raw = parseYaml(readFileSync(join(dir, name), "utf-8")) as { table: TableDoc };
      const table = raw.table;
      if (ny && !table.id.startsWith("ny_")) errors.push(`tables/ny/${YEAR}/${name}: table id '${table.id}' must start with ny_`);
      if (ny && tables.some((t) => t.id === table.id)) errors.push(`tables/ny/${YEAR}/${name}: table id '${table.id}' is also federal`);
      table.cite = fillCite(table.cite as unknown as CiteAuthored, table.tax_year, `table ${table.id}`);
      tables.push(table);
    }
  };
  loadTables(TABLES_DIR, false);
  if (existsSync(NY_TABLES_DIR)) loadTables(NY_TABLES_DIR, true);

  // Ambiguity register
  const registerRaw = parseYaml(readFileSync(REGISTER_PATH, "utf-8")) as { register: RegisterDoc };
  const register = registerRaw.register;
  for (const entry of register.entries) {
    entry.cite = fillCite(entry.cite as unknown as CiteAuthored, register.tax_year, `register ${entry.id}`);
  }
  let nyRegister: RegisterDoc | null = null;
  if (existsSync(NY_REGISTER_PATH)) {
    nyRegister = (parseYaml(readFileSync(NY_REGISTER_PATH, "utf-8")) as { register: RegisterDoc }).register;
    for (const entry of nyRegister.entries) {
      if (!entry.id.startsWith("amb.ny.")) errors.push(`ambiguities/ny/${YEAR}.yaml: entry '${entry.id}' must start with amb.ny.`);
      entry.cite = fillCite(entry.cite as unknown as CiteAuthored, nyRegister.tax_year, `register ${entry.id}`);
    }
  }

  // Interview: one question bank for the year, and profiles that name the inputs they ask.
  // A question's prompt is its collection's frame followed by the form line's question text
  // (`source`), and its citation the line's (a roster question's, its collection's), unless the
  // bank states its own; stating one equal to the derived value is an error, so copies of form
  // data do not creep back into the interview.
  const bank = (parseYaml(readFileSync(join(ROOT, "interview", `questions-${YEAR}.yaml`), "utf8")) as { bank: QuestionBank }).bank;
  // The New York question bank (decision C5), merged into the federal one: its inputs are New York lines
  // (ids ny_) and rosters ($ny_), asked by the New York profile only.
  const NY_BANK = join(ROOT, "interview", "ny", `questions-${YEAR}.yaml`);
  const NY_PROFILE = join(ROOT, "interview", "ny", `${YEAR}.yaml`);
  // "all" in a profile means every federal question, so the federal profiles are unchanged by the New York bank.
  const federalInputs = bank.questions.map((q) => q.input);
  if (existsSync(NY_BANK)) {
    const nyBank = (parseYaml(readFileSync(NY_BANK, "utf8")) as { bank: QuestionBank }).bank;
    if (nyBank.tax_year !== YEAR) errors.push(`New York question bank: tax_year ${nyBank.tax_year}, but the build is for ${YEAR}`);
    for (const q of nyBank.questions) if (!q.input.replace(/^\$/, "").startsWith("ny_")) errors.push(`New York question bank: input '${q.input}' is not a New York line`);
    bank.questions = [...bank.questions, ...nyBank.questions];
    bank.frames = { ...bank.frames, ...nyBank.frames };
  }
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
    if (!prompt || (q.help !== undefined && !q.help) || !Number.isSafeInteger(q.order)) { errors.push(`invalid ${where}`); return null; }
    // Entry syntax belongs to the clients (the CLI's entry hint, the page's widgets), not to the wording.
    for (const [field, text] of [["prompt", prompt], ["help", q.help ?? ""]] as const) {
      const syntax = entrySyntax(text);
      if (syntax) errors.push(`${where}: the ${field} states entry syntax (${syntax}); say what to answer, not how to type it`);
      for (const p of parseStructured(text).problems) errors.push(`${where}: the ${field}'s structured text ${p}`);
    }
    if (q.choices !== undefined) {
      const ok = q.input.startsWith("$") && Array.isArray(q.choices) && q.choices.length >= 2 && q.choices.every((c) =>
        typeof c.label === "string" && c.label !== "" && Array.isArray(c.value) && c.value.every((k) => /^[a-zA-Z0-9_-]+$/.test(k))
        && new Set(c.value).size === c.value.length && stableStringify(Object.keys(c.labels ?? {}).sort()) === stableStringify([...c.value].sort()));
      if (!ok) errors.push(`${where}: choices must be a roster's, at least two, each a label, distinct entry keys and a label for each key`);
    }
    // Value labels present an enum input's values as the facts they stand for; each label names exactly one value,
    // every value has one, and the answer is still the value.
    if (q.value_labels !== undefined) {
      const line = forms.flatMap((d) => d.lines).find((l) => l.id === q.input && l.expr.op === "input");
      const enumName = /^Enum\(([a-z_]+)\)$/.exec(line?.type ?? "")?.[1];
      const values = enumName ? (params.enums[enumName] ?? nyParams?.enums[enumName])?.values : undefined;
      const labels = q.value_labels && typeof q.value_labels === "object" && !Array.isArray(q.value_labels) ? q.value_labels : null;
      if (!values) errors.push(`${where}: value_labels are for an enum input`);
      else if (!labels || stableStringify(Object.keys(labels).sort()) !== stableStringify([...values].sort())) {
        errors.push(`${where}: value_labels must label every value of the enum (${values.join(", ")}) and no other`);
      } else {
        const texts = Object.values(labels);
        if (texts.some((t) => typeof t !== "string" || t.trim() === "" || t.includes("\n"))) errors.push(`${where}: each value label is one non-empty line`);
        else if (new Set(texts).size !== texts.length) errors.push(`${where}: two values share a label; each label maps to exactly one value`);
        for (const t of texts) { const syntax = typeof t === "string" ? entrySyntax(t) : null; if (syntax) errors.push(`${where}: a value label states entry syntax (${syntax})`); }
      }
    }
    return { input: q.input, prompt, help: q.help ?? "", order: q.order, cite: cite!, ...(q.choices ? { choices: q.choices } : {}),
      ...(q.value_labels ? { value_labels: q.value_labels } : {}) };
  };
  const resolved = new Map(bank.questions.flatMap((q) => { const r = resolveQuestion(q); return r ? [[q.input, r] as const] : []; }));
  const loadProfile = (file: string, name: string): InterviewData => {
    const profile = (parseYaml(readFileSync(join(ROOT, "interview", file), "utf8")) as { interview: InterviewProfile }).interview;
    const own = profile.questions === "all" ? federalInputs : profile.questions;
    // questions_from: a profile (in interview/) whose questions come first, as the New York profile takes the
    // federal full profile's.
    const before = profile.questions_from
      ? (parseYaml(readFileSync(join(ROOT, "interview", profile.questions_from), "utf8")) as { interview: InterviewProfile }).interview.questions
      : [];
    const inputs = [...(before === "all" ? federalInputs : before), ...own];
    if (new Set(inputs).size !== inputs.length) errors.push(`${name}: duplicate questions`);
    for (const input of inputs) if (!bankByInput.has(input)) errors.push(`${name}: question ${input} is not in the question bank`);
    // targets_from: a profile whose targets come first (the New York profile takes the federal full profile's, so a
    // refused federal return refuses it too).
    const targetsBefore = profile.targets_from
      ? (parseYaml(readFileSync(join(ROOT, "interview", profile.targets_from), "utf8")) as { interview: InterviewProfile }).interview.targets
      : [];
    return {
      tax_year: profile.tax_year, targets: [...targetsBefore, ...profile.targets], initial: profile.initial,
      cite: fillCite(profile.cite, YEAR, name),
      questions: inputs.flatMap((input) => resolved.get(input) ?? []),
    };
  };
  const interview = loadProfile(`${YEAR}.yaml`, "interview");
  const salesInterview = loadProfile(`sales-${YEAR}.yaml`, "sales interview");
  const stage4Interview = loadProfile(`stage4-${YEAR}.yaml`, "Stage 4 interview");
  const fullInterview = loadProfile(`full-${YEAR}.yaml`, "full interview");
  const nyInterview = existsSync(NY_PROFILE) ? loadProfile(join("ny", `${YEAR}.yaml`), "New York interview") : null;
  // The refusal gates that are consistency checks, each with the explanation the web UI shows for its conflict
  // (presentation only). Every key must be a gate line: a line that some line's `refuses` names in `when`.
  const CONFLICTS = join(ROOT, "interview", `conflict_checks-${YEAR}.yaml`);
  const conflictChecks = existsSync(CONFLICTS)
    ? parseYaml(readFileSync(CONFLICTS, "utf8")) as { tax_year: number; conflicts: Record<string, string> }
    : null;
  if (conflictChecks) {
    const gateLines = new Set([...forms, ...defs].flatMap((d) => d.lines.flatMap((l) => (l.refuses ?? []).map((r) => r.when))));
    if (!conflictChecks.conflicts || typeof conflictChecks.conflicts !== "object") errors.push(`conflict_checks-${YEAR}.yaml: no conflicts map`);
    for (const [gate, text] of Object.entries(conflictChecks.conflicts ?? {})) {
      const where = `conflict_checks-${YEAR}.yaml: ${gate}`;
      if (!gateLines.has(gate)) errors.push(`${where}: not a refusal gate (no line's refuses names it)`);
      if (typeof text !== "string" || text.trim() === "" || text.includes("\n")) errors.push(`${where}: the explanation must be one non-empty paragraph`);
      else if (/cannot prepare|outside this tool|not supported/i.test(text)) errors.push(`${where}: the explanation of a conflict must not describe it as unsupported`);
    }
  }
  // Every document under the year's directories must state that year.
  const stated: [string, number][] = [
    ["sources manifest", (JSON.parse(readFileSync(MANIFEST_PATH, "utf-8")) as { tax_year: number }).tax_year],
    ["params", params.tax_year], ["ambiguity register", register.tax_year],
    ["question bank", bank.tax_year], ["interview", interview.tax_year], ["sales interview", salesInterview.tax_year],
    ["Stage 4 interview", stage4Interview.tax_year], ["full interview", fullInterview.tax_year],
    ...(nyInterview ? [["New York interview", nyInterview.tax_year] as [string, number]] : []),
    ...(conflictChecks ? [["conflict checks", conflictChecks.tax_year] as [string, number]] : []),
    ...[...forms, ...defs].map((d): [string, number] => [d.id, d.tax_year]),
    ...tables.map((t): [string, number] => [`table ${t.id}`, t.tax_year]),
    ...(existsSync(NY_MANIFEST_PATH) ? [["New York sources manifest", nyManifestYear] as [string, number]] : []),
    ...(nyParams ? [["New York params", nyParams.tax_year] as [string, number]] : []),
    ...(nyRegister ? [["New York ambiguity register", nyRegister.tax_year] as [string, number]] : []),
  ];
  for (const [what, year] of stated) if (year !== YEAR) errors.push(`${what}: tax_year ${year}, but the build is for ${YEAR}`);
  // The checked data: federal and New York together.
  const data: CanonicalData = {
    forms, defs, tables,
    params: nyParams ? { tax_year: params.tax_year, enums: { ...params.enums, ...nyParams.enums }, values: { ...params.values, ...nyParams.values } } : params,
    register: nyRegister ? { tax_year: register.tax_year, entries: [...register.entries, ...nyRegister.entries] } : register,
  };

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
  if (nyInterview) validate(validateWith("interview"), nyInterview, "New York interview");
  for (const doc of forms) validate(formFileValidator, { form: doc }, `form ${doc.id}`);
  for (const doc of defs) validate(defFileValidator, { def: doc }, `def ${doc.id}`);
  validate(paramsValidator, { params }, "params");
  if (nyParams) validate(paramsValidator, { params: nyParams }, "New York params");
  for (const table of tables) validate(tableValidator, { table }, `table ${table.id}`);
  validate(registerValidator, { register }, "register");
  if (nyRegister) validate(registerValidator, { register: nyRegister }, "New York register");

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
    const profiles = [interview, salesInterview, stage4Interview, fullInterview, ...(nyInterview ? [nyInterview] : [])];
    const targets = new Set(profiles.flatMap((i) => i.targets));
    const asked = new Set(profiles.flatMap((i) => i.questions.map((q) => q.input)));
    for (const d of data.forms) if (d.collection?.implicit && asked.has(`$${d.id}`)) errors.push(`${d.id}: an implicit collection's entry is never asked, but an interview asks $${d.id}`);
    for (const d of data.forms) for (const l of d.lines) {
      if (!isMarkedLine(l)) continue; // numbered lines are the form's own lines; helper, column and worksheet-step lines are checked
      const unread = !read.has(l.id) && !targets.has(l.id);
      if (unread && !l.display) errors.push(`${d.id}.${l.id}: no line reads this ${l.expr.op} line and it is not an interview target; remove it or say why it is shown (display)`);
      if (!unread && l.display) errors.push(`${d.id}.${l.id}: marked display but read by another line or an interview target`);
    }
  }
  // The interview path checks walk the year's fixtures; a year being adopted has none until
  // tools/fixtures_year.py carries them over, which needs this build.
  // The fixtures' test-data defaults: one per input and roster, each a value the input accepts.
  if (errors.length === 0) errors.push(...defaultsProblems(data, yearDefaultsFiles()));
  if (!existsSync(yearPath("fixtures"))) stats.push(`interview path checks skipped: no fixtures/${YEAR}/ yet`);
  else if (errors.length === 0) errors.push(...checkInterview(data, interview), ...checkSalesInterview(data, salesInterview, walkedCases("sales", data)), ...checkSalesInterview(data, stage4Interview, walkedCases("stage4", data)), ...checkSalesInterview(data, fullInterview, walkedCases("full", data)));
  // The New York profile walks the New York fixtures' paths (fixtures/ny/<year>/), once they exist.
  if (nyInterview && errors.length === 0 && existsSync(nyPath("fixtures"))) {
    // As federally (stages 3 to 5 only), the walk covers the hand-authored stage fixtures: class M cases keep only the
    // answers their route reads, and mutation cases exist to kill mutants, so neither is an interview path.
    const ny = loadFixtureCases("ny", data).filter((c) => !c.file.startsWith("classm") && c.file !== "mutation.json");
    errors.push(...checkSalesInterview(data, nyInterview, ny, 600).map((e) => `New York interview: ${e}`));
  }
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
    if (nyInterview) writeFileSync(join(OUT_DIR, "interview-ny.json"), stableStringify(nyInterview));
    if (conflictChecks) writeFileSync(join(OUT_DIR, "conflicts.json"), stableStringify({ conflicts: conflictChecks.conflicts }));
    writeFileSync(join(OUT_DIR, "params.json"), stableStringify({ params }));
    for (const table of tables) {
      writeFileSync(join(OUT_DIR, "tables", `${table.id}.json`), stableStringify({ table }));
    }
    writeFileSync(join(OUT_DIR, "register.json"), stableStringify({ register }));
    if (nyParams) writeFileSync(join(OUT_DIR, "params-ny.json"), stableStringify({ params: nyParams }));
    if (nyRegister) writeFileSync(join(OUT_DIR, "register-ny.json"), stableStringify({ register: nyRegister }));
    stats.push(`canonical output written to canonical/${YEAR}/`);
  }

  return { data, errors, stats };
}
