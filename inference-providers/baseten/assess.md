# Assess - Baseten

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Baseten's **Security Practices** (Last Updated 2026-11-12) say Baseten "adheres to a Zero Data
Retention posture" for **Model APIs** and **Dedicated Inference** and will not "store, retain, or
otherwise make a persistent copy of model inputs or outputs". The docs add that Dedicated
Inference synchronous requests "run under ZDR by default". The Security Practices do not say "ZDR
is the default configuration". A **Customer-Controlled Factors** clause says Baseten is not in
breach of the ZDR commitments where retention follows from customer configuration, customer
runtime code, a customer-enabled Third-Party Product or a written customer direction. Terms Sec
2.5 and DPA Sec 4.5 tie the commitment to that ZDR designation. **Async Inference** (an elective
Dedicated Inference feature) queues inputs for up to **72 hours** before deletion, and outputs are
never stored. Terms Sec 6.3 bars Baseten from using **Customer Content - including deployed model
weights, outputs and inference logs -** to train, fine-tune or otherwise develop models.

<!-- item: data-ownership -->
## Data & IP ownership

Terms & Conditions Sec 6.1: **"Customer reserves all rights, title, and interest in and to
Customer Content,"** a definition that includes deployed **Customer Models** and **Model
Outputs**. A **mutual confidentiality clause** (Sec 11.1-11.2) names Customer Content and Customer
Models and requires both parties to protect confidential information **"with the same degree of
care it uses for its own (but no less than reasonable care),"** surviving **three years** after
termination (trade secrets indefinitely, Sec 11.4). Most peers do not match this. The DPA gives 15
days' notice of new sub-processors (Sec 7.1) and a ten-day objection right. The list at
trust.baseten.co has 13 rows, and six cloud-compute additions since August sit behind a gated
compute-providers PDF.

<!-- item: residency -->
## Residency & sovereignty

The Regional deployments docs publish an **EU region** (`eu`, next to `us`), selectable per GPU
model deployment through the CLI or Management API, with a regional endpoint. **Model APIs** use a
shared endpoint whose serving regions "can change", so staying in specific regions needs a
compliance policy enabled by support. Chains and training jobs cannot select a region. The docs
do not say where the Baseten-operated control plane runs. **Baseten Self-Hosted** (Enterprise) is
the stronger path, running the whole workload plane inside the customer's own VPC.

**CLOUD Act disclosure:** Baseten is US-headquartered (San Francisco). Standard US jurisdiction
applies to the managed service, including a deployment pinned to the EU region.

<!-- item: compliance -->
## Compliance & attestations

**SOC 2 Type II** is confirmed on the Security Practices (named audit firm Sensiba San Filippo LLP
on the vendor's blog), as are **HIPAA** (BAAs with qualifying customers) and a **GDPR DPA**. The
Vanta Trust Center renders only in a browser. It labels **ISO 27001:2022**, **PCI DSS SAQ D**,
CCPA and GDPR next to SOC 2 and HIPAA, and its updates feed announced the ISO 27001 certification
on 2026-08-24. Pages readable without JavaScript show no trace of ISO 27001. The certificate, the
5.31.26 SOC 2 and SOC 3 reports, the HIPAA report and the PCI attestation are all behind "Request
access", so they are vendor claims and the compliance score is 4. ISO 27701 and CSA STAR are not
listed. A FedRAMP 20x package is listed but is not an authorisation.

<!-- item: security -->
## Security controls

Isolation is logical namespace separation for shared use (access controls, unique customer
identifiers) plus **Dedicated** single-tenant Kubernetes namespaces with Calico and Cilium network
policies ("Baseten never shares GPUs across users") and **Self-Hosted** deployment inside the
customer's own VPC. Encryption is **TLS 1.2+** in transit (mTLS between clusters) and **AES-256**
at rest. Access is **least-privilege with enforced MFA** for all personnel, with quarterly access
reviews. Customers are notified of an unauthorised disclosure within **48 hours**. The Security
Practices say Baseten engages qualified third-party firms for periodic penetration testing, and
the docs say annually. The trust centre lists an October 2026 test report that is gated. No public
bug-bounty programme was found. By default a deployment can reach any internet host unless the
customer configures egress restrictions.

<!-- item: pricing -->
## Pricing & cost model

Per-token pricing for hosted Model APIs and per-GPU-minute pricing for dedicated deployments are
both published on Baseten's pricing page, with pay-as-you-go and "Production scale" routes and
published default rate limits. Example rates per 1M tokens (input / cached / output): GLM-5.3
$1.40 / $0.14 / $4.40; DeepSeek V4.1 Flash $0.30 / $0.007 / $1.20; Kimi K3.1 Pro $2.00 / $0.20 /
$10.00. Dedicated GPU-minute rates run from T4 $0.01052 up to H100 80GB $0.10833 (about $6.50 an
hour) and B200 $0.16633.

<!-- item: reliability -->
## Reliability posture

The SLA at baseten.co/service-level-agreement (stamped 2026-09-15) is a "commercially reasonable
measures" undertaking to reach **99.9%** monthly availability for Dedicated Inference and Model
APIs on Baseten-managed infrastructure. Service credits are 10/15/30%, capped at **40%** of
monthly fees, with a **24-hour claim window**. It is not an unqualified guarantee. The public
**status page** shows all systems operational and logs **7 major or critical incidents between
2026-09-20 and 2026-11-18**, all resolved. They include an 11 h 45 min regional event on
2026-09-29 and a 21-minute outage of all Model APIs on 2026-11-11.
