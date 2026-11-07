// Self-test of the check rules that have no failing case in the shipped data: each rule must
// flag a constructed violation and pass the corresponding clean case.
import assert from "node:assert/strict";
import { registerLinkProblems, tableBandMonoProblems } from "./check.js";
import { entrySyntax } from "./interview.js";
import { gateProblems } from "./gates.js";
import { evaluate } from "./eval.js";
import type { CanonicalData, Line, RegisterEntry, TableDoc } from "./types.js";
import { flatText, indentRest, parseStructured, textSummary } from "./text.js";

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


/** A document `g` with one gate: `g.box` takes `g.box_amount` when `g.any` is true and `g.zero` (parameter z, 0) when it
 * is false; `g.total` reads the gate line. `edit` changes the lines before the data is made. */
function gated(edit: (lines: Line[]) => void = () => {}): CanonicalData {
  const eq = (v: boolean) => ({ op: "test", eq: ["g.any", { const: v }] });
  const lines = [
    { id: "g.any", printed: "1", label: "any", type: "Bool", expr: { op: "input", source: "Any?" }, cite: null },
    { id: "g.box_amount", printed: "2", label: "amount", type: "NonNegDollars", expr: { op: "input", source: "Amount?" }, cite: null, gated_by: "g.box" },
    { id: "g.box", printed: "2", label: "box", type: "NonNegDollars", expr: { op: "choose", alternatives: [{ guard: eq(true), then: "g.box_amount" }, { guard: eq(false), then: "g.zero" }] }, cite: null },
    { id: "g.zero", printed: "zero", label: "zero", type: "NonNegDollars", expr: { op: "param", ref: "z" }, cite: null },
    { id: "g.total", printed: "3", label: "total", type: "NonNegDollars", expr: { op: "sum", of: ["g.box"] }, cite: null },
  ] as unknown as Line[];
  edit(lines);
  return { forms: [{ id: "g", kind: "form", tax_year: 2025, title: "g", lines }], defs: [], tables: [],
    params: { tax_year: 2025, enums: {}, values: { z: { type: "NonNegDollars", value: 0, cite: null } } }, register: { tax_year: 2025, entries: [] } } as unknown as CanonicalData;
}
const line = (lines: Line[], id: string) => lines.find((l) => l.id === id)!;

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

  // Entry syntax in question wording: the forms the question bank used, and substance it must not flag.
  const syntax = [
    "Money is integer cents.", "In cents; zero if none.", "Answer true or false.", "Answer true/false for questions; a count is a whole number.",
    "Unknown may be null; do not guess.", "Enter a JSON array of distinct keys.", "Empty [] means none.",
    'Enter ["taxpayer"], or ["taxpayer","spouse"] if you are married filing jointly.', "List stable keys for taxable interest payers.",
    "Answer taxpayer for the entry keyed taxpayer and spouse for the entry keyed spouse.", "Integer cents.", "A whole number.",
  ];
  for (const s of syntax) assert.ok(entrySyntax(s), `entry syntax not flagged: ${s}`);
  const substance = [
    "Zero if none.", "Answer No if you have none.", "Yes refuses the return.", "Enter 0 if none; Yonkers tax is outside this tool.",
    "The percentage of this property's use that is for this business, from 1 to 100.", "List the employers that gave you a Form W-2, one entry per employer.",
    "Line 7 of your 2024 Schedule D; a loss (printed in parentheses) is entered as a negative amount.", "Box 12 holds up to four amounts, each with a code of one or two letters.",
  ];
  for (const s of substance) assert.equal(entrySyntax(s), null, `substance flagged as entry syntax: ${s}`);

  // Gate conventions (gates.ts): the clean gate, then one violation each.
  assert.deepEqual(gateProblems(gated()), []);
  const gateCases: [string, (lines: Line[]) => void, RegExp, string[]?][] = [
    ["a second reader", (ls) => { (line(ls, "g.total").expr as { of: string[] }).of.push("g.box_amount"); }, /read by g\.total; a gated input is read only by its gate line/],
    ["a refusal gate reading it", (ls) => { line(ls, "g.total").refuses = [{ when: "g.box_amount", form: "x", remedy: "x", cite: null as never }]; }, /read by g\.total/],
    ["an interview target", () => {}, /an interview target/, ["g.box_amount"]],
    ["no else", (ls) => { (line(ls, "g.box").expr as { alternatives: { then: string }[] }).alternatives[1]!.then = "g.box_amount"; }, /no else alternative/],
    ["an else that is not zero", (ls) => { (line(ls, "g.box").expr as { alternatives: { then: string }[] }).alternatives[1]!.then = "g.total"; }, /no else alternative/],
    ["a guard reading the input", (ls) => { ((line(ls, "g.box").expr as { alternatives: { guard: { eq: unknown[] } }[] }).alternatives[0]!.guard.eq)[0] = "g.box_amount"; }, /a guard of the gate reads the gated input/],
    ["a gate that is not a choose", (ls) => { line(ls, "g.box").expr = { op: "sum", of: ["g.box_amount"] }; }, /not a choose/],
    ["a missing gate line", (ls) => { line(ls, "g.box_amount").gated_by = "g.nowhere"; }, /no line g\.nowhere/],
    ["a marker on a computed line", (ls) => { line(ls, "g.total").gated_by = "g.box"; }, /only an input line can be gated/],
    ["two inputs on one gate", (ls) => { ls.push({ ...line(ls, "g.box_amount"), id: "g.other" }); }, /gates g\.box_amount, g\.other; a gate line gates one input/],
  ];
  for (const [name, edit, re, targets] of gateCases) assert.match(gateProblems(gated(edit), targets).join("\n"), re, `gate check missed: ${name}`);
  // The convention hides the gated input: unanswered gate, only the gate is asked; no, nothing; yes, the amount.
  const asked = (inputs: Record<string, unknown>) => [...new Set([...evaluate(gated(), inputs as never, ["g.total"]).derivations.values()]
    .flatMap((d) => d.value.kind === "unknown" && d.value.input ? [d.value.input] : []))];
  assert.deepEqual(asked({}), ["g.any"]);
  assert.deepEqual(asked({ "g.any": false }), []);
  assert.deepEqual(asked({ "g.any": true }), ["g.box_amount"]);

  // Structured text (text.ts): the subset parses to its blocks; everything else is a named problem; plain text is untouched.
  const good = "Any of these?\n\nWork:\n- wages (Form W-2)\n- tips, for example:\n  - cash tips\n\nA closing note, with a colon:\n\n- a list after a blank line";
  const parsed = parseStructured(good);
  assert.deepEqual(parsed.problems, []);
  assert.deepEqual(parsed.blocks, [{ kind: "paragraph", text: "Any of these?" },
    { kind: "list", heading: "Work:", items: [{ text: "wages (Form W-2)", items: [] }, { text: "tips, for example:", items: ["cash tips"] }] },
    { kind: "paragraph", text: "A closing note, with a colon:" }, { kind: "list", heading: null, items: [{ text: "a list after a blank line", items: [] }] }]);
  const plain = "  a plain *label*  with  `anything`, - kept as it is ";
  assert.deepEqual(parseStructured(plain).problems, []);
  assert.equal(indentRest(plain, "    "), plain);
  assert.equal(textSummary(plain), plain);
  assert.equal(flatText(plain), plain);
  assert.equal(indentRest(good, "  ").split("\n")[5], "    - cash tips");
  assert.equal(textSummary(good), "Any of these?");
  assert.equal(flatText("Q?\n\nH:\n- a\n  - b"), "Q? H: - a - b");
  const bad: [string, RegExp][] = [
    ["- a bullet first\n\nx", /first line must be the question/],
    ["Q?\nHeading:\n- a", /must follow a blank line/],
    ["Q?\n\nNo colon\n- a", /must end with ":"/],
    [`Q?\n\n${"h".repeat(81)}:\n- a`, /at most 80 characters/],
    ["Q?\n\n  - nested first", /nested bullet must follow a bullet/],
    ["Q?\n\n- a\nafter the list", /must follow a blank line/],
    ["Q?\n\n\nx", /two blank lines/],
    ["Q?\n\nx\n", /only allowed between blocks/],
    ["Q?\n\n### Heading", /block syntax/],
    ["Q?\n\n* star", /block syntax/],
    ["Q?\n\n1. one", /block syntax/],
    ["Q?\n\n- **bold**", /inline Markdown/],
    ["Q?\n\n- a _stressed_ word", /inline Markdown/],
    ["Q?\n\n- [a](b)", /inline Markdown/],
    ["Q?\n\n    - too deep", /indented line/],
    ["Q?\n\nx ", /trailing spaces/],
    ["Q?\n\n\tx", /tab/],
  ];
  for (const [text, re] of bad) assert.match(parseStructured(text).problems.join("\n"), re, `not flagged: ${JSON.stringify(text)}`);
  assert.deepEqual(parseStructured("Q?\n\n- employer_reported, an enum value").problems, []);
  console.log(`check self-test: ${9 + syntax.length + substance.length + 1 + gateCases.length + 3 + 10 + bad.length} cases passed (tableBand_mono condition, register links, entry syntax in question wording, gate conventions, structured text)`);
}
