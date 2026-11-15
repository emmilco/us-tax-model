## landing-02 (fixed before landing; never assigned an id) — Church employee income question asks only about the filer, not the spouse

- **Date:** 2026-11-14.
- **Caught by:** the consumers check on the landing branch (tools/check_consumers.py): drafted as "differs" by an Opus reading agent of the landing lane, 2026-11-14, and confirmed by the landing agent against the question's prompt and help in interview/2025/questions.yaml.
- **Source:** i1040sse p. 1, Employees of Churches and Church Organizations.
- **Symptom:** scope.church_exempt_wages asks "pay you wages" while its parent scope.religious_work includes the spouse; a spouse's church employee income is not refused. Pair consumer:scope.church_exempt_wages@i1040sse:p1 left unruled.
- **Tags:** interview wording, scope, consumers
- **Fix:** on the landing branch, before review (lane land3-consumers, claude-opus-5-5): scope.church_exempt_wages asks about the filer or spouse. Pair ruled same.
- **Fix lines:** `scope.church_exempt_wages`
