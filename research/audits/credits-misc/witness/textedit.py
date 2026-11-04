"""Text-level edit inside one fixture case: textedit.py <file> <case id> <old> <new> [<old> <new> ...]

The case's region runs from its "id" line to the next case's "id" line; each old string must occur
exactly once in that region. The rest of the file is untouched (some fixture files do not round-trip
json.dumps).
"""
import re
import sys

path, case_id = sys.argv[1:3]
pairs = sys.argv[3:]
text = open(path).read()
start = text.index(f'"id": "{case_id}"')
m = re.compile(r'"id": "').search(text, start + 1)
end = m.start() if m else len(text)
region = text[start:end]
for old, new in zip(pairs[::2], pairs[1::2]):
    assert region.count(old) == 1, (case_id, old, region.count(old))
    region = region.replace(old, new)
open(path, "w").write(text[:start] + region + text[end:])
