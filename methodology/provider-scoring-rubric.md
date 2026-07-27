# Provider Scoring Rubric (Inference & Hosting Providers)

**Version:** `1.1` · **Baseline:** July 2026

Providers are not models - they are *services you route data through* or *sources you
pull weights from*. They are scored on an adapted rubric that emphasises **data
governance, compliance, provenance, and lock-in** over raw capability. Same 0-5 anchors,
same 0-100 rollup and letter grades as the [model rubric](scoring-rubric.md), same
evidence rules.

Two profiles share most dimensions but weight them differently.

---

## Inference providers (serve models via API - your data leaves your network)

| # | Dimension | Weight | What it measures |
|---|---|--------|---|
| 1 | **Data Governance & Privacy** | 0.24 | Default retention, training-on-inputs, ZDR availability & scope, sub-processors, third-party model routing leakage |
| 2 | **Compliance & Certifications** | 0.18 | SOC 2 (Type I vs II), ISO 27001/27701, HIPAA/BAA, GDPR/DPA, FedRAMP |
| 3 | **Data Residency & Sovereignty** | 0.16 | EU regions, sovereign options, CLOUD Act exposure, region pinning |
| 4 | **Security Posture** | 0.14 | Isolation/tenancy, encryption, access controls, pen-testing, incident history |
| 5 | **Reliability & SLA** | 0.12 | Uptime record, SLA terms, failover, incident communication |
| 6 | **Transparency & Lock-in** | 0.10 | Model portability, OpenAI-compat, dedicated-vs-serverless clarity, exit cost |
| 7 | **Cost & Value** | 0.06 | Pricing clarity and competitiveness (informational; lightly weighted) |

### Inference-provider anchors

Every rung 0-5 is defined for all seven dimensions (no interpolated middle), so an
inference-provider score maps to a written anchor the same way a model score does.

**D1 Data Governance & Privacy** (weight 0.24)

| Score | Anchor |
|---|---|
| 0 | Retains and may train on inputs by default; no ZDR; opaque sub-processors. |
| 1 | Retains inputs by default; training-on-inputs unclear; no ZDR; sub-processors undocumented. |
| 2 | No training on inputs claimed, but retention is the default with only a limited opt-out; ZDR unavailable or unclear; partial sub-processor disclosure. |
| 3 | No training by default; ZDR available; retention documented; some caveats (e.g. free-tier logs, third-party model routing under other terms). |
| 4 | Contractually no training; short bounded retention or ZDR by default on paid tiers; sub-processors disclosed and routing terms clear - short of zero-retention-by-default. |
| 5 | Zero retention by default, contractually no training, ZDR verifiable, sub-processors disclosed, third-party routing leakage clearly flagged. |

**D2 Compliance & Certifications** (weight 0.18)

| Score | Anchor |
|---|---|
| 0 | None documented / no trust page. |
| 1 | Security/privacy claims on a marketing page only; no third-party certification and no DPA. |
| 2 | A DPA is available and one certification is in progress or self-attested (e.g. SOC 2 Type I), but no completed independent audit. |
| 3 | SOC 2 (Type II) **or** ISO 27001, GDPR/DPA available. |
| 4 | Two of {SOC 2 Type II, ISO 27001, HIPAA/BAA} - or two independent security attestations (e.g. ISO 27001 + CSA STAR) - plus GDPR/DPA documented; short of the full HIPAA + ISO 27701 + published-trust-centre set. |
| 5 | SOC 2 Type II **and** ISO 27001/27701, HIPAA/BAA where relevant, published trust centre. |

**D3 Data Residency & Sovereignty** (weight 0.16)

| Score | Anchor |
|---|---|
| 0 | Single-region (typically US), no residency options. |
| 1 | Multi-region for latency only, with no data-residency guarantee or region pinning. |
| 2 | An EU region is offered for some workloads but without pinning guarantees or a documented data boundary. |
| 3 | EU region available for at least some workloads. |
| 4 | EU/sovereign residency with region pinning for the main workloads and a documented data boundary - short of sovereign guarantees across all services. |
| 5 | EU/sovereign residency with region pinning and documented data-boundary guarantees; CLOUD-Act exposure honestly disclosed. |

**D4 Security Posture** (weight 0.14)

| Score | Anchor |
|---|---|
| 0 | No documented isolation, encryption or access-control posture; no pen-testing; unresolved incident history. |
| 1 | Basic in-transit/at-rest encryption asserted, but no isolation model, access-control detail or testing disclosed. |
| 2 | Encryption in transit and at rest plus stated access controls, but no independent pen-test and only a thin or undocumented isolation story. |
| 3 | Documented tenant isolation, encryption in transit and at rest, role-based access control, and periodic penetration testing. |
| 4 | All of 3 **plus** independent pen-test attestation or a bug-bounty programme, and a clean or well-handled incident history. |
| 5 | Independently audited security posture (isolation, encryption, key management, access controls), regular third-party pen-testing/bug bounty, and a transparent incident-response record. |

