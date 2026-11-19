# Groq - OneHill Inference-Provider Dossier

> **Score: 72.4/100 · Grade B** · HQ: United States · EU residency: yes (Finland and London capacity, no pinning clause) · Trains on inputs: never
> Last verified: 2026-11-19
>
> _Right for latency-sensitive workloads on a curated open catalogue; the biggest caveat is that batch and fine-tuning features retain data and default to US storage._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 4/5 | Inference not retained by default (30-day abuse logs unless ZDR); batch/fine-tune retain to US |
| Compliance & Certifications | 4/5 | DPA and BAA published; SOC 2 Type II is a claim (trust centre unreadable); ISO 27001 unconfirmed |
| Data Residency & Sovereignty | 3/5 | EU capacity exists (Finland, London) but no pinning clause; retained data in US GCP |
| Security Posture | 4/5 | SOC 2 Type II controls + Data Controls for ZDR |
| Reliability & SLA | 3/5 | Public status page, 100% API uptime Aug-Nov 2026; no published SLA |
| Transparency & Lock-in | 3/5 | OpenAI-compat + open models, but custom LPU + narrower catalogue |
| Cost & Value | 4/5 | Low per-token rates plus a rate-limited free tier |

## 1. What it serves & how it's priced

Groq runs open models on its custom LPU hardware, optimised for very low latency. The catalogue is curated, narrow and fast-changing: gpt-oss 120B and 20B and Whisper in production; Qwen3.8-27B, gpt-oss-safeguard, Orpheus TTS and Prompt Guard in preview. Llama 3.1 8B and 3.3 70B were retired for free and developer tiers on 2026-08-16 and are now enterprise-contract only. The DeepSeek R1 distill, Gemma, Mixtral and Qwen3-32B models are gone. Full DeepSeek, GLM, Mistral and arbitrary fine-tunes are not available, a coverage limit against NVIDIA-GPU providers. Pricing is per-token with a rate-limited free tier, taken from the docs models page (groq.com/pricing redirects to the home page): gpt-oss-120B $0.15/$0.60, gpt-oss-20B $0.075/$0.30, Qwen3.8-27B $0.80/$4.00.

## 2. Data governance - where your prompts go

Standard inference is not retained by default. According to the docs, ZDR is available to all customers via Data Controls, though the Services Agreement says "Eligible Customers", a term it never defines. This is a stronger baseline than enterprise-only ZDR. The docs also say inputs and outputs may be logged for up to 30 days when Groq troubleshoots errors or investigates abuse, unless ZDR is on. The Services Agreement (last modified 2026-06-22) bars Groq from using Inputs or Outputs for training and has a mutual confidentiality clause naming Customer Data.

The caveats are in the ancillary features. Batch processing retains input/output files for 30 days unless deleted, and fine-tuning retains weights and datasets until the customer deletes them. This retained-feature data is stored in US GCP buckets. There is no closed third-party model routing. The DPA points to a sub-processor list at trust.groq.com/subprocessors, which is JavaScript-only and unreadable.

## 3. Compliance & certifications

The DPA (GDPR, UK and Swiss transfers via deemed-signed SCCs) and a HIPAA BAA (generally available services only) are published. SOC 2 Type II is a trust-centre claim (2025 report), and trust.groq.com is JavaScript-only, so the claim is unconfirmed. ISO 27001/27701 is unconfirmed. The posture is solid but short of the top anchor, because the ISO attestation is missing and the SOC 2 report is gated.

## 4. Residency & sovereignty

Groq launched an EU data centre in Helsinki, Finland (with Equinix) in July 2025, and its platform page lists EU-1 Vantaa (Finland) and EU-2 London. This satisfies the "EU region available" anchor. Retained data is stored in US GCP buckets, the DPA permits US processing, EEA customers contract with Groq UK Limited, and region pinning is unconfirmed.

CLOUD Act disclosure: as a US-headquartered provider, Groq is subject to US jurisdiction including the CLOUD Act, even for EU-hosted data. This is standing context and is not scored as a defect on its own.

## 5. Reliability & lock-in

Groq has a public status page (groqstatus.com) showing 100% uptime for the API and production models from August to November 2026. No SLA is published, so reliability is 3. The OpenAI-compatible API and open-weight models keep workloads portable at the API level. The custom LPU hardware and narrower catalogue are coverage and lock-in considerations, because not every model run elsewhere is available.

## 6. Choosing this provider - the practical guideline

Groq suits latency-critical serving of mainstream open models where its curated catalogue covers the need. For regulated data, avoid the 30-day batch retention path (or delete promptly), keep fine-tuning artifacts managed, and remember that retained-feature data defaults to US storage even though EU inference exists. Secure a BAA before PHI and confirm whether region pinning can be contractually guaranteed.

## 7. Sources & evidence

See [`entry.yaml`](entry.yaml) and the clause extracts under `docs/primary-sources/groq/`: the Services Agreement, DPA, BAA and AUP, the data-controls and models documentation, the status page, and the platform page (all publisher sources). The trust centre cannot be read.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
