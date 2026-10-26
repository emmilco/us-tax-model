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
  const hsaOut = join(temp, 'hsa-jobs.json');
  const hsa = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs',
    '--docs', 'f8889', '--corpus', '1', '--include-fixtures', '--out', hsaOut],
  { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  assert.equal(hsa.status, 0, hsa.stderr);
  const hsaJobs = JSON.parse(readFileSync(hsaOut, 'utf8')).jobs;
  assert.ok(hsaJobs.length > 0, 'HSA fixture seeds must provide worked cases');
  assert.ok(hsaJobs.every(job => job.worked_scope === 'printed-irs-lines'));
  assert.ok(hsaJobs.every(job => job.fill.every(line => /\.line\d+[a-z]?$/.test(line.id))), 'request printed HSA outputs without guessing internal helpers');
  assert.ok(hsaJobs.some(job => job.branches.some(branch => branch.startsWith('f8889.') && !branch.startsWith('f8889.line'))), 'helper branches still participate in case coverage');
  assert.ok(hsaJobs.some(job => Object.entries(job.inputs).some(([key, value]) => key.endsWith('.line14a') && value > 0)), 'positive distributions must be worked, not only incidental zeroes');
  assert.ok(hsaJobs.every(job => job.given.every(value => !['household.hsa_share_sum', 'household.hsa_step1_sum', 'household.hsa_split_count'].includes(value.ref))), 'validation-only calculations must not feed the reviewed computation back as authoritative givens');
  console.log(`classm HSA: ${hsaJobs.length} printed-output jobs retain helper-branch selection`);
} finally {
  rmSync(temp, { recursive: true, force: true });
}
