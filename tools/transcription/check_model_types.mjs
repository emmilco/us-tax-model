// Type-only validation. This command never evaluates a candidate.
import { readFileSync } from 'node:fs';
import { prepareCandidate } from './model_candidate.mjs';
const { context, form, lines } = JSON.parse(readFileSync(0, 'utf8'));
const { errors } = prepareCandidate(context, form, lines);
process.stdout.write(JSON.stringify({ policy: 'project-expression-types-v1', errors }));
