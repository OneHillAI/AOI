# Assess - Runware

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

The Terms were last updated on 29 September 2026.

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Training: none. Terms Sec 3 says "Runware will not use your Training Data or Trained Models to train, fine-tune, or develop Runware's own models or those of any third party", and Sec 4 (Serverless) says the same for Customer Material. The docs add that API data is never used to train, with or without zero data retention. Nothing in the current Terms permits training on ordinary inputs either.

Retention on the managed API is generic and not zero. The Privacy Policy (Sec 6) keeps data "as long as necessary" and no longer than the account lifetime, with no numeric window, no auto-purge and no opt-in-storage clause. Terms Sec 2 says Runware "does not retain your Outputs on a long-term basis", and the docs say output URLs last 7 days.

Zero data retention exists, with limits. It is an organisation-level option for enterprise accounts, switched on by Runware staff on request, applying only from that moment and covering a listed set of models. It appears in the docs and not in the Terms or Privacy Policy.

Closed partner models change the picture. The catalogue includes models licensed to Runware by their owners. When a provider runs the model, the docs say that provider's own retention terms apply to its copy (for example HeyGen keeps request data for 24 hours).

The July and August 2026 versions of the Terms carried a broad licence over inputs and outputs, and the current text has none. No archived copy of the earlier text is readable, so no verbatim comparison exists.

<!-- item: data-ownership -->
## Data & IP ownership

Terms Sec 2: "As between you and Runware, you own your Outputs ... Runware asserts no ownership of, and claims no intellectual property rights in, your Outputs" and "Runware takes no licence in your Outputs." Trained Models and Serverless Customer Material are also yours. The only licence granted to Runware is the use of your company name and logo for marketing, revocable on request. The earlier Terms text granted a worldwide, perpetual, transferable licence over inputs and outputs.

Confidentiality is express in two places only: privately uploaded models (Sec 2, "whether or not an NDA has been signed") and Serverless Customer Material (Sec 4). Prompts and outputs on the managed Models API have no stated duty of confidence, so protection there comes from the absence of any licence.

The Privacy Policy names only analytics and payment tools (Google Analytics, PostHog, Meta Pixel, LinkedIn Insight Tag, Umami, Stripe), so the infrastructure processors that handle prompt content are undisclosed. Self-hosting the open-weight checkpoints is the cleanest route where data control matters most.

<!-- item: residency -->
## Data residency & jurisdiction

Marketing and binding text disagree. The help centre says all data is "stored on secure, EU-based servers". Terms Sec 16 says "the Services are hosted in the United States, Germany and Romania." The Terms govern.

There is no customer-selectable region and no contractual pinning, and US CLOUD Act reach is not addressed. The binding entity is Runware Ltd, United Kingdom, under English law with arbitration seated in London, but hosting is partly US and the site footer names "Runware, Inc.". Runware is a UK-jurisdiction provider with EU and US hosting and no sovereign option.

<!-- item: compliance -->
## Compliance & attestations

SOC 2 and ISO 27001 appear only as footer badges with no report, number, issuer, scope, type or period, and trust.runware.ai is a JavaScript-only page that cannot be read. A DPA is available through the enterprise agreement process according to the help centre (the public `runware.ai/dpa` URL returns 404), and its text is unread.

The Terms (Sec 1) state the Services are not tailored to HIPAA or FISMA and bar their use where those laws apply. The Privacy Policy cites GDPR and UK GDPR without naming SCCs or the EU-US Data Privacy Framework. Request the DPA and the attestation reports before any regulated use.

<!-- item: security -->
## Security controls

There is a responsible-disclosure programme with safe harbour and a 5-business-day acknowledgement target; Runware states it is not a public bug bounty. The Terms add a Serverless clause under which Runware may scan workloads and isolate compromised ones, and the footer lists enterprise SSO/SAML and configurable MFA. The rating stays short of strong because no attestation report or independent penetration test is readable.

<!-- item: pricing -->
## Pricing & cost model

Pay-as-you-go published rates cover 420 models across image, video, audio, text and 3D, billed per generation, per second or per million tokens. Per-second serverless GPU rates (L40s to B300) come with reserved starting prices. New business sign-ups get $2 of free credit. Community models carry no public price. Enterprise plans add custom terms.

<!-- item: reliability -->
## Reliability posture

A public status page exists at status.runware.ai. On 2026-11-19 it reported "fully operational" and, for August to November 2026, 99.93% uptime for Models (Third-party Models 99.98%) and 99.90% for Serverless. The Terms disclaim availability (Sec 18) and contain no SLA or service credits. Custom SLAs are advertised for enterprise plans only.
