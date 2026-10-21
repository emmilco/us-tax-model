// Values-sheet output: each form in printed order, line by line, with the
// value, the citation, and the path explanation.

import { fmtMoney, shortHash } from "./util.js";
import type { CanonicalData, FormDoc } from "./types.js";
import type { EvalResult, Value } from "./eval.js";

export function fmtValue(v: Value): string {
  switch (v.kind) {
    case "count": return String(v.value);
    case "refusal": return `REFUSED: ${v.form}. ${v.remedy} (trigger: ${v.gate}; ${v.cite.doc}, ${v.cite.locator})`;
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

/** The entry keys of collection `doc` on this return, under `parent` when the collection is nested, in key order. */
function entryKeys(doc: FormDoc, parent: string | null, result: EvalResult): string[] {
  const local = new RegExp(`^${parent ? escapeRe(parent) + "\\." : ""}${escapeRe(doc.id)}\\[([^\\]]+)\\]\\.[a-z0-9_]+$`);
  const keys = new Set<string>();
  for (const key of result.derivations.keys()) {
    const m = key.match(local);
    if (m) keys.add(`${parent ? parent + "." : ""}${doc.id}[${m[1]}]`);
  }
  return [...keys].sort();
}

function escapeRe(s: string): string { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

/** One section of the sheet: each line of `doc` that has a value, under `prefix` for a collection entry. */
function pushSection(lines: string[], doc: FormDoc, result: EvalResult, title: string, prefix: string | null): void {
  const keyOf = (id: string) => prefix ? `${prefix}.${id.slice(doc.id.length + 1)}` : id;
  if (!doc.lines.some((l) => result.derivations.has(keyOf(l.id)))) return;
  lines.push(`== ${title} ==`);
  for (const line of doc.lines) {
    const der = result.derivations.get(keyOf(line.id));
    if (!der) continue;
    if (line.shown_when) {
      const cond = result.derivations.get(keyOf(line.shown_when))?.value;
      if (cond?.kind === "bool" && !cond.value) continue; // the form does not report this entry on this line
    }
    lines.push(`  ${line.printed.padEnd(3)} ${line.label}`);
    lines.push(`      = ${fmtValue(der.value)}`);
    if (der.cite) lines.push(`      cite: [${der.cite.doc}] ${der.cite.locator} (${der.cite.revision}; ${shortHash(der.cite.snapshot)})`);
    if (der.notes.length > 0) lines.push(`      note: ${der.notes.join("; ")}`);
  }
  lines.push("");
}

/** A collection entry's section, followed by the sections of the entries nested under it. */
function pushEntry(lines: string[], data: CanonicalData, doc: FormDoc, entry: string, result: EvalResult): void {
  pushSection(lines, doc, result, `${doc.title} — ${entry}`, entry);
  for (const child of data.forms) {
    if (child.collection?.parent !== doc.id) continue;
    for (const sub of entryKeys(child, entry, result)) pushEntry(lines, data, child, sub, result);
  }
}

export function renderValuesSheet(data: CanonicalData, result: EvalResult, targetDocs: string[]): string {
  const lines: string[] = [];
  lines.push("Values sheet — tax year 2025 (not a complete return for all filers)");
  lines.push("");
  for (const docId of targetDocs) {
    const doc = [...data.forms].find((f) => f.id === docId);
    if (!doc) continue;
    if (!doc.collection) { pushSection(lines, doc, result, doc.title, null); continue; }
    if (doc.collection.parent) continue; // printed under its parent entry
    for (const entry of entryKeys(doc, null, result)) pushEntry(lines, data, doc, entry, result);
  }
  const choices = [...result.derivations.entries()].filter(([, d]) => d.op === "choose");
  if (choices.length > 0) {
    lines.push("Path choices (guard wording per the rendered worksheets in rendered/2025/):");
    for (const [key, der] of choices) {
      lines.push(`  ${key}: chose ${fmtValue(der.value)}${der.takenGuardIndex !== undefined ? ` (guard ${der.takenGuardIndex})` : ""}`);
      for (let gi = 0; gi < der.guardsNotTaken.length; gi++) {
        const g = der.guardsNotTaken[gi]!;
        lines.push(`      not taken: guard ${gi} = ${fmtValue(g.value)}`);
      }
    }
    lines.push("");
  }
  lines.push("Derivations:");
  for (const [key, der] of result.derivations) {
    if (der.operands.length) lines.push(`  ${key}: ${der.op}(${der.operands.map(o => `${o.ref} = ${fmtValue(o.value)}`).join("; ")})`);
  }
  for (const note of new Set([...result.derivations.values()].flatMap(d=>d.notes.filter(n=>n.startsWith("Interpretation "))))) lines.push(note);
  lines.push("Scope: Form 1040 lines 1a–37 with the schedules and forms this tool implements and their refusal screens. Unsupported paths are refused with citations. No filing or transmission.");
  lines.push("Rounding: amounts are exact cents; the return-wide whole-dollar rounding setting is deferred (see ambiguities/2025.yaml).");
  lines.push("Estimated tax penalty: not computed; the IRS will figure it (see i1040gi, line 38).");
  lines.push("This is a computation of published IRS forms and instructions; it is not tax or legal advice. Published instructions are not the law itself.");
  lines.push("The user is responsible for the return. Not affiliated with or endorsed by the IRS.");
  return lines.join("\n");
}

export function resultToJson(result: EvalResult): string {
  const values: Record<string, unknown> = {};
  for (const [key, der] of [...result.derivations.entries()].sort((a, b) => (a[0] < b[0] ? -1 : 1))) {
    values[key] = {
      value: der.value,
      op: der.op,
      cite: der.cite,
      operands: der.operands,
      guardsNotTaken: der.guardsNotTaken,
      notes: der.notes,
    };
  }
  return JSON.stringify({ values }, null, 2);
}

export function renderValuesHtml(data: CanonicalData, result: EvalResult, targetDocs: string[]): string {
  const escaped = renderValuesSheet(data, result, targetDocs).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
  return `<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>2025 values sheet</title><body><pre style="white-space:pre-wrap">${escaped}</pre></body></html>`;
}
