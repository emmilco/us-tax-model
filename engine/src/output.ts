// Values-sheet output: each form in printed order, line by line, with the
// value, the citation, and the path explanation.

import { fmtMoney, shortHash } from "./util.js";
import type { CanonicalData, FormDoc } from "./types.js";
import type { EvalResult, Value } from "./eval.js";

export function fmtValue(v: Value): string {
  switch (v.kind) {
    case "money":
      return fmtMoney(v.cents);
    case "rate":
      return `${v.num}/${v.den}`;
    case "bool":
      return v.value ? "true" : "false";
    case "enum":
      return v.value;
    case "unknown":
      return `UNKNOWN (${v.reason})`;
  }
}

export function renderValuesSheet(data: CanonicalData, result: EvalResult, targetDocs: string[]): string {
  const lines: string[] = [];
  lines.push("Values sheet — tax year 2025 (Stage 1 slice)");
  lines.push("");
  for (const docId of targetDocs) {
    const doc = [...data.forms].find((f) => f.id === docId);
    if (!doc) continue;
    lines.push(`== ${doc.title} ==`);
    for (const line of doc.lines) {
      const key = `${doc.id}.${line.id}`;
      const der = result.derivations.get(key);
      const value = der ? fmtValue(der.value) : "(not evaluated)";
      lines.push(`  ${line.printed.padEnd(3)} ${line.label}`);
      lines.push(`      = ${value}`);
      if (der && der.cite) {
        lines.push(`      cite: [${der.cite.doc}] ${der.cite.locator} (${der.cite.revision}; ${shortHash(der.cite.snapshot)})`);
      }
      if (der && der.notes.length > 0) {
        lines.push(`      note: ${der.notes.join("; ")}`);
      }
    }
    lines.push("");
  }
  lines.push("This is a computation of published IRS forms and instructions; it is not tax advice.");
  lines.push("The user is responsible for the return. Not affiliated with or endorsed by the IRS.");
  return lines.join("\n");
}

export function resultToJson(result: EvalResult): string {
  const values: Record<string, unknown> = {};
  for (const [key, der] of [...result.derivations.entries()].sort((a, b) => (a[0] < b[0] ? -1 : 1))) {
    values[key] = {
      value: der.value,
      op: der.op,
      cite: der.cite ? { doc: der.cite.doc, locator: der.cite.locator } : null,
      guardsNotTaken: der.guardsNotTaken,
      notes: der.notes,
    };
  }
  return JSON.stringify({ values }, null, 2);
}
