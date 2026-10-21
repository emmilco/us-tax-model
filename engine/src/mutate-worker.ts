// A mutation worker: evaluates its share of the mutants (see mutantShare in mutate.ts).
// The tax year comes from the main thread, put on the command line before year.ts loads.
import { parentPort, workerData } from "node:worker_threads";

const { year, index, count } = workerData as { year: number; index: number; count: number };
process.argv.push("--year", String(year));
const { mutantShare } = await import("./mutate.js");
parentPort!.postMessage(mutantShare(index, count));
