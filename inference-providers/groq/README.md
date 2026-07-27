# Groq - OneHill Inference-Provider Dossier

> **Score: 70.0/100 · Grade B** · HQ: United States · EU residency: yes (Helsinki, very recent) · Trains on inputs: never
> Last verified: 2026-07-25
>
> _Right for latency-sensitive workloads on a curated open catalogue; the biggest caveat is that batch and fine-tuning features retain data and default to US storage._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 4/5 | Inference not retained; ZDR for all - but batch/fine-tune retain to US |
| Compliance & Certifications | 4/5 | SOC 2 Type II + GDPR/HIPAA stated; ISO 27001 unconfirmed |
| Data Residency & Sovereignty | 3/5 | EU data centre exists (Helsinki) but very recent; defaults US |
| Security Posture | 4/5 | SOC 2 Type II controls + Data Controls for ZDR |
| Reliability & SLA | 3/5 | No incidents surfaced; fast-scaling startup, no SLA verified |
| Transparency & Lock-in | 3/5 | OpenAI-compat + open models, but custom LPU + narrower catalogue |
| Cost & Value | 4/5 | Low per-token rates plus a rate-limited free tier |

## 1. What it serves & how it's priced

Groq runs open models on its custom LPU hardware, optimised for very low latency. The catalogue is deliberately curated and narrower than GPU providers: Llama 3.1 8B Instant, Llama 3.3 70B Versatile, gpt-oss 20B/120B (plus gpt-oss-safeguard), Qwen3, Gemma, Mixtral, and DeepSeek R1 Distill Llama 70B. Full DeepSeek, GLM, Mistral, and arbitrary fine-tunes are not available - a real coverage limit versus NVIDIA-GPU providers. Pricing is per-token with a rate-limited free tier; example third-party rates: Llama 3.1 8B $0.05/$0.08, Llama 3.3 70B $0.59/$0.79, gpt-oss-120B $0.15/$0.60, DeepSeek R1 Distill Llama 70B $0.75/$0.99.

## 2. Data governance - where your prompts go

Standard inference is not retained by default, and ZDR is available to all customers via Data Controls - a stronger baseline than enterprise-only ZDR. Groq states it does not train on customer data. The important caveats are in the ancillary features: batch processing retains input/output files for 30 days unless deleted, and fine-tuning retains weights and datasets until the customer deletes them, with this retained-feature data stored in US GCP buckets. There is no closed third-party model routing. A formal sub-processor list was not confirmed.

## 3. Compliance & certifications

SOC 2 Type II is confirmed (2025 report). Groq states GDPR and HIPAA compliance, with a DPA published and a dedicated trust centre. ISO 27001/27701 is unconfirmed. This is a solid compliance posture that falls short of the top anchor mainly on the missing ISO attestation.

## 4. Residency & sovereignty

Groq launched an EU data centre in Helsinki, Finland (with Equinix), announced July 2025. This satisfies the "EU region available" anchor, but it is very recent and default storage is otherwise US, so EU residency guarantees are not yet mature and region pinning is unconfirmed.

**CLOUD Act disclosure:** As a US-headquartered provider, Groq is subject to US jurisdiction including the CLOUD Act, even for EU-hosted data. This is disclosed as standing context, not scored as a defect on its own.

## 5. Reliability & lock-in

No specific incidents surfaced, but Groq is a fast-scaling hardware startup with no public uptime SLA independently verified, holding reliability at 3. On lock-in, the OpenAI-compatible API and open-weight models keep workloads portable at the API level, but the custom LPU hardware and narrower catalogue are genuine coverage/lock-in considerations - you may not find every model you run elsewhere.

## 6. Choosing this provider - the practical guideline

Groq is a strong fit for latency-critical serving of mainstream open models where its curated catalogue covers your needs. Before sending regulated data, avoid the 30-day batch retention path (or delete promptly), keep fine-tuning artifacts managed, and remember retained-feature data defaults to US storage even though EU inference exists. Secure a BAA before PHI and confirm whether region pinning can be contractually guaranteed.

## 7. Sources & evidence

See [`data.yaml`](data.yaml): the data-controls documentation and trust centre (publisher), the Helsinki data-centre newsroom post (publisher), and pricing/catalogue observations (third_party, approximate).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
