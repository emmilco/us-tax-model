// A mutation worker: evaluates its share of the mutants (see mutantShare in mutate.ts), or, given a plan, its share
// of the sampled check of the keyed arguments (sampledShare).
// The tax year comes from the main thread, put on the command line before year.ts loads.
// First: a traced step records this worker's reads too (build-cache.ts).
import "./build-cache.js";
import { parentPort, workerData } from "node:worker_threads";

const { year, index, count, ny, plan } = workerData as { year: number; index: number; count: number; ny?: boolean; plan?: unknown };
process.argv.push("--year", String(year));
if (ny) process.argv.push("--ny");
const { mutantShare, sampledShare } = await import("./mutate.js");
parentPort!.postMessage(plan === undefined ? mutantShare(index, count) : sampledShare(index, count, plan as Parameters<typeof sampledShare>[2]));
