# Assess - Groq

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

The governing documents, the Groq Services Agreement and the your-data docs, say inference is not retained by default and is never trained on. Groq "is not permitted to use Inputs or Outputs for training or fine-tuning any AI Model Services or other models". It also "will never access Customer Data for training purposes." Zero data retention is available to all customers through Data Controls and is not gated to an enterprise tier. Groq serves open-weight models on its own LPU hardware, so no closed third-party model's data terms attach to routed inference.

The docs add that inputs and outputs may be logged for up to 30 days when Groq troubleshoots platform errors or investigates suspected abuse, unless ZDR is on. The Services Agreement (Sec 4.2, last modified 2026-06-22) allows the same access and limits ZDR to undefined "Eligible Customers", while the docs say all customers may enable it. Confirm eligibility before relying on it.

The caveat is in the non-inference features. Batch processing retains input/output files for 30 days unless deleted, and fine-tuning retains weights and datasets until the customer deletes them. That retained data is stored in US GCP buckets. The "not retained" headline holds for streaming inference but not automatically for batch or fine-tuning workflows, so plan those data lifecycles explicitly.

<!-- item: data-ownership -->
## Data & IP ownership

Under the Services Agreement, Groq "does not access, use, store, or retain Inputs or Outputs except as necessary to provide the Cloud Services". The customer "retains all Intellectual Property Rights in Customer Data (including in Inputs and Outputs)," so its data and derived knowledge stay with the customer, given never-training and open-weight-only serving. The DPA discloses a published sub-processor list at trust.groq.com/subprocessors with a 15-day written objection right. The caveats concern data lifecycle and not training: the batch (30-day) and fine-tuning features retain data in US GCP storage until deleted. Contractualise the specifics through the DPA and BAA.

<!-- item: compliance -->
## Compliance & attestations

The trust centre claims SOC 2 Type II (2025 report). The trust.groq.com page is JavaScript-only and cannot be read, so the claim is unconfirmed and the sub-processor list is unread. The DPA covers GDPR, CCPA and PDPL with deemed-signed EU SCCs. A HIPAA BAA is offered for generally available services only (beta and preview features are excluded). ISO 27001 / 27701 are unconfirmed, and the SOC 2 report itself is gated behind request. For ISO-dependent or healthcare procurement, request the current attestation letters and countersign the BAA directly.

<!-- item: residency -->
## Data residency & jurisdiction

Retained customer data sits in US GCP buckets (your-data docs). EU capacity exists: Groq launched a Helsinki, Finland site with Equinix on 6 July 2025, and its platform page lists EU-1 Vantaa (Finland) and EU-2 London among 13 data centers. Region pinning is unconfirmed, EEA customers contract with Groq UK Limited, and the DPA expressly permits Processing in the United States and other countries. EU residency is a capability to validate in onboarding and no contract guarantees it. As a US-headquartered company, Groq also carries standing US CLOUD Act exposure regardless of region.

<!-- item: security -->
## Security controls

Documented controls include SOC 2 Type II scope (trust-centre claim), the DPA's Annex II measures (zero-trust network access, subprocessor assessments, regular security testing), a private HackerOne vulnerability programme and Data Controls for enabling ZDR. The Services Agreement commits Groq not to access, store or retain Inputs or Outputs except to provide the service. No independently reviewed penetration test is surfaced, and the SOC 2 report itself is gated. Day-to-day controls are documented, but the deepest independent assurance is not visible, so the assessment is solid but partial.

<!-- item: pricing -->
## Pricing & cost model

Pricing is per-token with a rate-limited developer tier, taken from the docs models page (groq.com/pricing redirects to the home page). Rates per M in/out are gpt-oss-120B $0.15/$0.60, gpt-oss-20B $0.075/$0.30 and Qwen3.8-27B $0.80/$4.00 (preview). Llama 3.1 8B and Llama 3.3 70B are "Contact Sales" (retired for free and developer tiers on 2026-08-16), so the older Llama and DeepSeek R1 distill rates no longer apply. Confirm live rates before committing.

<!-- item: reliability -->
## Reliability posture

Groq has a public status page (groqstatus.com). On 2026-11-19 it reported "fully operational" and, for August to November 2026, 100% uptime for the API and all six production model components and 99.98% across seven preview components. No SLA is published, and the Services Agreement mentions service level commitments only as a paid add-on. The self-serve catalogue turns over quickly (see Models served), so plan for model retirements.
