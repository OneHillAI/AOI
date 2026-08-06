## Tasks

### Schema
- [x] Add `data_governance.confidentiality` (enum) + `confidentiality_caveats` to
  `schema/inference-provider.v2.schema.json`.
- [x] Add top-level `dedicated_availability` (enum) + `dedicated_notes` to the provider schema.

### Methodology
- [ ] Update `methodology/provider-scoring-rubric.md`: document `confidentiality` as a
  `data_governance` input and `dedicated_availability` as a `transparency_lockin` input, with the
  `disclaimed`/`adverse` cap and the on-prem/air-gapped uplift; bump provider rubric to `1.2`.

### Entries (populate fields + re-score against 2026-08-06 primary sources)
- [ ] groq: confidentiality `mutual` (§10), dedicated `enterprise_only` (GroqMetal/GroqRack).
- [ ] berget: confidentiality `explicit` (ToS §18), dedicated `coming_soon`; subprocessors disclosed
  (DPA Appendix 1, entirely-EEA).
- [ ] infercom: confidentiality `functional_only` (no express duty), dedicated `available`
  (single-tenant racks + on-prem/air-gapped).
- [ ] together: confidentiality `disclaimed` (ToS §9), dedicated `self_serve`.
- [ ] deepinfra: confidentiality `functional_only` (no clause; memory-only + "remain private"),
  dedicated `self_serve`; note no DPA / US-only / debugging carve-out.
- [ ] runware: confidentiality `adverse` (content deemed non-confidential + perpetual licence),
  dedicated `enterprise_only`; note private-uploaded-models exception.

### Validate
- [ ] `scripts/score.py --write` on all six; `scripts/completeness.py --write`; `scripts/validate.py`
  green (0 errors). Record every score delta in each entry's changelog and the PR body.
