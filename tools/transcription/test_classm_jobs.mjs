// Regression for a random corpus losing Form 2441's active benefits regime.
// Existing regression facts may seed independent hand-work; their expected
// values are never supplied to the model.
import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const temp = mkdtempSync(join(tmpdir(), 'classm-seeds-'));
try {
  const out = join(temp, 'jobs.json');
  const proc = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs',
    '--docs', 'f2441', '--corpus', '1', '--include-fixtures', '--out', out],
  { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  assert.equal(proc.status, 0, proc.stderr);
  const jobs = JSON.parse(readFileSync(out, 'utf8')).jobs;
  assert.ok(jobs.length > 0, 'fixture seeds must supply an active Form 2441 case');
  assert.ok(jobs.every(j => j.inputs['f2441.care'] || j.inputs['f2441.benefits']), 'unfiled forms earn no job');
  assert.ok(jobs.some(j => j.inputs['f2441.benefits'] && j.project['f2441.line15']?.cents > 0),
    'the benefits arithmetic must be exercised with a positive amount');
  assert.ok(jobs.some(j => j.inputs['f2441.line13'] > 0 && j.inputs['f2441.line14'] > 0),
    'carry-in and forfeiture must be exercised together');
  console.log(`classm seeds: ${jobs.length} active jobs; positive benefits and carry/forfeiture covered`);
} finally {
  rmSync(temp, { recursive: true, force: true });
}
