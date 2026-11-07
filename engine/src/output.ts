// Values-sheet output: each form in printed order, line by line, with the
// value, the citation, and the path explanation.

import { fmtMoney, shortHash } from "./util.js";
import type { CanonicalData, FormDoc } from "./types.js";
import type { Derivation, EvalResult, Value } from "./eval.js";
import { YEAR } from "./year.js";
import { indentRest } from "./text.js";

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

/** One line of a values-sheet section. `shown` is false when the line's `shown_when` test is false on this return:
 * the form does not report the entry on that line, and the sheet omits it. */
export interface SheetLine {
  key: string;
  printed: string;
  label: string;
  value: Value;
  status: "value" | "unknown" | "refused";
  cite: Derivation["cite"];
  notes: string[];
  shownWhen: string | null;
  shown: boolean;
}

/** One section: a form, worksheet or collection entry with at least one evaluated line. `entry` is the entry key
 * (for example `person[taxpayer].w2[a]`) or null for a form that is not a collection. */
export interface SheetSection { doc: string; title: string; entry: string | null; lines: SheetLine[] }

/** The values sheet as data; `renderValuesSheetText` prints it as the text sheet. */
export interface ValuesSheet {
  sections: SheetSection[];
  choices: { key: string; value: Value; takenGuardIndex?: number; guardsNotTaken: Value[] }[];
  derivations: { key: string; op: string; operands: { ref: string; value: Value }[] }[];
  interpretations: string[];
  notices: string[];
}

export function lineStatus(v: Value): SheetLine["status"] {
  return v.kind === "refusal" ? "refused" : v.kind === "unknown" ? "unknown" : "value";
}

/** One section of the sheet: each line of `doc` that has a value, under `prefix` for a collection entry. */
function pushSection(sections: SheetSection[], doc: FormDoc, result: EvalResult, title: string, prefix: string | null): void {
  const keyOf = (id: string) => prefix ? `${prefix}.${id.slice(doc.id.length + 1)}` : id;
  if (!doc.lines.some((l) => result.derivations.has(keyOf(l.id)))) return;
  const lines: SheetLine[] = [];
  for (const line of doc.lines) {
    const key = keyOf(line.id);
    const der = result.derivations.get(key);
    if (!der) continue;
    let shown = true;
    if (line.shown_when) {
      const cond = result.derivations.get(keyOf(line.shown_when))?.value;
      if (cond?.kind === "bool" && !cond.value) shown = false; // the form does not report this entry on this line
    }
    lines.push({ key, printed: line.printed, label: line.label, value: der.value, status: lineStatus(der.value), cite: der.cite,
      notes: der.notes, shownWhen: line.shown_when ? keyOf(line.shown_when) : null, shown });
  }
  sections.push({ doc: doc.id, title, entry: prefix, lines });
}

/** A collection entry's section, followed by the sections of the entries nested under it. */
function pushEntry(sections: SheetSection[], data: CanonicalData, doc: FormDoc, entry: string, result: EvalResult): void {
  pushSection(sections, doc, result, `${doc.title} — ${entry}`, entry);
  for (const child of data.forms) {
    if (child.collection?.parent !== doc.id) continue;
    for (const sub of entryKeys(child, entry, result)) pushEntry(sections, data, child, sub, result);
  }
}

/** The values sheet of `result`: each form of `targetDocs` in printed order, line by line; collection entries under
 * their parents; the path choices, the derivations and the standing notices. */
