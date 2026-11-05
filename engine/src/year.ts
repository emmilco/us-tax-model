// The tax year a command works on: `--year N` anywhere on the command line, or
// else the newest year listed as adopted in years.json. The flag is removed from
// process.argv when this module loads, so command parsers never see it; a child
// process started by a command gets the year back through YEAR_ARGS.

import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "../..");

function fail(message: string): never {
  console.error(message);
  process.exit(2);
}

function resolveYear(): number {
  const argv = process.argv;
  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i]!;
    const value = arg === "--year" ? argv[i + 1] : arg.startsWith("--year=") ? arg.slice(7) : undefined;
    if (value === undefined) continue;
    argv.splice(i, arg === "--year" ? 2 : 1);
    if (!/^\d{4}$/.test(value)) fail(`--year: expected a four-digit year, got '${value}'`);
    const year = Number(value);
    if (!existsSync(join(ROOT, "forms", String(year)))) fail(`--year ${year}: no data for that year (forms/${year}/ does not exist)`);
    return year;
  }
  const adopted = (JSON.parse(readFileSync(join(ROOT, "years.json"), "utf8")) as { adopted: number[] }).adopted;
  if (adopted.length === 0) fail("years.json lists no adopted year; pass --year");
  return Math.max(...adopted);
}

export const YEAR = resolveYear();

// `--ny` (decision C6): the fixture commands (test-fixtures, coverage, evidence, compare, mutate) work on the New York
// fixtures (fixtures/ny/<YEAR>/) and write their reports to reports/ny/<YEAR>/. Without it they work on the federal
// fixtures exactly as before. Removed from process.argv here, like --year.
function resolveNy(): boolean {
  const i = process.argv.indexOf("--ny", 2);
  if (i < 0) return false;
  process.argv.splice(i, 1);
  return true;
}
export const NY_MODE = resolveNy();
export const YEAR_ARGS = ["--year", String(YEAR)];
// The reports directory of the fixture commands: reports/<YEAR>/, or reports/ny/<YEAR>/ with --ny.
export function reportPath(...rest: string[]): string {
  return NY_MODE ? join(ROOT, "reports", "ny", String(YEAR), ...rest) : join(ROOT, "reports", String(YEAR), ...rest);
}

// The same report as a command prints it: reports/<YEAR>/<name>, or reports/ny/<YEAR>/<name> with --ny.
export function reportName(name: string): string {
  return NY_MODE ? `reports/ny/${YEAR}/${name}` : `reports/${YEAR}/${name}`;
}

// A path under one of the per-year directories: yearPath("canonical") is canonical/<YEAR>.
export function yearPath(top: string, ...rest: string[]): string {
  return join(ROOT, top, String(YEAR), ...rest);
}

// New York (owner decision C1, docs/ny/DECISIONS.md): the New York data sits in a tree of its own beside
// the federal one, nyPath("forms") being forms/ny/<YEAR>/. Its documents (ids prefixed `ny_`) enter the
// same canonical build, so a New York line can read a federal line; the federal files are unchanged.
export function nyPath(top: string, ...rest: string[]): string {
  return join(ROOT, top, "ny", String(YEAR), ...rest);
}
