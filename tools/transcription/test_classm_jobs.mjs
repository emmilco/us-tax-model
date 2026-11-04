// Regression for a random corpus losing Form 2441's active benefits regime.
// Existing regression facts may seed independent hand-work; their expected
// values are never supplied to the model.
import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
// The year of the run (--year N, removed from process.argv on import) is passed to every engine command.
import { YEAR_ARGS } from '../../engine/dist/year.js';

const temp = mkdtempSync(join(tmpdir(), 'classm-seeds-'));
try {
  const out = join(temp, 'jobs.json');
  const proc = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs', ...YEAR_ARGS,
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
  // A single document is worked on its printed lines only, and a case holds only the answers the
  // interview asks: the saver's credit dependent question is asked only if someone can claim you.
  assert.ok(jobs.every(j => j.worked_scope === 'printed-irs-lines'), 'single documents request printed IRS lines only');
  assert.ok(jobs.every(j => j.inputs['sa.dependent'] === true || !('person[taxpayer].sav_claimed' in j.inputs)),
    'a case must not hold an answer the interview never asks');
  const hsaOut = join(temp, 'hsa-jobs.json');
  const hsa = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs', ...YEAR_ARGS,
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
  // Lines hidden by shown_when show no amount: the 28% Rate Gain Worksheet on a return that never
  // reaches it has nothing to fill, so no job compares its hidden lines.
  const g28Out = join(temp, 'g28-jobs.json');
  const g28 = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs', ...YEAR_ARGS,
    '--docs', 'g28', '--corpus', '300', '--include-fixtures', '--out', g28Out],
  { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  assert.equal(g28.status, 0, g28.stderr);
  const g28Jobs = JSON.parse(readFileSync(g28Out, 'utf8')).jobs;
  assert.ok(g28Jobs.length > 0, 'a reached 28% Rate Gain Worksheet must still be worked');
  assert.ok(g28Jobs.every(job => !job.branches.includes('g28.reached:false')), 'hidden worksheet lines must not be filled or written into class M expectations');
  console.log(`classm shown_when: ${g28Jobs.length} g28 jobs, none on an unreached worksheet`);
  // A Form 1095-A is answered either as uniform (one monthly column A and B and the line 33 column C
  // total) or month by month; the generator fills both so every line computes, but the worker sees
  // only the route the entry takes, and the other route's totals are not requested.
  const f1095aOut = join(temp, 'f1095a-jobs.json');
  const f1095a = spawnSync(process.execPath, ['engine/dist/main.js', 'classm-jobs', ...YEAR_ARGS,
    '--docs', 'f1095a', '--corpus', '300', '--include-fixtures', '--out', f1095aOut],
  { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  assert.equal(f1095a.status, 0, f1095a.stderr);
  const f1095aJobs = JSON.parse(readFileSync(f1095aOut, 'utf8')).jobs;
  assert.ok(f1095aJobs.length > 0, 'a Form 1095-A must still be worked');
  let entries = 0;
  for (const job of f1095aJobs) for (const [entry, fields] of Object.entries(job.entries)) {
    const uniform = fields.find(f => f.field === 'f1095a.uniform')?.value.value;
    const shown = new Set(fields.map(f => f.field.slice('f1095a.'.length)));
    const filled = job.fill.filter(l => l.entry === entry).map(l => l.id.slice(entry.length + 1));
    const other = uniform ? ['in_a_jan', 'in_b_jan', 'in_c_jan'] : ['mo_a', 'mo_b', 'c_total'];
    assert.ok(other.every(k => !shown.has(k)), `${job.id} ${entry}: the other route's answers are shown`);
    assert.ok(filled.every(k => !k.startsWith('yr_') || k.endsWith(uniform ? '_uniform' : '_monthly')), `${job.id} ${entry}: the other route's total is requested`);
    entries++;
  }
  assert.ok(entries > 0);
  console.log(`classm route: ${f1095aJobs.length} f1095a job(s), ${entries} entries shown only their own route`);
} finally {
  rmSync(temp, { recursive: true, force: true });
}
