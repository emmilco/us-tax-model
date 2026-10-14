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
