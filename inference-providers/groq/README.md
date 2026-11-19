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
| Compliance & Certifications | 4/5 | DPA and BAA read; SOC 2 Type II is a claim (trust centre unreadable); ISO 27001 unconfirmed |
| Data Residency & Sovereignty | 3/5 | EU capacity exists (Finland, London) but no pinning clause; retained data in US GCP |
| Security Posture | 4/5 | SOC 2 Type II controls + Data Controls for ZDR |
| Reliability & SLA | 3/5 | Public status page, 100% API uptime Aug-Nov 2026; no published SLA |
| Transparency & Lock-in | 3/5 | OpenAI-compat + open models, but custom LPU + narrower catalogue |
| Cost & Value | 4/5 | Low per-token rates plus a rate-limited free tier |

## 1. What it serves & how it's priced

Groq runs open models on its custom LPU hardware, optimised for very low latency. The catalogue is deliberately curated, narrow and fast-changing (read 2026-11-19): gpt-oss 120B and 20B and Whisper in production; Qwen3.8-27B, gpt-oss-safeguard, Orpheus TTS and Prompt Guard in preview. Llama 3.1 8B and 3.3 70B were retired for free and developer tiers on 2026-08-16 and are now enterprise-contract only, and the DeepSeek R1 distill, Gemma, Mixtral and Qwen3-32B models are gone. Full DeepSeek, GLM, Mistral, and arbitrary fine-tunes are not available - a real coverage limit versus NVIDIA-GPU providers. Pricing is per-token with a rate-limited free tier, read from the docs models page (groq.com/pricing now redirects to the home page): gpt-oss-120B $0.15/$0.60, gpt-oss-20B $0.075/$0.30, Qwen3.8-27B $0.80/$4.00.

## 2. Data governance - where your prompts go

Standard inference is not retained by default, and ZDR is available to all customers via Data Controls according to the docs (the Services Agreement says "Eligible Customers", a term it never defines) - a stronger baseline than enterprise-only ZDR. The docs also say inputs and outputs may be logged for up to 30 days when Groq troubleshoots errors or investigates abuse, unless ZDR is on. The Services Agreement (last modified 2026-06-22, unchanged) bars Groq from using Inputs or Outputs for training and has a mutual confidentiality clause naming Customer Data. The important caveats are in the ancillary features: batch processing retains input/output files for 30 days unless deleted, and fine-tuning retains weights and datasets until the customer deletes them, with this retained-feature data stored in US GCP buckets. There is no closed third-party model routing. The DPA points to a sub-processor list at trust.groq.com/subprocessors, which is JavaScript-only and could not be read.

## 3. Compliance & certifications

The DPA (GDPR, UK and Swiss transfers via deemed-signed SCCs) and a HIPAA BAA (generally available services only) were read on 2026-11-19. SOC 2 Type II is a trust-centre claim from the July read (2025 report); trust.groq.com is now JavaScript-only, so it is not re-confirmed. ISO 27001/27701 is unconfirmed. This is a solid compliance posture that falls short of the top anchor on the missing ISO attestation and the gated SOC 2 report.

## 4. Residency & sovereignty

Groq launched an EU data centre in Helsinki, Finland (with Equinix) in July 2025, and its platform page now lists EU-1 Vantaa (Finland) and EU-2 London. This satisfies the "EU region available" anchor, but retained data is stored in US GCP buckets, the DPA permits US processing, EEA customers contract with Groq UK Limited, and region pinning is unconfirmed.

**CLOUD Act disclosure:** As a US-headquartered provider, Groq is subject to US jurisdiction including the CLOUD Act, even for EU-hosted data. This is disclosed as standing context, not scored as a defect on its own.

## 5. Reliability & lock-in

Groq has a public status page (groqstatus.com) showing 100% uptime for the API and production models from August to November 2026, but no SLA is published, so reliability is 3 (raised from 2 on 2026-11-19). On lock-in, the OpenAI-compatible API and open-weight models keep workloads portable at the API level, but the custom LPU hardware and narrower catalogue are genuine coverage/lock-in considerations - you may not find every model you run elsewhere.

## 6. Choosing this provider - the practical guideline

Groq is a strong fit for latency-critical serving of mainstream open models where its curated catalogue covers your needs. Before sending regulated data, avoid the 30-day batch retention path (or delete promptly), keep fine-tuning artifacts managed, and remember retained-feature data defaults to US storage even though EU inference exists. Secure a BAA before PHI and confirm whether region pinning can be contractually guaranteed.

## 7. Sources & evidence

See [`entry.yaml`](entry.yaml) and the clause extracts under `docs/primary-sources/groq/`: the Services Agreement, DPA, BAA and AUP, the data-controls and models documentation, the status page, and the platform page (all publisher). The trust centre could not be read.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
