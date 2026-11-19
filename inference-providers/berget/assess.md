# Assess - Berget AI

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Zero data retention is the default for serverless inference**, stated in two binding
documents. The Data Processing Agreement (updated 2026-10-22, and first in the Terms' order of
precedence) says in Appendix 2 that Berget applies "a true Zero Data Retention policy",
stores no prompts, files or outputs after completed calls, and keeps none of it on persisted
disks even during inference. The Terms of Service (Sec 7) say Berget will never store the
actual prompt content or the output content. The DPA also has an **express no-training
sentence**: "Berget AI does not train any models on the input or output from serverless inference
endpoints, nor does it share the data with any model providers for model training." The
catalogue is open-weight only, so no closed third-party model's data terms attach.

Inference retention is separate from **account termination**. On termination, Customer Data is
kept **30 days** for export and recovery, then irreversibly deleted. Berget does keep metadata
(service logs, API request metadata, token counts, API key and subscription ID for billing).
Two caveats apply. The Terms reserve a right to **aggregated, anonymised data** that
identifies neither the customer nor any natural person (Sec 19.1). The retention guarantees are
**not independently attested**: no SOC 2 or ISO 27001 audit stands behind them, which is why
data governance is held at 4, not 5.

<!-- item: data-ownership -->
## Data & IP ownership

**Your data stays yours**, per the Terms. As between Berget and the customer, the customer
retains all title and intellectual property rights in Customer Data (Sec 17.1). Berget's licence
is scoped to hosting, using, processing and transmitting it to provide the Service. Sec 18 is a
**mutual confidentiality clause** whose definition includes "in particular Customer Data", with a
duty on termination to cease use and destroy (Sec 18.5). The DPA names four sub-processors (AI
Iron AB, Acebit AB, Obenet AB and Stripe Payments Europe, Limited) and gives 30 days notice of
changes with an objection and termination right. The caveats are that the assurance rests on
binding terms with no independent audit, and the Sec 19.1 aggregated-data reservation. The
customer feedback licence (Sec 19.2) covers suggestions only.

<!-- item: residency -->
## Data residency & jurisdiction

**The binding boundary is the EEA, and the contract does not promise Sweden.** DPA Sec 10.1 says
all Berget data centres are in the EEA, and Sec 10.2 says Berget will not transfer personal data
outside the EEA without the customer's written instruction. The company is **Swedish-owned** with
no US parent, which keeps it outside US CLOUD Act reach. Three points temper the marketing.
First, Sec 10.1 lets the customer choose a data centre only for compute and storage, "not
including serverless inference", so a serverless customer cannot pin a data centre. Second, the
statements that data "stays within Sweden's borders", "never crosses borders" and involves "no US
entity" appear on the landing page, in the docs and in the Berget Code post, and no clause
promises them. Third, the Privacy page is a website privacy policy and says nothing about where
inference runs. The payment sub-processor, Stripe Payments Europe, Limited, is in Ireland. For an
EU adopter this is a strong jurisdictional position, scored 4 because the main workload has no
region pinning.

<!-- item: compliance -->
## Compliance & attestations

Berget publishes a **GDPR Data Processing Agreement** at berget.ai/en/dpa. It is an Art. 28(3)
controller-processor agreement with named sub-processors, a 24-hour breach notice where
feasible, an audit right (one per 12 months, customer pays), a 30-day return or deletion on
termination, and a Chapter V transfer clause (EU SCCs where applicable). Formal security
attestations - **SOC 2, ISO 27001, ISO 27701, HIPAA/BAA** - do not exist on any Berget page. ToS
Sec 6.7 says Berget "is actively working toward ISO 27001 certification". For ISO-dependent or
healthcare procurement, treat compliance as "GDPR DPA in place, no certificate yet".

<!-- item: security -->
## Security controls

ToS Sec 6.7 states **industry-standard technical and organisational measures** - encryption in
transit, network isolation, access controls and system monitoring - and DPA Sec 8 adds
pseudonymisation and encryption, restore capability and regular testing of the measures. The
page titled Security is a **responsible-disclosure policy** (GitHub private reporting, a PGP key,
a Signal number, a typical 48-hour response and a safe-harbour statement) and is not a trust
centre. No independently reviewed penetration test or SOC 2 / ISO 27001 attestation exists, so
the posture is stated but untested.

<!-- item: pricing -->
## Pricing & cost model

**Per-model per-token rates are published** through the API listing, in euros per million
tokens: for example Mistral-Small-3.2 0.30 in and 0.30 out, Gemma 4 31B 0.25 and 0.50, Kimi K3.1
Pro 3.00 and 10.00. **There is no pure pay-as-you-go**: the pricing FAQ says API access needs an
active plan, from the free Trial (EUR 5 credits) through Starter EUR 25, Team EUR 50 and
Enterprise EUR 500 per month, each a prepaid top-up. Credits are non-refundable and expire after
12 months. Berget Code is EUR 150 to 500 per seat per month, and Dedicated Inference is quoted
from about EUR 2,500 per GPU per month. Zero retention is the default and carries no premium.

<!-- item: reliability -->
## Reliability posture

The **SLA (2026-10-23)** gives serverless inference, including Berget Code, a **best-effort**
level with "no compensation payable for interruptions". A **99.5% monthly uptime** commitment
with fee credits of 10% or 25% covers only **Dedicated Inference with an HA setup**, which is
sales-contracted. The SLA names `status.berget.ai` for incident information, but that page is a
JavaScript shell with no readable content, so no incident history or uptime record is
available. The tech.eu article supports production use since 2025 but names no customers.
Serverless is unsuitable for availability-critical workloads without a dedicated contract.
