// The Tax Table midpoint conjecture, tested against every cell:
// for each band and each filing-status column, tax = round-half-up to whole
// dollars of the rate-schedule tax at the band's midpoint. The result is
// recorded in reports/2025/tax_table_conjecture.md either way.

import { mkdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { exactBracketCents } from "./eval.js";

const ROOT = resolve(import.meta.dirname, "../..");

export function runConjecture(): void {
  const data = loadCanonical();
  const table = data.tables.find((t) => t.id === "tax_table");
  const schedule = data.tables.find((t) => t.id === "rate_schedule");
  if (!table || table.kind !== "tax_table" || !schedule || schedule.kind !== "bracket_schedule") {
    console.error("conjecture: tax_table or rate_schedule missing; run `main.js build` first");
    process.exit(1);
  }
  const alias = schedule.status_alias ?? {};
  const rows = table.bands!;
  const cols = table.columns!;

  interface Mismatch {
    col: string;
    at: number;
    less: number;
    table: number;
    expected: number;
  }
  const mismatches: Mismatch[] = [];
  let cells = 0;

  for (const band of rows) {
    const mid = Math.floor((band.at_least + band.less_than) / 2); // integer cents; band midpoints are whole cents
    for (let ci = 0; ci < cols.length; ci++) {
      const col = cols[ci]!;
      const status = alias[col.statuses[0]!] ?? col.statuses[0]!;
      const sched = schedule.schedules![status];
      if (!sched) {
        console.error(`conjecture: no schedule for status ${status}`);
        process.exit(1);
      }
      const exact = exactBracketCents(sched, mid)!; // {n: cents*den, d: den}
      const n = exact.n;
      const d = exact.d;
      // exact cents = n/d. Whole dollars = n/(100 d). Round half-up:
      const roundedDollars = (n + 50n * d) / (100n * d);
      const expected = Number(roundedDollars) * 100;
      cells++;
      if (expected !== band.tax[ci]) {
        mismatches.push({ col: col.key, at: band.at_least, less: band.less_than, table: band.tax[ci]!, expected });
      }
    }
  }

  const report: string[] = [];
  report.push("# Tax Table midpoint conjecture — result for 2025");
  report.push("");
  report.push("Method: for every band of `tax_table` and every filing-status column, compute the");
  report.push("exact rate-schedule tax (`rate_schedule`, Rev. Proc. 2024-40 section 3.01, with");
  report.push("qualifying surviving spouses aliased to the joint schedule) at the band's midpoint");
  report.push("(at_least + less_than) / 2, then round to whole dollars half-up. Compare with the");
  report.push("printed cell. This is the conjecture from `spec/spec.md` section 6.3, tested, not");
  report.push("assumed.");
  report.push("");
  report.push(`- Cells tested: ${cells} (${rows.length} bands x ${cols.length} columns)`);
  report.push(`- Matching cells: ${cells - mismatches.length}`);
  report.push(`- Mismatching cells: ${mismatches.length}`);
  report.push("");
  if (mismatches.length === 0) {
    report.push("Result: the conjecture holds for every cell under the half-up whole-dollar rounding");
    report.push("rule. The rule is recorded for the test harness: `round_half_up_to_whole_dollars");
    report.push("(schedule_at(midpoint))`.");
  } else {
    report.push("Mismatching cells (band, column, printed value, expected value):");
    report.push("");
    for (const m of mismatches.slice(0, 200)) {
      report.push(
        `- ${m.col} ${m.at / 100}-${m.less / 100}: printed ${m.table / 100}, conjecture ${m.expected / 100}`,
      );
    }
    if (mismatches.length > 200) report.push(`- … and ${mismatches.length - 200} more`);
  }
  report.push("");

  const outDir = join(ROOT, "reports", "2025");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "tax_table_conjecture.md"), report.join("\n"));
  console.log(`conjecture: ${cells} cells tested, ${mismatches.length} mismatches`);
  console.log(`report: reports/2025/tax_table_conjecture.md`);
}

