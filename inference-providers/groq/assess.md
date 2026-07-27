# Assess - Groq

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score (70.0/100 · Grade B) -
live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

The governing documents - the **Groq Services Agreement** and the **your-data docs** -
say inference is **not retained by default** and is **never trained on**: Groq
"is not permitted to use Inputs or Outputs for training or fine-tuning any AI Model Services or
other models" and "will never access Customer Data for training purposes." **Zero data retention
is available to all customers** through Data Controls, not gated to an enterprise tier. Because
Groq serves open-weight models on its own LPU hardware, there is no closed third-party model
whose data terms would attach to routed inference.

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

The **trust centre** states **SOC 2 Type II** is maintained (2025 report). The **DPA**
covers **GDPR, CCPA and PDPL**, and a **HIPAA BAA** is offered (the BAA excludes the
Compound system as a non-covered service). **ISO 27001 / 27701 are unconfirmed**, and the SOC 2
report itself is **gated** behind request rather than read here. For ISO-dependent or healthcare
procurement, request the current attestation letters and countersign the BAA directly.

<!-- item: residency -->
## Data residency & jurisdiction

Default storage is **US**, with a **European data centre in Helsinki, Finland** launched (with
Equinix) on **6 July 2025**. The EU footprint is therefore real but **very recent**, **region
pinning is unconfirmed**, and the **DPA expressly permits Processing in the United States and
other countries** - so treat EU residency as an emerging capability to validate in onboarding
rather than a mature guarantee. As a US-headquartered company, Groq also carries standing **US
CLOUD Act exposure** regardless of region.

<!-- item: security -->
## Security controls

Documented controls include **SOC 2 Type II** scope (trust centre), **Data Controls** for enabling
ZDR, and the Services Agreement's commitment that Groq **does not access, store or retain Inputs or
Outputs except to provide the service**. No independently reviewed penetration test is surfaced, and
the SOC 2 report itself is gated (not read). This is assessed as solid-but-partial:
day-to-day controls are documented, but the deepest independent assurance is not visible.

<!-- item: pricing -->
## Pricing & cost model

Pricing is **per-token** with a **rate-limited free/developer tier**, read from Groq's own pricing
page. Confirmed rates include **Llama 3.3 70B $0.59/$0.79** and **gpt-oss-120B $0.15/$0.60** per M
in/out; other example rates (Llama 3.1 8B $0.05/$0.08, DeepSeek R1 Distill Llama 70B $0.75/$0.99)
are **approximate**, so treat them as an order-of-magnitude guide and confirm live rates before
committing.

<!-- item: reliability -->
## Reliability posture

The **trust centre** attests operational controls, but Groq is a **fast-scaling hardware startup**
with **no public uptime SLA or status history independently verified**. Reliability is
therefore assessed conservatively: adequate on available evidence, but without an observable
status/SLA record to lean on for availability-critical workloads.
