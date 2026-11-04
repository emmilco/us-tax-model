// Self-test of the check rules that have no failing case in the shipped data: each rule must
// flag a constructed violation and pass the corresponding clean case.
import assert from "node:assert/strict";
import { registerLinkProblems, tableBandMonoProblems } from "./check.js";
import type { CanonicalData, RegisterEntry, TableDoc } from "./types.js";

function table(bands: { at_least: number; less_than: number; tax: number[] }[]): TableDoc {
  return { id: "t", kind: "tax_table", title: "t", tax_year: 2025, cite: null as never, columns: [{ key: "a", statuses: [] }, { key: "b", statuses: [] }], bands };
}

function entry(id: string, extra: Partial<RegisterEntry> = {}): RegisterEntry {
  return { id, text_at_issue: "x", readings: ["x"], chosen: "x", reason: "x", cite: null as never, ...extra };
}

function data(entries: RegisterEntry[], links: string[]): CanonicalData {
  const lines = links.map((a, i) => ({ id: `f.l${i}`, printed: "1", label: "l", type: "Dollars", expr: { op: "input", source: "x" }, cite: null, ambiguity: a }));
  return { forms: [{ id: "f", kind: "form", tax_year: 2025, title: "f", lines }], defs: [], tables: [], params: { tax_year: 2025, enums: {}, values: {} }, register: { tax_year: 2025, entries } } as unknown as CanonicalData;
}

export function runCheckSelfTest(): void {
  // tableBand_mono's condition
  assert.deepEqual(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [0, 0] }, { at_least: 5, less_than: 9, tax: [1, 0] }, { at_least: 9, less_than: 12, tax: [1, 2] }])), []);
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [3, 0] }, { at_least: 5, less_than: 9, tax: [2, 1] }])).join("\n"), /column a falls to 2 at band 1/);
  // a fall below an earlier band that is not the adjacent one
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [3, 0] }, { at_least: 5, less_than: 9, tax: [4, 0] }, { at_least: 9, less_than: 12, tax: [3, 0] }])).join("\n"), /falls to 3 at band 2/);
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 6, tax: [0, 0] }, { at_least: 5, less_than: 9, tax: [0, 0] }])).join("\n"), /band 0 overlaps band 1/);
  assert.match(tableBandMonoProblems(table([{ at_least: 5, less_than: 5, tax: [0, 0] }])).join("\n"), /band 0 is empty or reversed/);

  // register links
  assert.deepEqual(registerLinkProblems(data([entry("amb.a"), entry("amb.b", { unlinked: "superseded by BUG-0000" })], ["amb.a"])), []);
  assert.match(registerLinkProblems(data([entry("amb.a"), entry("amb.b")], ["amb.a"])).join("\n"), /register amb\.b: no line links this entry/);
  assert.match(registerLinkProblems(data([entry("amb.b", { unlinked: "  " })], [])).join("\n"), /register amb\.b: no line links/);
  assert.match(registerLinkProblems(data([entry("amb.a", { unlinked: "superseded" })], ["amb.a"])).join("\n"), /carries an unlinked reason/);
  console.log("check self-test: 9 cases passed (tableBand_mono condition, register links)");
}
