# Assess - Infercom

_Should we route our data through this provider? Data governance, data & IP ownership,
residency, compliance, security, pricing, and reliability - plus the provider AOI score -
live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Zero data retention, set out in a binding Privacy Policy:** the Privacy Policy states in terms
that "Infercom does not store, log, or retain the content of your prompts or model outputs" -
inference data is processed transiently and the content discarded - that Infercom "does not use
inference data for model training, fine-tuning, or service improvement" (both EU-Hosted and
Global Catalogue), and that usage logs hold **metadata only** - timestamps, model identifiers,
token counts, response times, error codes, API key identifiers, **not prompt/response content** -
for **90 days**. These clauses are read directly from the Privacy Policy, so the posture is contractual rather than
marketing. A GDPR **Art. 28(3) DPA (v1.3)** sits on top - its Art. 28(3) nature, Luxembourg party
and 2026-03-04 effective date are confirmed, though the PDF's full clause text is documented but
unverified (unreadable behind the proxy). The catalogue is open-weight only, so no
closed third-party model's data terms attach. One scope caveat separates cleanly from retention:
the no-storage/no-training posture is uniform, but **residency is not** - see the jurisdiction
item, where the default Global Model Catalogue routes non-EU-hosted models' prompts to the US.
Sub-processors are not individually disclosed.

<!-- item: data-ownership -->
## Data & IP ownership

**Your data and the knowledge derived from it stay yours.** The Privacy Policy and DPA state
that data is not retained after inference, prompts are never used for training or service
improvement, and Infercom serves **open-weight models only** - nothing is captured to improve
the service and no closed-model vendor terms attach. Two caveats: the **sub-processor list is
not disclosed**, and while ownership of your data holds across the catalogue, its **location does
not** - non-EU-hosted models route prompt content to the US (see jurisdiction). Sign the DPA and
pin EU-hosted models.

<!-- item: residency -->
## Data residency & jurisdiction

**Pin EU-hosted models to get EU sovereignty - it is not automatic.** EU-hosted models run in
Munich (Equinix) under EU jurisdiction, stay in the EEA, and carry **no US CLOUD Act / PATRIOT
Act exposure**. But Infercom's own Privacy Policy is explicit that the default **Global Model
Catalogue** also serves non-EU-hosted models whose **API requests, including prompt content, are
routed to SambaNova's global infrastructure outside the EEA - primarily the United States** -
under Standard Contractual Clauses / EU-US Data Privacy Framework. Sovereignty is therefore a
**per-model choice**, not a blanket property: pick EU-hosted models and the extraterritorial
switch-off risk is effectively removed; use the Global Catalogue and your prompts can leave the
EU under US jurisdiction.

<!-- item: compliance -->
## Compliance & attestations

Infercom is **ISO 27001 certified** and has **completed the Cloud Security Alliance's AI
security assessment (CSA STAR / AI CAIQ)**, covering model governance, data handling and
security controls. It aligns with **GDPR, the German BDSG, and the EU AI Act**. This is a
genuinely strong, independently attested compliance posture for an EU adopter - the ISO
certification is corroborated by third-party partnership announcements. **SOC 2, ISO 27701 and
HIPAA/BAA** status are not confirmed; request those directly if your procurement requires them.

<!-- item: security -->
## Security controls

Security rests on **ISO 27001-certified security management**, a **completed CSA AI security
assessment**, and **encryption in transit**. This is stronger independent assurance than most
newly launched providers offer. It is assessed as solid-but-partial only because the platform
is **newly launched** and no independent penetration test beyond the ISO/CSA scope was
surfaced.

<!-- item: pricing -->
## Pricing & cost model

Pricing is **pay-as-you-go** for OpenAI-compatible inference. Exact per-model rates were **not
confirmed** in the public sources reviewed, so treat the cost model as
transparent-in-shape but **confirm live per-model rates** with the provider before committing.

<!-- item: reliability -->
## Reliability posture

The underlying **SambaNova RDU dataflow** architecture is claimed to deliver up to **10x faster
inference and 5x better energy efficiency** than GPU alternatives. However, the platform is
**newly launched** (first datacenter late 2025) and **no public uptime SLA or history was
independently verified**, so reliability is assessed conservatively pending an observable
track record.
