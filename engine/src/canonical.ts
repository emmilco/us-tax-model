// Loader for the canonical JSON written by the build.

import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import type { CanonicalData, FormDoc } from "./types.js";
import { yearPath } from "./year.js";

export const CANON_DIR = yearPath("canonical");

export function loadCanonical(dir: string = CANON_DIR): CanonicalData {
  const forms: FormDoc[] = [];
  const defs: FormDoc[] = [];
  for (const name of readdirSync(dir).filter((f) => f.endsWith(".json")).sort()) {
    const raw = JSON.parse(readFileSync(join(dir, name), "utf-8")) as { form?: FormDoc; def?: FormDoc };
    if (raw.form) forms.push(raw.form);
    if (raw.def) defs.push(raw.def);
  }
  const params = (JSON.parse(readFileSync(join(dir, "params.json"), "utf-8")) as { params: CanonicalData["params"] })
    .params;
  const tables = readdirSync(join(dir, "tables"))
    .filter((f) => f.endsWith(".json"))
    .sort()
    .map(
      (f) =>
        (JSON.parse(readFileSync(join(dir, "tables", f), "utf-8")) as { table: CanonicalData["tables"][number] })
          .table,
    );
  const register = (JSON.parse(readFileSync(join(dir, "register.json"), "utf-8")) as {
    register: CanonicalData["register"];
  }).register;
  // New York (decision C1): parameters and register entries written beside the federal ones by the
  // build, merged here so every reader sees one parameter set and one register.
  const nyParamsPath = join(dir, "params-ny.json");
  if (existsSync(nyParamsPath)) {
    const ny = (JSON.parse(readFileSync(nyParamsPath, "utf-8")) as { params: CanonicalData["params"] }).params;
    params.enums = { ...params.enums, ...(ny.enums ?? {}) };
    params.values = { ...params.values, ...ny.values };
  }
  const nyRegisterPath = join(dir, "register-ny.json");
  if (existsSync(nyRegisterPath)) {
    const ny = (JSON.parse(readFileSync(nyRegisterPath, "utf-8")) as { register: CanonicalData["register"] }).register;
    register.entries = [...register.entries, ...ny.entries];
  }
  return { forms, defs, params, tables, register };
}
