# Assess - Baseten

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score - live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Baseten's **security-practices page** (independently browser-confirmed, verbatim) states: **"ZDR
is the default configuration for the customer's use of the inference products"** for Model APIs
and Dedicated Inference - **Zero Data Retention is the default**, not an opt-in or
enterprise-gated feature. **Correction:** this default lives on the Security Practices page, not
the Terms directly - Terms Sec 2.5 merely honours whatever posture Security Practices designates.
The one exception is **Async Inference**, which queues inputs for up to **72 hours** before
deletion (outputs are never stored on that path either). Terms & Conditions Sec 6.3 bars Baseten
from using **Customer Content - including deployed model weights and outputs -** to train,
fine-tune, or otherwise develop its own models.

<!-- item: data-ownership -->
## Data & IP ownership

Terms & Conditions Sec 6.1 (independently browser-confirmed): **"Customer reserves all rights,
title, and interest in and to Customer Content,"** a definition that includes deployed **Customer
Models** and **Model Outputs**. A **MUTUAL confidentiality clause** (Sec 11.1-11.2) - confirmed
on **two separate live fetches** - requires both parties to protect confidential information
**"with the same degree of care it uses for its own (but no less than reasonable care),"**
surviving **three years** after termination (trade secrets indefinitely, Sec 11.4) - a genuine,
independently-verified positive, stronger than several peers' one-directional or disclaimed
clauses. The sub-processor list (trust.baseten.co) exists with a 15-day pre-notification
commitment (DPA Sec 7.1), though its actual named contents remain unread - the portal is a
JS-gated Vanta page that returns only a meta description on every path tried.

<!-- item: residency -->
## Residency & sovereignty

No published, named **EU region** exists for the managed service. A **"regional environments"**
feature can route a deployment to a designated region, but the docs direct customers to **contact
support** to confirm availability - there is no self-serve, published region list. The practical
EU-residency path is **Baseten Self-Hosted**, which runs the entire workload plane inside the
customer's own VPC/cloud in any region, including the EU.

**CLOUD Act disclosure:** Baseten is US-headquartered (San Francisco); standard US jurisdiction
applies to the managed service.

<!-- item: compliance -->
## Compliance & attestations

**SOC 2 Type II** is confirmed, with a named audit firm (Sensiba San Filippo LLP) and a clean
opinion across Security/Availability/Processing Integrity/Confidentiality/Privacy criteria.
**HIPAA** and a **GDPR DPA** are both confirmed directly. **Correction:** a prior claim of **ISO
27001** certification is retracted - an independent browser pass found no trace of it anywhere,
not even self-attested; **ISO 27701**, **PCI DSS**, **FedRAMP**, and **CSA STAR** remain
unconfirmed - the Vanta Trust Center that would carry such certificates is fully JS-gated.

<!-- item: security -->
## Security controls

**Correction (description, not substance):** independently browser-confirmed isolation is
logical namespace separation for shared use (access controls, unique customer identifiers) plus
**Dedicated** single-tenant Kubernetes namespaces with Calico/Cilium network policies ("Baseten
never shares GPUs across users") and **Self-Hosted** deployment inside the customer's own VPC -
not an explicit "three-tier" model as previously described, though the practical effect is
similar. Encryption is **TLS 1.2+** in transit and **AES-256** at rest; access is
**least-privilege with enforced MFA** for all personnel. Baseten states it engages qualified
third-party firms for **periodic penetration testing** (confirmed verbatim); no public
bug-bounty programme was found.

<!-- item: pricing -->
## Pricing & cost model

Per-token pricing for hosted Model APIs and per-GPU-minute pricing for dedicated deployments are
both published directly on Baseten's pricing page, across Basic/Pro/Enterprise tiers. Example
rates: GLM-5.3 $1.40/$0.14-cached/$4.40 per 1M tokens; DeepSeek V4.1 Flash
$0.30/$0.03-cached/$1.20; dedicated GPU-minute rates from T4 $0.01052 up to H100 80GB $0.10833
(~$6.50/hr).

<!-- item: reliability -->
## Reliability posture

**Correction: a real, committed SLA exists** and was independently browser-read at
baseten.co/service-level-agreement - **"ninety-nine point nine percent (99.9%)"** committed
uptime for both Dedicated Inference and Model APIs, service credits capped at **40%** of monthly
fees, and a **24-hour claim window**. The public **status page** (status.baseten.co,
independently confirmed) shows all systems operational, with three brief incidents in the current
90-day window (Sep 9, 14, 20 2026), all resolved same-day or next-day.