// The EIC Table against Rev. Proc. 2024-40 section 3.06(1): for each child
// count and status column, the credit at a band's midpoint m is the smaller of
// m x (maximum / earned income amount) and the maximum, less
// (maximum / (completed phaseout - threshold phaseout)) x (m - threshold), not
// below zero, rounded half-up to whole dollars. The rates are those the Rev.
// Proc. amounts imply (the statutory percentages are not in the archive), so a
// cell may differ by $1 where the implied rate is rounded; a larger difference
// means a misread row or column. The result is recorded either way.
export function runEicConjecture(): void {
  const data = loadCanonical();
  const p = (k: string): bigint => {
    const v = data.params.values[k]?.value;
    if (typeof v !== "number") { console.error(`conjecture: parameter ${k} missing`); process.exit(1); }
    return BigInt(v);
  };
  let cells = 0, exact = 0, off1 = 0, kink = 0;
  const worse: string[] = [];
  for (let k = 0; k < 4; k++) {
    const table = data.tables.find((t) => t.id === `eic_${k}`);
    if (!table || table.kind !== "tax_table") { console.error(`conjecture: eic_${k} missing`); process.exit(1); }
    const eia = p(`eic.earned_amount${k}`), max = p(`eic.maximum${k}`);
    table.columns!.forEach((col, ci) => {
      const side = col.key === "joint" ? "joint" : "other";
      const thr = p(`eic.ws_threshold${k === 0 ? 0 : 1}.${side}`), end = p(`eic.limit${k}.${side}`);
      const bands = table.bands!;
      for (let bi = 0; bi < bands.length; bi++) {
        const band = bands[bi]!;
        // A row split for a footnote in one column keeps the whole row's printed value in the
        // other column, figured at the whole row's midpoint.
        const prev = bands[bi - 1], next = bands[bi + 1];
        const sibling = band.less_than % 5000 !== 0 ? next : band.at_least % 5000 !== 0 && band.at_least !== 100 ? prev : undefined;
        const rowValue = sibling !== undefined && sibling.tax[ci] === band.tax[ci];
        const lo = rowValue ? Math.min(band.at_least, sibling!.at_least) : band.at_least;
        const hi = rowValue ? Math.max(band.less_than, sibling!.less_than) : band.less_than;
        const m2 = BigInt(lo + hi); // twice the midpoint, in cents
        // The band that contains the earned income amount prints the maximum credit.
        if (BigInt(band.at_least) < eia && eia < BigInt(band.less_than)) {
          cells++; kink++;
          if (band.tax[ci] === Number(max)) exact++;
          else worse.push(`- ${k} children, ${col.key}, ${band.at_least / 100}-${band.less_than / 100}: printed ${band.tax[ci]! / 100}, maximum ${Number(max) / 100}`);
          continue;
        }
        // Work in units of cents / (2 * eia * (end - thr)) so every term is an integer.
        const span = end - thr;
        const den = 2n * eia * span;
        let build = m2 * max * span; // m * max/eia, scaled by den
        const cap = max * den;
        if (build > cap) build = cap;
        const over = m2 - 2n * thr; // 2 (m - thr)
        const phase = over > 0n ? over * max * eia : 0n; // (m - thr) * max/span, scaled by den
        let credit = build - phase;
        if (credit < 0n) credit = 0n;
        const dollars = (credit + 50n * den) / (100n * den);
        const expected = Number(dollars) * 100;
        const printed = band.tax[ci]!;
        cells++;
        if (expected === printed) exact++;
        else if (Math.abs(expected - printed) === 100) off1++;
        else worse.push(`- ${k} children, ${col.key}, ${band.at_least / 100}-${band.less_than / 100}: printed ${printed / 100}, formula ${expected / 100}`);
      }
    });
  }
  const report = [
    "# EIC Table against Rev. Proc. 2024-40 — result for 2025",
    "",
    "Method: for every band of `eic_0` to `eic_3` (extracted from i1040gi pp. 49-60 by `tools/extract_eic_table.py`)",
    "and both status columns, the credit at the band's midpoint is the smaller of the midpoint times (maximum",
    "credit / earned income amount) and the maximum credit, less (maximum credit / (completed phaseout amount -",
    "threshold phaseout amount)) times the excess of the midpoint over the threshold phaseout amount, not below",
    "zero, rounded half-up to whole dollars. The four amounts per child count and status are the year parameters",
    "`eic.earned_amount*`, `eic.maximum*` (Rev. Proc. 2024-40 section 3.06(1)) and `eic.ws_threshold*`, `eic.limit*`",
    "(the instructions' Worksheet A line 5 and Step 1 amounts, which equal the Rev. Proc.'s threshold and completed",
    "phaseout amounts). The rates are those the Rev. Proc. amounts imply; the statutory percentages are not archived,",
    "so a difference of $1 is expected where an implied rate is rounded. A larger difference would mean a misread",
    "row or column. Two readings of the printed table are part of the method: a row split for a footnote in one",
    "column keeps the whole row's value, figured at the whole row's midpoint, in the other column; and the band",
    "that contains the earned income amount prints the maximum credit (checked as equality with the maximum).",
    "",
    `- Cells tested: ${cells} (of which ${kink} in a band containing the earned income amount)`,
    `- Equal to the formula: ${exact}`,
    `- Differing by $1: ${off1}`,
    `- Differing by more than $1: ${worse.length}`,
    "",
    ...(worse.length ? ["Cells differing by more than $1:", "", ...worse.slice(0, 200), ""] : ["No cell differs by more than $1.", ""]),
  ];
  writeFileSync(join(ROOT, "reports", "2025", "eic_table_conjecture.md"), report.join("\n"));
  console.log(`eic conjecture: ${cells} cells, ${exact} equal, ${off1} within $1, ${worse.length} worse`);
  console.log("report: reports/2025/eic_table_conjecture.md");
  if (worse.length) process.exitCode = 1;
}
