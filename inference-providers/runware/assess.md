# Assess - Runware

_Should we adopt it? The data-governance, residency, compliance and security posture that
decides whether your data should flow through this provider live here. The binding documents were
read on 2026-07-26 and they matter: they do not match the marketing._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Read from the binding Terms and Privacy Policy (Runware Ltd, UK), the posture is **weak**, and it
contradicts the marketing.

- **Retention is generic, not zero.** The Privacy Policy keeps data "as long as necessary" and for
  the life of the account. There is **no auto-purge and no opt-in-storage clause**, contrary to the
  marketed "generated content is auto-purged unless you opt into storage".
- **No no-training commitment.** The Privacy Policy **does not address training** at all, and the
  Terms reference **"storing training data and models."** Nothing in the binding text stops training
  on your data.

<!-- item: data-ownership -->
## Data & IP ownership

This is the central finding. Per the read **Terms**, the customer owns the "Generations" (outputs),
**but grants Runware a worldwide, perpetual, transferable licence over both inputs and outputs.**
Nominal ownership sits with you; a perpetual, transferable right to use your prompts and your
generated content sits with Runware. That is the opposite of "your data belongs to you and is never
reused". The Privacy Policy names only **Stripe and Google Analytics** as sub-processors, so the
processors that actually handle prompt content are not disclosed. The one clean escape is to
**self-host the same open-weight checkpoints**, which removes Runware from the data path entirely.

<!-- item: residency -->
## Data residency & jurisdiction

The Trust page advertises **"EU & US"** data residency, but **no contractual region-pinning
document** was found, and US CLOUD Act is not addressed anywhere located. The binding legal entity
is **Runware Ltd (United Kingdom)** under UK law and London arbitration, even though the company
markets a US (San Francisco) HQ. EU residency is advertised, not guaranteed, so treat this as a
UK-jurisdiction provider without a sovereign, EU-only option.

<!-- item: compliance -->
## Compliance & attestations

**SOC 2** and **ISO 27001** appear as **badges on the Trust page with no readable report** (no
number, issuer, scope, type, or period). **No public DPA** was located (both `runware.ai/dpa` and
`runware.ai/data-processing-agreement` returned 404, so it is likely enterprise-only). GDPR/UK GDPR
is cited **without naming SCCs or the EU-US Data Privacy Framework**. Request a DPA and the actual
attestation reports before any regulated use.

<!-- item: security -->
## Security controls

The Trust page carries the SOC 2 / ISO 27001 badges and there is a dedicated
vulnerability-disclosure page; models run on Runware's own Sonic Inference Engine hardware. Held
short of a strong rating absent a readable attestation report or an independent penetration test.

<!-- item: pricing -->
## Pricing & cost model

Pay-as-you-go, usage-based pricing with representative rates read on the pricing page; enterprise
plans add dedicated capacity and custom terms.

<!-- item: reliability -->
## Reliability posture

A **USD 50M Series A** (December 2025) and advertised enterprise **custom SLAs** point to
production scale, but no public uptime SLA or status page was found, so availability is asserted
rather than independently observable.
