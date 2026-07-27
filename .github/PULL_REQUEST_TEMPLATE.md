## What this changes

Describe the change in one or two sentences.

## Checklist

- [ ] No em dashes or en dashes anywhere in the change. Plain hyphens, commas, or separate
      sentences only. British spelling.
- [ ] Any new or changed rating traces to a primary document. New clauses are saved under
      docs/primary-sources/<entity-id>/ and logged in _sources.md with doc_type and retrieved.
- [ ] Any dimension scored 5 cites a retrieved binding document or a third-party attestation.
- [ ] python scripts/validate.py models inference-providers reports 0 errors.
- [ ] cd site && npm run build completes cleanly.
- [ ] CHANGELOG.md updated under Unreleased.
