// A mutation worker: evaluates its share of the mutants (see mutantShare in mutate.ts).
// The tax year comes from the main thread, put on the command line before year.ts loads.
import { parentPort, workerData } from "node:worker_threads";

const { year, index, count, ny } = workerData as { year: number; index: number; count: number; ny?: boolean };
process.argv.push("--year", String(year));
if (ny) process.argv.push("--ny");
const { mutantShare } = await import("./mutate.js");
parentPort!.postMessage(mutantShare(index, count));
