// Build: read the authored YAML, resolve citations against the source
// manifest, write canonical JSON, validate against the schema, and run the
// static checks. Fails with a non-zero exit on any error.

import { mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { Ajv2020 } from "ajv/dist/2020.js";
import type { ValidateFunction } from "ajv";
import { stableStringify } from "./util.js";
import { runChecks } from "./check.js";
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
const MANIFEST_PATH = join(ROOT, "sources", "2025", "manifest.json");
const SCHEMA_PATH = join(ROOT, "schema", "data.schema.json");
const FORMS_DIR = join(ROOT, "forms", "2025");
const TABLES_DIR = join(ROOT, "tables", "2025");
const PARAMS_PATH = join(ROOT, "params", "2025.yaml");
const REGISTER_PATH = join(ROOT, "ambiguities", "2025.yaml");
const OUT_DIR = join(ROOT, "canonical", "2025");

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
      errors.push(`${where}: cite doc '${cite.doc}' not in sources/2025/manifest.json`);
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
    for (const line of doc.lines ?? []) {
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
  for (const doc of forms) validate(formFileValidator, { form: doc }, `form ${doc.id}`);
  for (const doc of defs) validate(defFileValidator, { def: doc }, `def ${doc.id}`);
  validate(paramsValidator, { params }, "params");
  for (const table of tables) validate(tableValidator, { table }, `table ${table.id}`);
  validate(registerValidator, { register }, "register");

  // Static checks (references, acyclicity, types, guards, citations).
  const checkResult = runChecks(data);
  errors.push(...checkResult.errors);
  stats.push(...checkResult.stats);

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
    writeFileSync(join(OUT_DIR, "params.json"), stableStringify({ params }));
    for (const table of tables) {
      writeFileSync(join(OUT_DIR, "tables", `${table.id}.json`), stableStringify({ table }));
    }
    writeFileSync(join(OUT_DIR, "register.json"), stableStringify({ register }));
    stats.push(`canonical output written to canonical/2025/`);
  }

  return { data, errors, stats };
}
