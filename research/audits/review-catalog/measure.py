"""Per-form prompt sizes from saved --dry-run previews: total, other-form catalog, collection catalog, screening list."""
import os, sys, json
d = sys.argv[1]
out = {}
for f in sorted(os.listdir(d)):
    if not f.endswith('.preview.prompt.txt'):
        continue
    s = open(os.path.join(d, f), encoding='utf-8').read()
    def between(a, b):
        i = s.find(a); j = s.find(b, i)
        return j - i if i >= 0 and j >= 0 else 0
    out[f.split('.')[0]] = {
        'total': len(s),
        'lines_catalog': between('Lines on other forms you may reference by id', '# Output'),
        'collections': between('Keyed collections (Form W-2s', 'The computed fields of the document under review'),
        'screening': between('Screening inputs (answered yes', 'Lines on other forms you may reference by id'),
        'excerpt': len(s) - s.find('# IRS text (archived snapshots'),
    }
json.dump(out, open(sys.argv[2], 'w'), indent=1)
for k, v in out.items():
    print(k, v)
