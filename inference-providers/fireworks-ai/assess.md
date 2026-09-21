# Assess - Fireworks AI

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score - live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Correction (2026-09-21):** an earlier pass claimed to have read the Terms of Service Sec 3.6
directly from a downloaded PDF. An independent Cowork browser session found
`fireworks.ai/terms-of-service` to be page-level noindexed, returning ROBOTS_DISALLOWED - a real
browser cannot reach it, so the ToS-level clause is not independently verified. What IS confirmed,
via the readable `data_handling` docs page: **Zero Data Retention** for serverless and dedicated
inference, with one carve-out - the **Response API**, which stores conversation data **by
default** (`store=true`) with **30-day auto-deletion**; `store=false` disables retention entirely,
and stored responses can be force-deleted by `response_id`. Separately, via the **Privacy
Policy** (a different, readable document): **"We do not use your prompts, training data, or API
inputs to train or improve our AI models without your explicit opt-in."** - training is opt-in,
not a flat "never."

<!-- item: data-ownership -->
## Data & IP ownership

**Correction (2026-09-21):** a prior claim of a Terms Sec 3.2/7 ownership clause and a DPA
Schedule 4 sub-processor list (naming AWS, GCP, OCI, and Anthropic) rests on the same unreachable
documents as above - `fireworks.ai/dpa` is also noindexed and ROBOTS_DISALLOWED to a real
browser. These claims are not independently verified; treat them as a documented gap rather than
grounding. There is no confirmed confidentiality clause over Customer Content either way -
confidentiality is coded `unknown`, not `functional_only`, pending a rendered PDF or authenticated
Trust Center access.

<!-- item: residency -->
## Residency & sovereignty

On-demand and dedicated deployments can be pinned to **US, Europe or Asia-Pacific**, though region
selection beyond the default requires a **sales-granted quota**. A **Virtual Cloud (BYOC)**
option runs the inference engine inside the customer's own VPC so "data never leaves your secure
environment" - enterprise-negotiated, not self-serve. A separate **"US-only serverless"** tier
(1.5x price premium) implies default serverless residency is not itself EU-pinned.

**CLOUD Act disclosure:** Fireworks is contractually domiciled in Delaware, USA; standard US
jurisdiction applies even to EU/APAC-hosted on-demand workloads.

<!-- item: compliance -->
## Compliance & attestations

Fireworks' own blog and docs FAQ (both independently browser-confirmed) announce **SOC 2 Type
II** (2023-10-27), **HIPAA compliance**, and a **triple ISO certification** (27001 / 27701 /
42001, 2025-11-19) - no auditor is named on either announcement and neither carries a
certificate/report date. A trust centre exists at **trust.fireworks.ai**, but it is fully
JS-gated - the certificates and audit reports themselves were not independently read this pass. A
prior claim that the DPA references GDPR SCCs and a UK Addendum is unconfirmed (the DPA itself is
unreachable - see Data governance).

<!-- item: security -->
## Security controls

Independently browser-confirmed, verbatim: **"Data is encrypted in transit (TLS 1.2+) and at
rest (AES-256)."** Dedicated workloads run in **"logically isolated environments, preventing
cross-customer access or data leakage,"** access follows **least privilege**, and
**customer-managed keys** are available (CMEK). **"Regular penetration testing validates
controls"** - now confirmed verbatim. No public bug-bounty programme was found, and the
serverless multi-tenancy isolation model itself was not detailed in the sources read (only the
dedicated tier is described).

<!-- item: pricing -->
## Pricing & cost model

Per-token serverless pricing (input / discounted cached-input / output) is published directly on
Fireworks' pricing docs, alongside per-GPU-second dedicated pricing. Batch inference runs at
**50% of standard price**; generic (non-featured) models are priced by parameter-size band; a
**"US-only serverless"** residency tier carries a **1.5x premium**. Example rates: Kimi K3
$3.00/$0.30-cached/$15.00 per 1M tokens; DeepSeek V4.1 Flash $0.30/$0.006-cached/$1.20; GLM-5.3
Flash $0.15/$0.03-cached/$0.50.

<!-- item: reliability -->
## Reliability posture

A public **status page** (status.fireworks.ai, read directly) shows per-endpoint 90-day uptime in
the **~99.67-100%** range across roughly 28 tracked serverless model endpoints. No SLA or
service-credit clause was found in the standard Terms of Service - an enterprise contract may
carry a separate, non-public SLA.
