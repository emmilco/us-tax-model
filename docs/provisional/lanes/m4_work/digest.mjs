// Lane m4 scratch: premiseDigest of a premise list. usage: node digest.mjs line1 line2 param:x ...
import { join, resolve } from "node:path";
const ROOT = resolve(import.meta.dirname, "../../../..");
const { loadCanonical } = await import(join(ROOT, "engine/dist/canonical.js"));
const { premiseDigest } = await import(join(ROOT, "engine/dist/mutate.js"));
console.log(premiseDigest(loadCanonical(), process.argv.slice(2)));
