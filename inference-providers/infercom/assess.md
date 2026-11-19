# Assess - Infercom

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Zero content retention is the default and is set out in three binding documents. The Privacy
Statement (v2.4, 2026-10-30) says "Infercom does not store, log, or retain the content of your
prompts or model outputs" and that it does not use inference data for "model training,
fine-tuning, or service improvement", for both EU-hosted models and the Global Model Catalog.
The Terms (v2.1) repeat the no-training commitment and add that Input and Output are used for
no purpose other than delivering the response.

Usage logs hold metadata only (timestamps, model identifiers, token counts, response times,
error codes, API key identifiers) for 90 days. Authentication logs are kept 12 months. The DPA
(v1.4, 24 September 2026) adds that personnel have no access to prompt content in the ordinary
course and that sub-processors may not train either.

Two limits matter. The DPA covers EU-hosted models only. For Non-EU Models it requires a
separate written addendum, so the Global Catalog's no-store commitment rests on the Privacy
Statement and Terms alone. And confidentiality is only functional: the Terms contain no clause
making inputs confidential, so trade secrets need an NDA or the enterprise contract.

<!-- item: data-ownership -->
## Data & IP ownership

Your data and the knowledge derived from it stay yours. Terms v2.1 Sec 6 say you keep all
rights in Input and Output and grant only a limited licence to process them to provide the
Services. Nothing is retained or used to improve the service, and only open-weight models are
served, so no closed-model vendor terms attach.

Sub-processors are named, but in two lists that do not match. The Privacy Statement names
SambaNova, Auth0, Stripe, Metronome (US) and TECLIB, while the DPA names SambaNova, Google
Ireland, Pipedrive, Stripe and TECLIB. Ask which list governs before signing. SambaNova's own
further sub-processors are available on request only.

<!-- item: residency -->
## Data residency & jurisdiction

Pin EU-hosted models to get EU sovereignty, and note the operator caveat. EU-hosted models run
on Infercom-owned hardware at Equinix Munich 4 and, under DPA v1.4, are processed exclusively
in the EU/EEA with no fallback, overflow or load-balancing routing outside it.

The Global Model Catalog (one model today, MiniMax-M3.1-Flash) is different. The Privacy
Statement says prompt content "is routed to SambaNova's global infrastructure outside the EEA,
primarily in the United States" under SCCs, and the DPA excludes those models.

The other limit is the operator. The Terms (Sec 2.1) say SambaNova Systems, Inc., a US company, "operates the platform
under a managed services agreement", and the DPA (Sec 7a) gives it
remote administrative access to account identifiers and request metadata under SCCs Module
Three. The Trust Centre FAQ says SambaNova has "operational access to the Munich facility".

The docs and pricing pages claim EU sovereign models have "no US CLOUD Act exposure". No
binding document makes that claim, and the US operator relationship leaves it open, so it is
marketing. Ask for the Transfer Impact Assessment (DPA Sec 7a(4)), or choose Dedicated Capacity
or on-premises if operator access matters.

<!-- item: compliance -->
## Compliance & attestations

ISO 27001:2022 is independently certified. The certificate (Proks Certification GmbH, No
LU-IS-20250253, scope "AI & Cloud Infrastructure Services (Inference as a Service)", valid
2025-12-16 to 2028-12-15) covers the hosted service. The Cloud Security Alliance listing is
STAR for AI Level 1, a self-assessment (AI CAIQ v1.1.0), not an audit.

The Trust Centre says SOC 2 is "Not
yet". The SOC 2 and ISO 22301 badges on that page belong to
the Equinix MU4 facility, not to Infercom. An Art. 28(3) GDPR DPA is available and incorporated
by the Terms on acceptance. ISO 27701 and HIPAA/BAA are not offered.

<!-- item: security -->
## Security controls

Security rests on the ISO 27001-certified ISMS and the controls binding in DPA v1.4 Annex 1:
TLS 1.2 or higher in transit (TLS 1.3 supported), AES-256 at rest per the Privacy Statement,
stateless in-memory processing, hardware-level tenant sandboxing, MFA, least privilege, access
logging, DDoS protection and automated failover. Breach notification to the customer is within
48 hours.

The controls are solid but not top-rated. No independent penetration-test report or
bug-bounty programme is published (vulnerabilities go to dpo@infercom.ai), there is no private
connectivity, and physical controls sit with the Equinix facility and the US operator.

<!-- item: pricing -->
## Pricing & cost model

Per-token rates are published in EUR, excluding VAT: gpt-oss-120b 0.22 in and 0.59 out, Gemma 4
31B 0.20 and 0.35, Whisper Large v3 0.10, E5-Mistral 7B embeddings 0.13, and the Global-catalog
MiniMax M3.1 Flash 0.60 and 2.40 per 1M tokens. There are no minimums or commitment, and new
accounts get EUR 5 credit that expires after 30 days. Dedicated Capacity and On-Premises are
priced per engagement. The Terms let Infercom change pay-as-you-go prices on posting, so
confirm live rates before committing.

<!-- item: reliability -->
## Reliability posture

There is a public status page, but no SLA for pay-as-you-go. status.infercom.ai (an Atlassian
Statuspage, live since 2025-12-31) shows per-model components and one public incident: a major
gemma-4-31B-it problem on 2026-06-19, resolved about 21 hours later.

The Terms (Sec 8.2) give SLAs with uptime commitments only to Reserved Capacity and Dedicated
Rack customers under separate agreement, and that text is not public. The speed claims (up to
10x versus GPUs) are vendor figures.
