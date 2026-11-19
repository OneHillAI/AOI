# Assess - Groq

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score (72.4/100 · Grade B) -
live here. Re-read against live sources on 2026-11-19._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

The governing documents - the **Groq Services Agreement** and the **your-data docs** -
say inference is **not retained by default** and is **never trained on**: Groq
"is not permitted to use Inputs or Outputs for training or fine-tuning any AI Model Services or
other models" and "will never access Customer Data for training purposes." **Zero data retention
is available to all customers** through Data Controls, not gated to an enterprise tier. Because
Groq serves open-weight models on its own LPU hardware, there is no closed third-party model
whose data terms would attach to routed inference.

One nuance the docs add: inputs and outputs **may be logged for up to 30 days** when Groq is
troubleshooting platform errors or investigating suspected abuse, unless ZDR is switched on. The
Services Agreement (Sec 4.2, last modified 2026-06-22, unchanged) allows the same access, and limits
ZDR to undefined "Eligible Customers" while the docs say all customers may enable it - confirm your
eligibility before relying on it.

The caveat is in the non-inference features: **batch processing retains input/output files for
30 days** unless deleted, and **fine-tuning retains weights and datasets until the customer
deletes them**, with that retained data stored in **US GCP buckets**. So the "not retained"
headline holds for streaming inference but not automatically for batch or fine-tuning workflows -
plan those data lifecycles explicitly.

<!-- item: data-ownership -->
## Data & IP ownership

The **Services Agreement** is explicit: the customer "retains all Intellectual Property Rights in
Customer Data (including in Inputs and Outputs)," and Groq "does not access, use, store, or retain
Inputs or Outputs except as necessary to provide the Cloud Services." Combined with never-training
and open-weight-only serving, **your data and the knowledge derived from it stay yours**. The
**DPA** discloses a **published sub-processor list** at trust.groq.com/subprocessors with a 15-day
written objection right - a correction to the earlier "not disclosed" reading. The caveats are
lifecycle rather than training: the **batch (30-day)** and **fine-tuning** features retain data in
**US GCP storage** until you delete it. Contractualise the specifics through the DPA and BAA.

<!-- item: compliance -->
## Compliance & attestations

The **trust centre** claimed **SOC 2 Type II** (2025 report) when read in July; **trust.groq.com is
now a JavaScript-only page** that could not be read on 2026-11-19, so the claim is not re-confirmed
and the sub-processor list was not read. The **DPA** (read, unchanged) covers **GDPR, CCPA and PDPL**
with deemed-signed EU SCCs, and a **HIPAA BAA** is offered for generally available services only
(beta and preview features are excluded). **ISO 27001 / 27701 are unconfirmed**, and the SOC 2
report itself is **gated** behind request rather than read here. For ISO-dependent or healthcare
procurement, request the current attestation letters and countersign the BAA directly.

<!-- item: residency -->
## Data residency & jurisdiction

Retained customer data sits in **US GCP buckets** (your-data docs). EU capacity exists: Groq
launched a **Helsinki, Finland** site with Equinix on **6 July 2025**, and its platform page now
lists **EU-1 Vantaa (Finland) and EU-2 London** among 13 data centers. **Region pinning is
unconfirmed**, EEA customers contract with **Groq UK Limited**, and the **DPA expressly permits
Processing in the United States and other countries** - so treat EU residency as a capability to
validate in onboarding rather than a contractual guarantee. As a US-headquartered company, Groq also carries standing **US
CLOUD Act exposure** regardless of region.

<!-- item: security -->
## Security controls

Documented controls include **SOC 2 Type II** scope (earlier trust-centre read), the DPA's Annex II
measures (zero-trust network access, subprocessor assessments, regular security testing), a **private
HackerOne** vulnerability programme, **Data Controls** for enabling ZDR, and the Services Agreement's commitment that Groq **does not access, store or retain Inputs or
Outputs except to provide the service**. No independently reviewed penetration test is surfaced, and
the SOC 2 report itself is gated (not read). This is assessed as solid-but-partial:
day-to-day controls are documented, but the deepest independent assurance is not visible.

<!-- item: pricing -->
## Pricing & cost model

Pricing is **per-token** with a **rate-limited developer tier**, read on 2026-11-19 from the docs
models page (groq.com/pricing now redirects to the home page). Current rates per M in/out:
**gpt-oss-120B $0.15/$0.60**, **gpt-oss-20B $0.075/$0.30**, **Qwen3.8-27B $0.80/$4.00** (preview).
**Llama 3.1 8B and Llama 3.3 70B are now "Contact Sales"** (retired for free and developer tiers
on 2026-08-16), so the older Llama and DeepSeek R1 distill rates no longer apply. Confirm live rates
before committing.

<!-- item: reliability -->
## Reliability posture

Groq now has a **public status page** (groqstatus.com), which earlier passes missed. On 2026-11-19
it reported "fully operational" and, for August to November 2026, **100% uptime for the API and
all six production model components** and 99.98% across seven preview components. **No SLA is
published**; the Services Agreement mentions service level commitments only as a paid add-on. The
self-serve catalogue turns over quickly (see Models served), so plan for model retirements.
