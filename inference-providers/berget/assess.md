# Assess - Berget AI

_Should we route our data through this provider? Data governance, data & IP ownership,
residency, compliance, security, pricing, and reliability - plus the provider AOI score -
live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Zero data retention is the default**, stated in the binding Terms of Service: Berget will
never store the actual prompt content used as model input or the output content generated
by the LLMs it hosts. There is **no training on customer inputs** -
the Terms grant Berget a licence limited to hosting and processing data to provide the Service,
no training right, and Berget Code separately confirms it does not train on customer code. The
catalogue is open-weight only, so no closed third-party model's data terms attach to routed
inference.

Separate one thing from the zero-inference-retention default: on **account termination**,
Customer Data is retained for **30 days** to allow export and recovery, then irreversibly
deleted. That is a lifecycle/exit provision, not ongoing inference retention. Two honest
caveats: the Terms reserve a right to process **aggregated, anonymised data** that does not
identify the customer or any natural person, and the data-handling guarantees are **not
independently attested** - there is no SOC 2 / ISO 27001 audit and the DPA's sub-processor
list is not disclosed. Contractualise the specifics in the DPA.

<!-- item: data-ownership -->
## Data & IP ownership

**Your data and the knowledge derived from it stay yours**, per the Terms. As between Berget
and the customer, the customer retains all title and intellectual
property rights in the Customer Data; Berget's licence is scoped only to hosting, processing
and transmitting that data to provide the Service. Combined with zero retention of prompt and
output content and open-weight-only serving, nothing is captured to improve the service beyond
aggregated, anonymised, non-identifying usage data, and no closed third-party model's terms
attach. The caveat is provenance-of-assurance: the posture is **documented in binding terms but
not independently audited**, and the **sub-processor list is not disclosed**.

<!-- item: residency -->
## Data residency & jurisdiction

**Infrastructure runs entirely on EU/Sweden-only servers with no US data transfers** per
Berget's Privacy and Security pages, the company is **Swedish-owned**, and it is therefore
**not subject to the US CLOUD Act** or equivalent extraterritorial legislation - Berget's
strongest card, and independently reported by EU tech press covering its Sweden-based sovereign
infrastructure. For an EU adopter this is genuine data sovereignty: no region setting to get
wrong because there is no non-EU region, and no US jurisdiction that could compel disclosure or
unilaterally cut off access. Switch-off risk from an extraterritorial actor is effectively
removed.

<!-- item: compliance -->
## Compliance & attestations

Berget publishes a **GDPR Data Processing Agreement** at berget.ai/dpa, which establishes the
legal basis for EU processing - though its clauses (transfer mechanism, SCCs, sub-processor
list) are not disclosed. Formal security attestations - **SOC 2, ISO 27001,
ISO 27701, HIPAA/BAA** - are **not confirmed**. For ISO-dependent or healthcare procurement,
treat compliance as "GDPR DPA in place, security attestations to be verified" and request the
current attestation status directly.

<!-- item: security -->
## Security controls

The Security page documents **industry-standard technical and organisational measures** -
encryption in transit, network isolation, access controls and system monitoring - plus a
**PGP-based channel** for encrypted vulnerability reporting. Inference runs inside a secure
Swedish network and content is not retained. Beyond that, no independently reviewed penetration
test or SOC 2 / ISO 27001 attestation was surfaced, so this is assessed as solid-but-partial:
the architectural controls are documented, but the deepest independent assurance is not visible.

<!-- item: pricing -->
## Pricing & cost model

Pricing is **pay-as-you-go per token**, with **prepaid token packs** also offered, and **zero
data retention is the default** rather than sold as a premium add-on. Per-model rates are not
published; treat pricing as transparent-in-model but **confirm live per-model
rates** on the provider pricing page before committing.

<!-- item: reliability -->
## Reliability posture

Independent press reports real production usage - the Swedish central bank (Riksbanken) as a
flagship customer and 300+ pilot/commercial customers - but **no public uptime SLA or status
page was found**. Reliability is therefore assessed conservatively: production-proven on
available evidence, but without an observable status/SLA record to lean on for
availability-critical workloads.
