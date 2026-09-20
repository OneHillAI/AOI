# Assess - Nebius (Token Factory)

_Should we route our data through this provider? Data governance, compliance, residency,
security, pricing, and reliability - plus the provider AOI score - live here._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

**This is the entry's central finding, and an independent Cowork browser session (2026-09-21)
CONFIRMED it VERBATIM.** Nebius' marketing-adjacent **Legal Quick Guide** states **"we do not use
your content to train, fine-tune or improve any AI models - ours or third parties'."** But the
**binding Token Factory Terms of Service, Sec 7** (independently re-read) states Nebius
**collects and processes Input/Output data by default** and uses it to train its own smaller
**"Speculative Decoding"** models, unless the customer actively **opts out** (via an onboarding
form or by emailing support). **Zero Data Retention is an account-level opt-in**, not the
default - and the Legal Quick Guide itself warns that enabling it **"may impact the level of
service provided (e.g., inference speed)."** This finding survives independent human-grade
verification, not just an automated read - it is real.

<!-- item: data-ownership -->
## Data & IP ownership

Terms of Service Sec 10(b)/(c) (independently re-read): the customer **"holds exclusive ownership
of all rights, titles, and interests... to Customer's Content,"** subject to the Sec 7 operational
licence described above. Sec 7 separately reserves the right to **"remove, screen, or delete any
of Your Inputs and Outputs at any time, for any reason, and without notice."** Neither the general
Master Agreement confidentiality clause (Sec 18) nor Sec 7 names Customer Content as the
customer's own Confidential Information; the DPA's processor-confidentiality duty is scoped to
**Customer Personal Data**, not Customer Content generally. Sub-processors are fully disclosed:
approximately **21** named entities (corrected from an earlier ~24; exact recount recommended)
with a 15-day advance-notice commitment.

<!-- item: residency -->
## Residency & sovereignty

**Correction:** only **two** EU regions are public/self-serve - Finland (eu-north1) and France
(eu-west1). Spain (eu-south1) and Iceland (eu-north2), plus a second French region (eu-west2),
are **private** - "available only to the users who already have deployments there," not
self-serve. An earlier draft claimed four public EU regions; an independent browser read of the
regions page corrected this. The DPA documents **region pinning** for AI Cloud and Token Factory
**dedicated** endpoints, but for **shared/public** Token Factory endpoints - the self-serve,
majority-usage surface - processing location **"may vary."** A US sub-processor entity (Nebius
Inc.) and a `us-central1` public region exist alongside the Netherlands-domiciled parent (Nebius
Group N.V.), creating plausible CLOUD Act exposure that no primary document addresses explicitly.

<!-- item: compliance -->
## Compliance & attestations

Nebius' **Trust Center and SOC 2 blog post** (independently browser-read, verbatim) document
**SOC 2 Type II audited by a NAMED firm - Deloitte -** covering HIPAA, and an **ISO 27001** scope
statement that explicitly names **"AI Studio"** (Token Factory itself, not just the company
generally) alongside AI Cloud and TractoAI. A **GDPR DPA** and **CSA STAR Level 1** are also
documented. The underlying SOC 2 report still requires an NDA and discloses no public audit
dates - compliance remains publisher-grade + named auditor, short of an independently-dated
public certificate. FedRAMP is not offered.

<!-- item: security -->
## Security controls

The Legal Quick Guide references **encryption at rest and in transit** and **need-to-know access
management**, and dedicated endpoints are marketed as single-tenant/isolated. This language is
generic - no cipher specifics, no independently confirmed penetration-testing programme, and no
public bug-bounty were found. SOC 2 Type II implies some independently tested operational
controls, but that is not the same as a named pen-test disclosure.

<!-- item: pricing -->
## Pricing & cost model

Public per-token pricing is verified directly and on re-check for several live **public
endpoints** - DeepSeek-V4-Pro at $1.75/$3.50 per 1M tokens, gpt-oss-120b at $0.15/$0.60,
Llama-3.3-70B-Instruct at $0.13/$0.40. **Correction:** a prior claim that several flagship models
(Kimi-K2-Instruct, Llama-3.3-70B-Instruct, GLM-4.5) showed "Public endpoint: Not available" is
not supported on re-check - those specific named versions have simply been **superseded** by
newer catalogue entries (ordinary churn), not gated behind a dedicated tier. The dedicated tier's
underlying per-replica/GPU-hour rate remains **not disclosed**, described only as varying
"depending on your custom contract or work order," and the full authoritative live price list is
auth-gated.

<!-- item: reliability -->
## Reliability posture

**Correction: there is NO committed inference SLA at all.** A prior draft claimed a real
contractual SLA existed with only the exact number unconfirmed - this overstated it. The master
SLA page (independently re-read) delegates entirely to per-service sub-pages; that index lists
exactly **seven** services (Compute Cloud, Managed Kubernetes, Managed MLflow, Managed
PostgreSQL, Object Storage, Standalone Applications, Virtual Private Cloud) and **none of them is
inference, Token Factory, or AI Studio**. The marketed 99.9% figure is confirmed marketing-only.
A public **status page** (independently confirmed) shows a dedicated Token Factory component as
Operational, with three brief, resolved incidents in the Sep 9-17 2026 window.
