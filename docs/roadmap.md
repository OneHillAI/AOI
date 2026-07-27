# Roadmap & Status

This registry is built foundation-first: get the method, schema, and tooling right, prove
them with deeply-worked exemplars, then scale coverage on top via the refresh pipeline.

## v0.1 - Foundation (this release)

**Done**
- ✅ Mission, architecture, and design principles ([`README.md`](../README.md)).
- ✅ Full public methodology: [scoring rubric](../methodology/scoring-rubric.md),
  [openness framework](../methodology/openness-framework.md),
  [supply-chain risk](../methodology/supply-chain-risk.md),
  [EU AI Act mapping](../methodology/eu-ai-act-mapping.md),
  [benchmark method](../methodology/benchmark-methodology.md),
  [safe-deployment playbook](../methodology/safe-deployment-playbook.md),
  [provider rubric](../methodology/provider-scoring-rubric.md),
  [update automation](../methodology/update-automation.md).
- ✅ Machine-readable schema for models + inference/hosting providers ([`schema/`](../schema/)).
- ✅ Scoring + validation tooling and CI ([`scripts/`](../scripts/), [`.github/`](../.github/)).
- ✅ Contribution templates ([`templates/`](../templates/)).
- ✅ Worked exemplar entries across the openness spectrum (see the section indexes).

## v0.2 - Breadth

- Expand model coverage to the full set of leading open families and their key variants.
- Expand inference-provider and hosting-provider coverage.
- Add EU-language capability probes to the benchmark core.
- Publish the benchmark harness (`ohbench`) so `onehill_verified` numbers are reproducible.

## v0.3 - Automation

- Hub-API collectors (versions, files, license, gating, format, verified-org, downloads).
- Security-feed watchers (CVEs, malicious-mirror findings, poisoning reports).
- Regulatory-feed watcher (AI Office guidance, template changes, systemic-risk designations).
- Scheduled refresh job that opens diff PRs; human review gates score/flag/ceiling changes.
  (Design: [update-automation.md](../methodology/update-automation.md).)

## v1.0 - Living registry

- Continuous refresh across the long tail within freshness SLAs.
- Public leaderboards generated from the data files.
- An `onehill_verified` badge backed by reproducible eval + verified provenance.

## Known limitations (stated honestly)

- OneHill cannot independently re-run every eval on every checkpoint at launch; entries
  mark which numbers are `onehill_verified` vs `third_party`/`publisher`.
- The 2026 model landscape moves weekly; version numbers, prices, and certs carry dates
  and short freshness SLAs precisely because they change.
- Scores are opinions with receipts, not warranties, and nothing here is legal advice.