**D5 Reliability & SLA** (weight 0.12)

| Score | Anchor |
|---|---|
| 0 | Not yet in production; no status page, no uptime record; opaque incident communication. |
| 1 | Best-effort only; no status page and no operational track record. |
| 2 | Serving in production but with no status page or published uptime history, and no SLA. |
| 3 | An operational track record with a public status page and documented incident communication (the SLA may be informal or absent). |
| 4 | Contractual SLA with credits, a solid public uptime record, and documented failover/redundancy - short of a long multi-year track record. |
| 5 | Strong contractual SLA with credits, a long verifiable uptime record, documented multi-region failover, and transparent, timely incident communication. |

**D6 Transparency & Lock-in** (weight 0.10)

| Score | Anchor |
|---|---|
| 0 | Proprietary API, custom silicon, no portability, opaque routing. |
| 1 | Proprietary API with some documentation but no open-model portability and unclear routing. |
| 2 | OpenAI-compatible surface but a largely proprietary catalogue, or an opaque sub-processor/routing story. |
| 3 | OpenAI-compatible API, standard open models, portable. |
| 4 | OpenAI-compatible API over open models with transparent routing and a documented exit path - short of full sub-processor transparency. |
| 5 | Fully portable (open models + open API), transparent routing/sub-processors, clear exit path. |

**D7 Cost & Value** (weight 0.06)

| Score | Anchor |
|---|---|
| 0 | Pricing undisclosed or quote-only; no way to estimate spend before committing. |
| 1 | Headline pricing shown but with material hidden costs (egress, minimums, opaque dedicated pricing). |
| 2 | Public per-token pricing but limited tier/quota transparency, or above-market rates for the class. |
| 3 | Clear public pricing that is broadly competitive for the class, with documented tiers. |
| 4 | Clear, competitive public pricing with a transparent dedicated/serverless breakdown and no surprise fees. |
| 5 | Fully transparent, competitive pricing across serverless and dedicated, with predictable, well-documented cost controls and no hidden fees. |

## Hosting / distribution providers (where weights live - you pull artifacts from them)

| # | Dimension | Weight | What it measures |
|---|---|--------|---|
| 1 | **Provenance & Integrity** | 0.26 | Verified orgs, signing, malware/pickle scanning, checksums, gating, revision pinning |
| 2 | **Format & Loader Safety** | 0.18 | safetensors default, pickle handling, `trust_remote_code` surface, loader CVE exposure |
| 3 | **License Surfacing & Governance** | 0.16 | License clarity, gating/EULA enforcement, terms of service |
| 4 | **Security Track Record** | 0.16 | History of malicious uploads, typosquatting response, disclosure handling |
| 5 | **Transparency & Trust Signals** | 0.12 | What trust signals are exposed to the downloader; how gameable they are |
| 6 | **Ecosystem & Portability** | 0.12 | Tooling, breadth, standards, lock-in |

### Hosting-provider anchors (abbreviated)

**D1 Provenance & Integrity**
- 0: Anonymous uploads, no scanning, no verified orgs, no checksums.
- 3: Verified orgs + automated malware/pickle scanning + content-addressed checksums + revision pinning.
- 5: All of the above **plus** cryptographic signing / provenance attestation surfaced to downloaders, and gated official releases.

**D2 Format & Loader Safety**
- 0: Pickle-first, silently executes code on load, `trust_remote_code` normalised.
- 3: safetensors promoted/default; pickle flagged; documents loader risks.
- 5: safetensors default and enforced where possible; template/config-injection surfaces documented; guidance to pin loader versions.

## Shared rules

- Same **evidence & sourcing rules** as models: a `5` anchor needs `onehill_verified`
  or `third_party` support; provider marketing alone caps at `3`.
- **Hard flags** (provider profile):
  - 🚩 Trains on customer inputs by default with no opt-out → **D** ceiling.
  - 🚩 No documented compliance and indefinite/unclear retention → **C** ceiling (inference).
  - 🚩 No malware scanning and pickle-first with anonymous uploads → **C** ceiling (hosting).
  - 🚩 Product discontinued / catalogue materially misrepresented → flagged prominently.
- **Universal disclosure:** US-headquartered providers carry a standing **CLOUD Act**
  note even when EU regions are offered; this is disclosed, not scored as a defect on
  its own.

### Rubric changelog
- **1.1** (2026-07) - Defined every rung 0-5 for all seven inference-provider dimensions
  (previously only D1/D2/D3/D6 carried abbreviated 0/3/5 bullets; D4 Security, D5
  Reliability and D7 Cost had none). Weights unchanged; triggers a re-score of every
  provider entry. Hosting-provider anchors remain abbreviated (out of scope for the
  current index).
- **1.0** (2026-07) - Initial provider rubric.
