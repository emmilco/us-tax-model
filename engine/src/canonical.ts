// Loader for the canonical JSON written by the build.

import { readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import type { CanonicalData, FormDoc } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
export const CANON_DIR = join(ROOT, "canonical", "2025");

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
  return { forms, defs, params, tables, register };
}
