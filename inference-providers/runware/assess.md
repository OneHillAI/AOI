# Assess - Runware

_Should we adopt it? The data-governance, residency, compliance and security posture that
decides whether your data should flow through this provider live here. Read again 2026-09-21: the
picture improved materially from an earlier 2026-08-06 pass - see the correction notes below._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Correction (2026-09-21):** the current Terms of Service (independently re-read, two fetches
including a targeted negative search) no longer contain the broad licence-over-inputs/outputs
finding from the prior pass. Sec 3 now states, near-verbatim: *"Runware will not use your
Training Data or Trained Models to train, fine-tune, or develop Runware's own models or those of
any third party."* Combined with Sec 2 granting Runware no rights over ordinary inputs/outputs
either, nothing in the current text permits training on your data - `trains_on_inputs` resolved
from unclear to **never**.

- **Retention is still generic, not zero - unchanged.** The Privacy Policy keeps data "as long as
  necessary" and for the life of the account, with **no auto-purge and no opt-in-storage clause**.
  This remains the entry's principal residual weakness.
- **Load-bearing caveat:** the confidentiality/licence-removal finding above is *inferred* from the
  current text's absence of the old clauses - web archives were proxy-blocked this pass, so no
  verbatim old-vs-new diff was possible. High confidence given an evident deliberate rewrite, but
  flagged as inferred rather than side-by-side quoted.

<!-- item: data-ownership -->
## Data & IP ownership

**Correction (2026-09-21), reversing the prior central finding.** A 2026-08-06 pass found the
customer had nominal ownership of Generations but Runware held a worldwide, perpetual,
transferable licence over both inputs and outputs. The current Terms (independently re-read) show
this is gone: Sec 2, near-verbatim - *"As between you and Runware, you own your Outputs...
Runware asserts no ownership of, and claims no intellectual property rights in, your Outputs."*
The only licence granted to Runware is name/logo for marketing (benign). A **Private Model
Protection** clause (Sec 2) separately treats privately uploaded custom models as confidential,
with an NDA available - this was already true before the rewrite and remains a genuine positive.
The Privacy Policy still names only **Stripe and Google Analytics** as sub-processors, so the
processors that actually handle prompt content remain undisclosed. Self-hosting the same
open-weight checkpoints remains the cleanest route where data control matters most.

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
