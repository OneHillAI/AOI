# DeepInfra - OneHill Inference-Provider Dossier

> **Score: 61.6/100 · Grade C** · HQ: United States · EU residency: no · Trains on inputs: never
> Last verified: 2026-11-19
>
> _The Terms of Service (last modified 2026-10-15) keep Zero Data Retention contractual and controlling, and now incorporate a DPA by reference that the trust centre says includes the EU SCCs; the earlier finding of no DPA and no SCCs is out of date. The biggest caveats are that zero-retention covers only DeepInfra-hosted models - 94 of 232 public entries are partner models under the partner's terms - all processing is in the US with no EU region, and the DPA PDF and attestation documents could not be opened, so compliance rests on the provider's own trust-centre statements._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 4/5 | Contractual, controlling ZDR (Sec 7(b)) and mutual confidentiality (Sec 17) - scoped to hosted models, partner models excluded |
| Compliance & Certifications | 3/5 | DPA incorporated by Sec 5(a); ISO 27001 and SOC 2 Type 1 stated, nothing opened; BAA enterprise-only |
| Data Residency & Sovereignty | 1/5 | US-only data centres; no EU region and no choice of US region |
| Security Posture | 3/5 | Trust-centre controls and pen-test report listed but unread; SOC 2 is Type 1 |
| Reliability & SLA | 3/5 | Public status page with measured 90-day uptime; no uptime SLA |
| Transparency & Lock-in | 4/5 | OpenAI-compat + portable open models; partner models not portable |
| Cost & Value | 4/5 | Very low serverless list prices; dedicated GPU-hour rates up 59% to 75% since July |

## 1. What it serves & how it's priced

DeepInfra is a US-headquartered, low-cost provider on NVIDIA GPUs with a public catalogue of 232 entries across modalities (93 text-generation): DeepSeek V4 and V4.1, Kimi K3 and K3.1 Pro, GLM-5.x, Qwen3.5, gpt-oss, Gemma 4, Nemotron 3, Llama 3.x and more. It also lists partner models (Anthropic Claude, Google Gemini and others; 94 of 232 entries are flagged partner). Pricing is mixed: per-token list prices (for example Llama 3.1 8B Turbo $0.02 / $0.04 and gpt-oss-120B $0.037 / $0.17 per million tokens in / out, DeepSeek V4 Flash $0.09 / $0.18) with Priority (1.5x) and Flex (0.8x) tiers, plus dedicated GPUs per GPU-hour (A100 $1.49, H100 $2.90, H200 $3.49, B200 $4.89, B300 $5.89). The dedicated rates are 59% to 75% above the July record, so cost is scored 4 rather than 5.

## 2. Data governance - where your prompts go

Zero Data Retention is contractual and controlling (Terms Sec 7(b), Sec 5(a)), training is barred except as necessary to provide the Services, and Sec 17 is a mutual confidentiality duty with three-year survival (it does not name Customer Data). Exceptions are bounded: support data kept at your written request for up to 30 days after resolution, non-content metadata, legal and abuse records, and data kept for a feature you elect (batch, asynchronous media, integrations, paid cache). The reason this is a 4, not a 5: ZDR "applies to models hosted by Provider", so when you use a partner model (Anthropic, Google and others) your data is governed by **that partner's** terms, which the Terms now say in the binding text; Sec 6(a) lets new sub-processors be added without consent; and nothing independent attests the ZDR. Sub-processors are now disclosed: AWS, Google Cloud Platform and Stripe, all in the United States.

## 3. Compliance & certifications

The earlier finding of no DPA and no SCCs is out of date. Terms Sec 5(a) incorporates a DPA by reference, the trust centre lists it (dated 2026-10-05) and its FAQ says it includes the EU SCCs (Modules 1 to 3), the UK IDTA and Swiss terms, with no EU-US Data Privacy Framework certification. The DPA PDF returned HTTP 403 and was not read, so that content is a publisher statement. The trust centre shows SOC 2 and ISO 27001 as "Compliant", GDPR as "In progress" and HIPAA as "Compliant", and lists a SOC 2 Type 1 report with bridge letter, an ISO 27001 certificate and a pen-test report, none opened. The BAA needs an enterprise agreement and covers hosted models only. This meets the score-3 anchor on publisher claims.

## 4. Residency & sovereignty

All inference runs in United States data centres, for both the serverless API and dedicated deployments, with no EU or other non-US region and no choice of US region (trust-centre FAQ). The SCCs are a transfer mechanism, not residency, so residency stays at 1.

**CLOUD Act disclosure:** As a US-headquartered provider, DeepInfra is subject to US jurisdiction including the CLOUD Act. With no EU residency option, all data is under US jurisdiction. This is disclosed as standing context.

## 5. Reliability & lock-in

A public status page now exists (status.deepinfra.com) with measured 90-day uptime (API and website 100%, per-model 99.98% to 100%), a maintenance page and scheduled deprecations. There is no uptime SLA or credits; Terms Sec 4(b) offers only a 24-hour hardware replacement for provided servers. Lock-in is low for open models - an OpenAI-compatible API and portable checkpoints - but partner models are not portable and carry different data terms.

## 6. Choosing this provider - the practical guideline

DeepInfra is a strong choice when cost is the driving constraint and your data is low-to-moderate sensitivity on its own hosted open models. Do not treat it as EU-resident, and do not assume its zero-retention applies when you route to a partner model - those calls follow the partner's terms. Ask for the DPA through the trust centre before relying on the SCCs, and sign the BAA on an enterprise agreement before sending PHI.

## 7. Sources & evidence

See [`entry.yaml`](entry.yaml) and [`docs/primary-sources/deepinfra/`](../../docs/primary-sources/deepinfra/): the Terms (publisher), trust centre and FAQ (publisher, attachments unread), data-privacy docs, status page, pricing page and live model listing.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
