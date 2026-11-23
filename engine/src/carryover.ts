// The cross-year carryover map (carryover/<year>.yaml): which of a year's lines the next year's return takes as an
// answer. Each entry names a line of the year (`from`), the input of the next year's return that holds it (`to`, an
// input of this year's definitions too: ids survive renumbering, and a prior-year input asks for the previous year's
// figure) and how the figure becomes the answer (`how`). The build checks every entry against the year's definitions.

import type { CanonicalData, FormDoc, Line } from "./types.js";

export interface CarryoverEntry { from: string; to: string; how: "copy" | "negate" | "nonzero"; note?: string }
export interface CarryoverMap { tax_year: number; carryovers: CarryoverEntry[] }

const MONEY = new Set(["Dollars", "NonNegDollars"]);

/** Whether `how` turns a value of type `from` into an answer of type `to`: `copy` keeps it (same type, or a
 * non-negative amount into a signed one), `negate` enters a signed loss as a positive amount, `nonzero` answers a
 * Bool question with whether the amount is other than zero. */
function fits(how: string, from: string, to: string): boolean {
  if (how === "copy") return from === to || (from === "NonNegDollars" && to === "Dollars");
  if (how === "negate") return from === "Dollars" && to === "NonNegDollars";
  if (how === "nonzero") return MONEY.has(from) && to === "Bool";
  return false;
}

/** The collections enclosing a document, itself first when it is one. */
function collections(doc: FormDoc, byId: Map<string, FormDoc>): string[] {
  const out: string[] = [];
  for (let d: FormDoc | undefined = doc; d?.collection; d = d.collection.parent ? byId.get(d.collection.parent) : undefined) out.push(d.id);
  return out;
}

/** The problems of a carryover map against a year's definitions: the year it states, and per entry a `from` that is
 * no line, a `to` that is no input, a `how` that does not turn the one type into the other, a `to` in a collection
 * that does not enclose `from` (a figure of one entry is the answer of the same entry next year, or of an entry
 * enclosing it; a return-wide figure is a return-wide answer), and an entry given twice. */
export function carryoverProblems(data: CanonicalData, map: CarryoverMap, year: number, where: string): string[] {
  const problems: string[] = [];
  if (map?.tax_year !== year) problems.push(`${where}: tax_year ${map?.tax_year}, but the build is for ${year}`);
  if (!Array.isArray(map?.carryovers)) return [...problems, `${where}: no carryovers list`];
  const byId = new Map(data.forms.map((d) => [d.id, d]));
  const lineOf = new Map<string, { doc: FormDoc; line: Line }>();
  for (const doc of data.forms) for (const line of doc.lines) lineOf.set(line.id, { doc, line });
  const seen = new Set<string>();
  for (const [i, e] of map.carryovers.entries()) {
    const at = `${where}: carryover ${i + 1} (${e?.from} to ${e?.to})`;
    const from = lineOf.get(e?.from), to = lineOf.get(e?.to);
    if (!from) problems.push(`${at}: from names no line`);
    if (!to) problems.push(`${at}: to names no line`);
    else if (to.line.expr.op !== "input") problems.push(`${at}: to is not an input`);
    if (!["copy", "negate", "nonzero"].includes(e?.how)) problems.push(`${at}: how must be copy, negate or nonzero`);
    else if (from && to && !fits(e.how, from.line.type, to.line.type)) problems.push(`${at}: ${e.how} does not turn a ${from.line.type} into a ${to.line.type} answer`);
    if (from && to) {
      const outer = collections(to.doc, byId);
      const inner = collections(from.doc, byId);
      if (outer.length > 0 && !inner.includes(outer[0]!)) problems.push(`${at}: to is in collection ${outer[0]}, which does not enclose ${from.doc.id}`);
      if (outer.length === 0 && inner.length > 0) problems.push(`${at}: from is a line of each entry of ${inner[0]}, and to is one answer for the return`);
    }
    const key = `${e?.from} ${e?.to}`;
    if (seen.has(key)) problems.push(`${at}: given twice`);
    seen.add(key);
  }
  return problems;
}
