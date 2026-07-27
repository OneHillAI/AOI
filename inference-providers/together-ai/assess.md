# Assess - Together AI

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score (75.2/100 · Grade B) -
live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Together AI's headline governance posture is **zero data retention by default**, stated in
the binding documents rather than a marketing page. The **Privacy Policy**
states that inputs and outputs are not stored by default, and that under ZDR content is not
stored, retained, or used for model training or product improvement except as needed to
provide the Services - aside from temporary caching for performance. The **Terms of Service**
add that Together does not use your data to train its models without your explicit opt-in and
consent, so training is **opt-in and off by default**, gated behind an org-admin Privacy &
Security setting.

The caveat concerns provenance of assurance: this is Together's own self-attestation in
its binding terms - strong, but **not independently audited** - and no public sub-processor
list was found. For a regulated deployment, contractualise the no-retention behaviour in the
DPA rather than relying on the default terms.

<!-- item: data-ownership -->
## Data & IP ownership

The **Terms of Service** settle ownership directly: *as between you and Company, you
exclusively own all right, title and interest in Your Content and Output*, granting Together
only a **limited license** to access, host and operate that content solely to provide the
Services. Together separately owns its own Company IP and Usage Data. Combined with
**ZDR-by-default** from the Privacy Policy - nothing retained to improve the service unless an
org admin opts in - the practical posture is that **your data and the outputs derived from it
stay yours**. The one gap is disclosure: the **sub-processor list is not published**, so for a
regulated deployment pin sub-processor terms in the DPA.

<!-- item: compliance -->
## Compliance & attestations

Together announced **SOC 2 Type II** through an independent, multi-month audit (per its own
blog - the announcement was read, the SOC 2 report itself was not obtained), and its **Data
Processing Addendum** binds it to the **EU Standard Contractual
Clauses** for EU personal-data transfers, satisfying the **GDPR DPA** requirement.
HIPAA/BAA support is *indicated* in the security docs via encryption, audit logging and
business associate agreements rather than shown as a standalone attestation, and **ISO 27001 /
27701 are unconfirmed** - the DPA aligns risk management to ISO 27005 / NIST 800-37, which is
not a 27001 certification. For healthcare or ISO-dependent procurement, request the current
attestation letters and the SOC 2 report directly.

<!-- item: residency -->
## Data residency & jurisdiction

Together's support knowledge base confirms **US and EU data centres**
(including Sweden GPU capacity) with dedicated, region-pinned endpoints; the **DPA** confirms
EU transfers run under SCCs with **default routing through North America**. The constraint is
commercial rather than technical: EU residency and dedicated/region-pinned endpoints are
**gated to the Scale and Enterprise tiers**, not available on the self-serve serverless plan.
As a US-headquartered company, Together also carries standing **US CLOUD Act exposure** even
for EU-hosted workloads - a jurisdictional fact no region setting removes.

<!-- item: security -->
## Security controls

The **security docs** and the **SOC 2 announcement** describe
**encryption in transit and at rest, audit logging, MFA/RBAC, continuous monitoring and
regular penetration testing**, and the **DPA** requires encryption of controller data in
transit and storage. No independently reviewed penetration-test report or the SOC 2 report
itself was obtained, so this is assessed as solid-but-partial: the day-to-day controls are
documented, but the deepest independent assurance is not visible.

<!-- item: pricing -->
## Pricing & cost model

Pricing is **mixed**: per-token serverless rates for the shared catalogue plus **dedicated
GPU endpoints** on Scale/Enterprise. Together's pricing page lists the models, and indicative
serverless rates corroborated by **independent third-party price analysis** - gpt-oss-120B
~$0.15/$0.60 per M in/out, Qwen3-235B ~$0.20/$0.60, DeepSeek-V3 ~$1.25/M - are **approximate
and move frequently** (the live pricing page was not read from source), so treat
them as an order-of-magnitude guide and confirm live rates before committing.

<!-- item: reliability -->
## Reliability posture

No incidents surfaced in research, but **no public uptime SLA, status page or failover
documentation was found or independently verified**. Reliability is therefore
assessed conservatively: adequate on available evidence, but without an observable status/SLA
record to lean on for availability-critical workloads.