export function valuesSheet(data: CanonicalData, result: EvalResult, targetDocs: string[]): ValuesSheet {
  const sections: SheetSection[] = [];
  for (const docId of targetDocs) {
    const doc = [...data.forms].find((f) => f.id === docId);
    if (!doc) continue;
    if (!doc.collection) { pushSection(sections, doc, result, doc.title, null); continue; }
    if (doc.collection.parent) continue; // printed under its parent entry
    for (const entry of entryKeys(doc, null, result)) pushEntry(sections, data, doc, entry, result);
  }
  const choices = [...result.derivations.entries()].filter(([, d]) => d.op === "choose").map(([key, der]) => ({
    key, value: der.value, ...(der.takenGuardIndex !== undefined ? { takenGuardIndex: der.takenGuardIndex } : {}),
    guardsNotTaken: der.guardsNotTaken.map((g) => g.value) }));
  const derivations = [...result.derivations.entries()].filter(([, der]) => der.operands.length)
    .map(([key, der]) => ({ key, op: der.op, operands: der.operands }));
  const interpretations = [...new Set([...result.derivations.values()].flatMap(d=>d.notes.filter(n=>n.startsWith("Interpretation "))))];
  return { sections, choices, derivations, interpretations, notices: standingNotices() };
}

/** The text values sheet: a rendering of `valuesSheet`. */
export function renderValuesSheetText(sheet: ValuesSheet): string {
  const lines: string[] = [];
  lines.push(`Values sheet — tax year ${YEAR} (not a complete return for all filers)`);
  lines.push("");
  for (const section of sheet.sections) {
    lines.push(`== ${section.title} ==`);
    for (const line of section.lines) {
      if (!line.shown) continue;
      lines.push(`  ${line.printed.padEnd(3)} ${indentRest(line.label, "      ")}`);
      lines.push(`      = ${fmtValue(line.value)}`);
      if (line.cite) lines.push(`      cite: [${line.cite.doc}] ${line.cite.locator} (${line.cite.revision}; ${shortHash(line.cite.snapshot)})`);
      if (line.notes.length > 0) lines.push(`      note: ${line.notes.join("; ")}`);
    }
    lines.push("");
  }
  if (sheet.choices.length > 0) {
    lines.push(`Path choices (guard wording per the rendered worksheets in rendered/${YEAR}/):`);
    for (const choice of sheet.choices) {
      lines.push(`  ${choice.key}: chose ${fmtValue(choice.value)}${choice.takenGuardIndex !== undefined ? ` (guard ${choice.takenGuardIndex})` : ""}`);
      for (let gi = 0; gi < choice.guardsNotTaken.length; gi++) {
        lines.push(`      not taken: guard ${gi} = ${fmtValue(choice.guardsNotTaken[gi]!)}`);
      }
    }
    lines.push("");
  }
  lines.push("Derivations:");
  for (const der of sheet.derivations) {
    lines.push(`  ${der.key}: ${der.op}(${der.operands.map(o => `${o.ref} = ${fmtValue(o.value)}`).join("; ")})`);
  }
  lines.push(...sheet.interpretations);
  lines.push(...sheet.notices);
  return lines.join("\n");
}

export function renderValuesSheet(data: CanonicalData, result: EvalResult, targetDocs: string[]): string {
  return renderValuesSheetText(valuesSheet(data, result, targetDocs));
}

/** Spec 8's standing notices, closing every output: the values sheet, its HTML form and every JSON result. */
export function standingNotices(): string[] {
  return [
    "Scope: Form 1040 lines 1a–37 with the schedules and forms this tool implements and their refusal screens. Unsupported paths are refused with citations. No filing or transmission.",
    `Rounding: amounts are exact cents; the return-wide whole-dollar rounding setting is deferred (see ambiguities/${YEAR}.yaml).`,
    "Estimated tax penalty: not computed; the IRS will figure it (see i1040gi, line 38).",
    "This is a computation of published IRS forms and instructions; it is not tax or legal advice. Published instructions are not the law itself.",
    "The user is responsible for the return. Not affiliated with or endorsed by the IRS.",
  ];
}

/** A result as JSON, `{ notices, values }`. A batch states the notices once at its top level, so its cases omit them. */
export function resultToJson(result: EvalResult, withNotices = true): string {
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
  return JSON.stringify(withNotices ? { notices: standingNotices(), values } : { values }, null, 2);
}

export function renderValuesHtml(data: CanonicalData, result: EvalResult, targetDocs: string[]): string {
  const escaped = renderValuesSheet(data, result, targetDocs).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
  return `<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${YEAR} values sheet</title><body><pre style="white-space:pre-wrap">${escaped}</pre></body></html>`;
}
