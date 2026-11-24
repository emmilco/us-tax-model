// `mutate-arguments [--ny]`: the keyed equivalence arguments of mutate.ts (EQUIVALENT_IF, ANSWERED_ONLY) checked on the
// canonical build without a mutation run (argumentProblems): an argument fails when no mutant has its id, when its
// mutant reads another line than the argument names, or when it no longer holds (a premise it pins changed).
// An argument listed in tools/mutation_arguments_open.json (`{"open": {argument id: bug id}}`, the open bug that
// covers it) is printed as known and does not fail the run; the run fails on a problem of an unlisted argument and
// on a listed argument of this jurisdiction that has no problem (remove it: the list only shrinks). Whether a mutant
// is killed is the mutation run's question (`mutate`, full tier).
// `mutate-arguments --self-test` checks the comparison with the list on planted problems.
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { argumentProblems } from "./mutate.js";
import { NY_MODE } from "./year.js";

const ROOT = resolve(import.meta.dirname, "../..");

export const OPEN_LIST = join(ROOT, "tools", "mutation_arguments_open.json");

type OpenList = { open: Record<string, string> };

const nyId = (id: string): boolean => /\bny[_.]/.test(id);
const idOf = (problem: string): string => problem.slice(0, problem.indexOf(": ") < 0 ? problem.length : problem.indexOf(": "));

// The problems split by the list: those of unlisted arguments (failing), those of listed ones (known), and the listed
// arguments of this jurisdiction with no problem (stale, failing).
export function compareWithList(problems: string[], listed: string[], ny: boolean): { failing: string[]; known: string[]; stale: string[] } {
  const mine = new Set(listed.filter((id) => nyId(id) === ny));
  const failing = problems.filter((p) => !mine.has(idOf(p)));
  const known = problems.filter((p) => mine.has(idOf(p)));
  const withProblem = new Set(problems.map(idOf));
  const stale = [...mine].filter((id) => !withProblem.has(id)).sort();
  return { failing, known, stale };
}

function selfTest(): number {
  const problems = ["operand.a.a.x.y: the mutant survives but the argument no longer holds", "operand.b.b.x.y: no mutant has this id any more"];
  const checks: [string, boolean][] = [];
  let r = compareWithList(problems, ["operand.a.a.x.y"], false);
  checks.push(["an unlisted argument fails", r.failing.length === 1 && r.failing[0]!.startsWith("operand.b.")]);
  checks.push(["a listed argument is known", r.known.length === 1 && r.known[0]!.startsWith("operand.a.")]);
  r = compareWithList(problems, ["operand.a.a.x.y", "operand.b.b.x.y", "operand.c.c.x.y"], false);
  checks.push(["a listed argument with no problem is stale", r.failing.length === 0 && r.stale.join() === "operand.c.c.x.y"]);
  r = compareWithList(problems, ["operand.a.a.x.y", "operand.b.b.x.y", "operand.ny_it201.ny_it201.x.y"], false);
  checks.push(["the other jurisdiction's listed argument is not stale", r.stale.length === 0]);
  r = compareWithList([], ["operand.ny_it201.ny_it201.x.y"], true);
  checks.push(["a New York listed argument is stale in the New York run", r.stale.length === 1]);
  const bad = checks.filter(([, ok]) => !ok).map(([what]) => what);
  for (const what of bad) console.error(`mutate-arguments self-test: ${what}: wrong`);
  console.log(`mutate-arguments self-test: ${bad.length === 0 ? "ok" : "FAILED"} (${checks.length} checks)`);
  return bad.length === 0 ? 0 : 1;
}

export function mutationArguments(args: string[]): number {
  if (args.includes("--self-test")) return selfTest();
  const list = JSON.parse(readFileSync(OPEN_LIST, "utf8")) as OpenList;
  const open = list.open ?? {};
  const { failing, known, stale } = compareWithList(argumentProblems(loadCanonical()), Object.keys(open), NY_MODE);
  const who = NY_MODE ? "New York" : "federal";
  for (const p of known) console.log(`  known (${open[idOf(p)]}): ${p}`);
  for (const p of failing) console.error(`  ${p}`);
  for (const id of stale) console.error(`  ${id}: listed in tools/mutation_arguments_open.json but has no problem; remove it from the list`);
  if (failing.length || stale.length) {
    console.error(`mutate-arguments (${who}): ${failing.length} argument(s) fail, ${stale.length} listed argument(s) stale; ${known.length} known`);
    return 1;
  }
  console.log(`mutate-arguments (${who}): every keyed argument holds but the ${known.length} listed as covered by an open bug`);
  return 0;
}
