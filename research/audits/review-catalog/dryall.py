"""Run transcribe.py --dry-run for every form; copy previews to OUT/prompts; keep stdout per form."""
import os, sys, subprocess, shutil
R, OUT = sys.argv[1], sys.argv[2]
os.makedirs(os.path.join(OUT, 'prompts'), exist_ok=True)
forms = sorted(f[:-5] for f in os.listdir(os.path.join(R, 'forms/2025')) if f.endswith('.yaml'))
for f in forms:
    p = subprocess.run([sys.executable, 'tools/transcription/transcribe.py', '--form', f, '--dry-run'], cwd=R,
                       capture_output=True, text=True)
    open(os.path.join(OUT, f + '.out'), 'w').write(p.stdout + p.stderr)
    if p.returncode:
        print('FAIL', f, p.stderr[-500:])
    src = os.path.join(R, '.transcription', f + '.preview.prompt.txt')
    if os.path.exists(src) and 'no source-defined' not in p.stdout:
        shutil.copy(src, os.path.join(OUT, 'prompts', f + '.preview.prompt.txt'))
print('done', len(forms))
