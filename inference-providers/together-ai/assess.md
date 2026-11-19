# Assess - Together AI

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score (69.6/100, grade C) - live
here. Re-verified 2026-11-19 against the live Terms, Privacy Policy, DPA PDF and product docs._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**Together stores your prompts by default and may use them for product improvements; zero data
retention is an opt-in.** The product docs say so directly: "By default, Together stores the
prompts you send and the responses models return, and may use them for product improvements."
An organisation admin turns off Prompt storage in Privacy settings to enable ZDR, and ZDR applies
only to requests after it is enabled. Under ZDR request content is not persisted, but request
metadata, account data and files you uploaded for fine-tuning or batch jobs are still retained.
Training on your data is a separate opt-in that is off by default (Privacy Policy Sec 1 and 2.2).
A second default matters: **passthrough models are ON**, meaning some models forward your prompts
and responses to an upstream provider that handles them under its own data policy; turning ZDR
on switches passthrough off. All of this is Together's own statement and has not been audited.
Terms Sec 9 adds that "The parties will have no confidentiality obligations to each other unless
otherwise agreed in writing", which caps this dimension at 3.

<!-- item: data-ownership -->
## Data & IP ownership

The **Terms of Service** (Sec 7, updated 2026-05-19) settle ownership: *as between you and
Company, you exclusively own all right, title, and interest in Your Content and Output*, with a
limited licence to operate them "solely as necessary to provide the Services". Together owns
Usage Data (aggregated or de-identified technical data it may use to improve and develop
services). Two limits: by default stored prompts may be used for product improvements (see above,
and this sits awkwardly with the narrow licence), and passthrough models place your data under a
third party's policy. The DPA's Annex III names nine sub-processors, including OpenAI OpCo, LLC
for "Generative AI"; Annex 1 scopes the DPA around account and employee data, so confirm how
personal data inside prompts is covered.

<!-- item: compliance -->
## Compliance & attestations

Together announced **SOC 2 Type II** (blog, 2025-07-08, auditor not named) and **ISO 27001:2022**
from A-LIGN, an ANAB-accredited body (blog, 2026-06-10). Both are vendor announcements: neither
the SOC 2 report nor the ISO certificate was read, and the trust centre where they are available
is a JavaScript-only page that could not be read. A **GDPR DPA** with EU SCCs and the UK Addendum
is published as a PDF. HIPAA and BAAs are stated in the SOC 2 blog, yet ToS Sec 4 forbids sending
"financial or medical information" or sensitive personal data under the standard terms, so
obtain a signed BAA and enterprise terms before sending PHI. ISO 27701 is not claimed.

<!-- item: residency -->
## Data residency & jurisdiction

**Serverless has a US-only guarantee and no EU option.** The docs offer one region control:
send requests to `us-api.together.ai` (1.25x the standard rate, 8 models) to keep inference
processing in the US. That guarantee "doesn't cover where data is stored, where logs are written,
or how network traffic is routed", and requests to `api.together.ai` "do not guarantee US
processing". EU residency means a dedicated endpoint or VPC deployment arranged with sales; the
support article that says so is a year old and gates it to Scale and Enterprise tiers, which the
rate-limit docs now call legacy contracts. As a US-headquartered company Together also carries
standing **US CLOUD Act exposure** that no region setting removes. Correction: an earlier version
of this entry said the DPA confirms default North America routing; that sentence is not in the
DPA PDF, and the nearest statement is the docs line that DeepSeek models are hosted in North
America data centres.

<!-- item: security -->
## Security controls

The DPA's Annex 2 commits Together to a written security programme, MFA for remote access,
encryption of controller data in transit and storage, **daily vulnerability scans, annual external
penetration tests, 30-day remediation of critical findings** and USD 2 million of cyber insurance.
Vulnerability reports go through a private HackerOne programme. The SOC 2 and ISO announcements
describe independent audits. No penetration-test report, SOC 2 report or ISO certificate was read,
so this stays solid-but-partial. The docs line "models are hosted at full precision" is
contradicted by the catalogue's FP4, FP8, NVFP4 and MXFP4 column, so read marketing claims on
that page with care.

<!-- item: pricing -->
## Pricing & cost model

Read live on 2026-11-19. **Serverless per-token rates** with cached-input prices for 24 chat
models, for example gpt-oss-120B $0.15 in and $0.60 out, DeepSeek V4.1 Flash $0.30 and $1.20, GLM-5.3
$1.40 and $4.40, Kimi K3.1 Pro $2.00 and $10.00, MiniMax M3.1 Flash $0.15 and $0.60 per 1M tokens.
US-only processing costs 25% more. **Dedicated** single-tenant GPUs are billed on demand per GPU
hour (H100 $5.49, H200 $5.99, B200 $9.29), GPU Clusters from $3.99 an hour for H100, and
provisioned throughput is sold through sales. Rates and promotions (Qwen4 Max to 2026-11-23) move
often, so confirm before committing.

<!-- item: reliability -->
## Reliability posture

**A public status page exists and shows per-model uptime, but there is no self-serve SLA.**
status.together.ai reports 90-day availability from 99.28% (Kimi K3) to 100%, for example
gpt-oss-120B 99.66% and GLM-5.3 99.91%. Its feed has two 2026 maintenance notices and no incident
posts since January 2025. The Terms (Sec 1) give "no guarantees ... uptime, or reliability" unless
an order form says otherwise, the docs call serverless "best-effort", and a defined SLA comes only
with provisioned throughput through sales. (The earlier entry said no status page existed; that
was wrong.)
