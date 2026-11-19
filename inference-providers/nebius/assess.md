# Assess - Nebius (Token Factory)

_Data governance, compliance, residency, security, pricing and reliability, with the provider AOI score._

<!-- item: data-governance -->
## Data governance - retention, ZDR & training

Nebius' non-binding Legal Quick Guide says "We do not use your content to train, fine-tune or
improve any AI models - ours or third parties'" and that Speculative Decoding "does not involve
training any model". The binding Token Factory Supplemental Terms Sec 5.1(b) (effective
2026-10-22) say otherwise. They let Nebius process Input and Output to "train smaller Models used
for Speculative Decoding" under royalty-free, transferable, sub-licensable, worldwide licences.
This is on by default; Sec 5.4 lets you opt out through the onboarding form or an e-mail to
tokenfactory-support@nebius.com. The legacy Terms (Sec 7) said "used exclusively for Speculative
Decoding"; Sec 5.1(b) omits "exclusively".

Sec 5.3 reserves "absolute discretion, to remove, screen, or delete any Inputs or Outputs at any
time, for any reason, and without notice." Zero Data Retention is an account-level opt-in. The
Quick Guide says enabling it also switches Speculative Decoding off and "may impact the level of
service provided (e.g., inference speed)". The contract governs, as the Quick Guide itself
states.

<!-- item: data-ownership -->
## Data & IP ownership

Supplemental Terms Sec 3.1: the customer retains ownership of Customer Content, including its
Input and Output, subject to the Sec 5.1 licence. The Services Agreement's confidentiality
clause (Sec 18) is general and mutual ("any information of the disclosing party") and does not
name Customer Data. Sec 10.1.3 limits Nebius' use of Customer Data and Customer AI Content to the
Agreement and the Service-Specific Terms, which include the Sec 5.1 licence. The DPA's
processor-confidentiality duty is scoped to Customer Personal Data. Sub-processors are fully
disclosed: 23 rows and 20 distinct entities (effective 2026-09-23) with processing locations,
transfer mechanisms and 15 days' advance notice.

<!-- item: residency -->
## Residency & sovereignty

The Nebius AI Cloud regions page lists four public EU region IDs in three countries (Finland
eu-north1, Spain eu-south1, France eu-west1 and eu-west2), with only Iceland private. That is the
GPU-cloud list. Token Factory's own documents name two EU data-plane regions, Finland (eu-north1)
and France (eu-west1), plus us-central1. Its sub-processor list gives France, Iceland, Finland and
the UK as Nebius B.V. processing locations. No Token Factory document names Spain or eu-west2.

DPA Sec 6.1 pins dedicated endpoints to the region you select, with limited processing outside it
for operation, maintenance, security or support. Public endpoints "are not region-pinned": they
show Region "Global", and their pages show processing in Finland, the UK and two US regions.

The contracting entity depends on where you are incorporated: Nebius B.V. (Dutch law), Nebius
Israel Ltd (Israeli law) or Nebius Inc. (Delaware law, JAMS arbitration). A US contracting entity
and four US-based infrastructure sub-processors make CLOUD Act exposure plausible. No primary
document addresses it.

<!-- item: compliance -->
## Compliance & attestations

A public SOC 3 report issued by Deloitte for Nebius BV (Security, Availability and Confidentiality
plus HIPAA mapping; period 2025-04-01 to 2025-07-31; dated 2025-10-19; clean opinion) lists AI
Studio, the inference platform, in its system description. An ISO/IEC 27001:2022 certificate (no.
1129086, SII-QCD, valid 2025-08-11 to 2028-08-11) covers Nebius B.V. Its scope sentence is generic,
and the trust centre states that the scope includes AI Studio (now Token Factory).

The trust centre also lists SOC 2 Type II with HIPAA (report under NDA, Deloitte), ISO 27701
(certified as PII controller and processor), ISO 42001, 22301, 27018, 27032, 27799, NIS 2 and DORA
alignment and CSA STAR Level 1 (a self-assessment). A GDPR DPA with SCCs is published. The SOC 3
period ended about 16 months ago. The SOC 2 report and the ISO 27701 and 42001 certificates are not
public, and FedRAMP is not offered.

<!-- item: security -->
## Security controls

The trust centre documents customer workload isolation (VPC, InfiniBand and Kubernetes isolation),
TLS in transit, storage encryption by default (with named exceptions), least-privilege access with
MFA, vulnerability management with automated and manual scanning and regular security assessments,
and a structured incident-response plan. DPA Annex 3 repeats the measures. Token Factory
encryption keys are Nebius-managed and customer-managed keys are not offered. No independent
penetration-test attestation or public bug-bounty programme is published.

<!-- item: pricing -->
## Pricing & cost model

Per-token prices are shown on per-model catalogue pages for models with a public endpoint, per 1M
tokens: gpt-oss-120b $0.15 input / $0.60 output, DeepSeek-V4-Pro-0813 $1.32 / $3.96, GLM-5.3
$1.40 / $4.40 and MiniMax-M3 $0.30 / $1.20, each with a cached-input rate. DeepSeek-V4-Pro,
Llama-3.3-70B-Instruct and Kimi-K2-Instruct show "Public endpoint Not available". The consolidated
price list and dedicated prices are behind a login. Dedicated endpoints are billed per running
replica, "charges may vary depending on your custom contract or work order", and the GPU-hour rate
is not disclosed.

<!-- item: reliability -->
## Reliability posture

There is no inference SLA. Supplemental Terms Sec 7.4: "Nebius does not provide any service level
commitments, uptime guarantees, or associated compensation for the Token Factory Service", with
credits excluded "unless agreed otherwise in writing". The SLA index (2026-10-06) lists eight
services (Compute Cloud, Disks, Managed Kubernetes, Managed MLflow, Managed PostgreSQL, Object
Storage, Shared Filesystem, Virtual Private Cloud) and none is inference.

Self-service dedicated endpoints "do not include a formal SLA unless covered by contract". A Token
Factory docs page says an Enterprise Tier adds an SLA, but no such terms are published. The public
status page shows all systems operational with two resolved Token Factory incidents in its 14-day
window (2026-11-05 some models unavailable in eu-north1; 2026-11-11 about eight minutes without
connectivity in tf-us2).
