# Assess - Fireworks AI

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Binding Terms (Last Updated 2026-07-10), Sec 3.6: "We will not use your Content to train our own
models or to improve the Service." Fireworks has adopted a Zero Data Retention policy: no logging
of Content for human review and no retention beyond the time it takes to generate and deliver
Output.

The commitment covers inference only. It excludes the Response API (stores conversation data by
default with `store=true`, up to 30 days; `store=false` disables it and `response_id` deletes it),
prompt caching (DPA 4.5), the Batch API (docs), and "any training, fine-tuning, or agent
features". Fireworks also reserves the right to run safety screening tools on Content. The Privacy
Notice says no training "without your explicit opt-in", which is looser than the Terms; the Terms
are the contract.

<!-- item: data-ownership -->
## Data & IP ownership

Sec 3.2 and 7: you own all right, title and interest in your Content (Input and Output). Sec 3.4
grants Fireworks a worldwide, royalty-free, non-exclusive licence to use it "for the purpose of
providing the Service to you". Sec 8 (Confidential Information) is one-directional: it protects
information "of Fireworks ane [sic] its licensors" and does not name your Content, so there is no
express confidentiality duty over it (functional_only; use an enterprise contract for trade
secrets).

DPA 11.2: on request within 30 days of expiry you get a copy or a self-service download, then
deletion. The DPA has Schedules 1 to 3 only; it has no Schedule 4 and does not name Anthropic. The
sub-processor list is on `trust.fireworks.ai/subprocessors`, a JavaScript-only page, so its names
are unverified.

<!-- item: residency -->
## Residency & sovereignty

On-demand and dedicated deployments use the GLOBAL multi-region unless you ask otherwise. Pinning
to US, Canada, Europe or APAC needs a quota granted by Fireworks, is fixed at creation, and costs
1.5x. US-only serverless is a 50% premium on select models. Fireworks Sovereign (and the Virtual
Cloud / BYOC option) runs the engine in the customer's own cluster: enterprise, priced by
contract, training "coming soon". DPA 6.1 lets Covered Data be processed wherever Fireworks or its
sub-processors maintain facilities.

CLOUD Act disclosure: Fireworks is contractually domiciled in Delaware, USA; standard US
jurisdiction applies even to EU/APAC-hosted on-demand workloads.

<!-- item: compliance -->
## Compliance & attestations

Fireworks' blog, docs FAQ, pricing page and DPA Schedule 2 state SOC 2 Type II (blog 2023-10-27),
HIPAA compliance (BAA for enterprise) and ISO 27001 / 27701 / 42001 (blog 2025-11-19). No auditor,
certification body or certificate date is stated, and the trust centre at trust.fireworks.ai
renders nothing without JavaScript, so these are vendor statements, not third-party artefacts. The
DPA carries SCCs (Module Two, Irish law), a UK Addendum and a 48-hour breach notice.

<!-- item: security -->
## Security controls

"Data is encrypted in transit (TLS 1.2+) and at rest (AES-256)." Dedicated workloads run in
"logically isolated environments", access follows least privilege, and customer-managed keys are
available. "Regular penetration testing validates controls." DPA Schedule 2 lists the
organisational measures. No public bug-bounty programme is published, and the serverless
multi-tenancy isolation model is not detailed (only the dedicated tier is).

<!-- item: pricing -->
## Pricing & cost model

Per-token serverless pricing (input / discounted cached-input / output) is published on Fireworks'
pricing docs, alongside per-GPU-second dedicated pricing (H100 80GB 8.00 USD per hour, B200 13.00,
GB300 20.00). Batch inference is 50% off, a Priority tier is 1.25x Standard, spot is 30% off on
select models, and generic models are priced by parameter-size band. US-only serverless and
region-restricted deployments carry a 1.5x premium.

Example rates per 1M tokens: Kimi K3 $3.00/$0.30-cached/$15.00; DeepSeek V4.1 Flash
$0.30/$0.006-cached/$1.20; GLM-5.3 Flash $0.15/$0.03-cached/$0.50; gpt-oss-120b
$0.15/$0.015-cached/$0.60.

<!-- item: reliability -->
## Reliability posture

A public status page (status.fireworks.ai) lists 23 serverless endpoints: 22 at 100% and the
lowest (Kimi K3.1 Pro) at 99.50% over 90 days, with no listed incidents. The standard Terms
(Sec 14, "as is" and "as available") carry no SLA or service-credit clause. Enterprise Reserved
Throughput advertises a "Throughput SLA and 99.9% uptime terms" that are not public and do not
cover overage.
