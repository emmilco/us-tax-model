// The worker of the step cache's planted step (stepProbe in build-cache.ts): reads the file it is given and posts its
// text. It loads build-cache.ts first, as every worker of a traced step does.
import "./build-cache.js";
import { readFileSync } from "node:fs";
import { parentPort, workerData } from "node:worker_threads";

parentPort!.postMessage(readFileSync(workerData as string, "utf8"));
