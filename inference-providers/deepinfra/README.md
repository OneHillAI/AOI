# DeepInfra - OneHill Inference-Provider Dossier

> **Score: 60.4/100 · Grade C** · HQ: United States · EU residency: no · Trains on inputs: never
> Last verified: 2026-07-25
>
> _Right for cost-sensitive open-model serving; the biggest caveat is that its zero-retention covers only its own open models - closed models routed through it fall under those vendors' terms - and there is no EU residency._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 4/5 | Zero-retention, no training, scoped to its own open-model serving |
| Compliance & Certifications | 3/5 | ISO 27001 + SOC 2 Type 1 only (not Type II); HIPAA unattested |
| Data Residency & Sovereignty | 1/5 | US-only data centres; no EU residency surfaced |
| Security Posture | 3/5 | ISO 27001 + Type 1 SOC 2; no independent pen-test surfaced |
| Reliability & SLA | 3/5 | No incidents surfaced; no public SLA verified |
| Transparency & Lock-in | 4/5 | OpenAI-compat + portable open models; some closed re-sold |
| Cost & Value | 5/5 | Among the cheapest providers on the market |

## 1. What it serves & how it's priced

DeepInfra is a US-headquartered, low-cost provider on NVIDIA GPUs serving roughly 77-90+ open models: Llama 3.x/4.x, DeepSeek V3/V3.2/V4 variants, Qwen3, Kimi K2, GLM-5, gpt-oss-120B, MiniMax-M2, Nemotron, Gemma, and more. It also re-sells some closed models (Anthropic Claude, Google). Pricing is mixed - pay-as-you-go per-token at the cheapest tier plus dedicated GPUs by the hour. Example third-party rates: Llama 3.1 8B ~$0.02/M, Llama 3.3 70B ~$0.35/M, gpt-oss-120B ~$0.08/M blended; GPU/hr A100 $0.89, H100 $1.79, H200 $2.19, B200 $2.79. Cost is its standout strength, earning the top anchor.

## 2. Data governance - where your prompts go

DeepInfra operates a zero-retention policy for inputs and outputs and states it does not train on submitted data; batch requests may store data temporarily, encrypted on disk, then delete it after inference. The critical finding - and the reason this dimension is a 4, not a 5 - is third-party routing leakage: when you use Google or Anthropic models **through** DeepInfra, your data is subject to **that vendor's** storage and training policy. DeepInfra's zero-retention guarantee is scoped to its own open-model serving; third-party model routing follows the downstream vendor's terms. Sub-processors are not disclosed. Treat the zero-retention promise as scoped to open models, and check the downstream vendor's terms whenever you call a closed model.

## 3. Compliance & certifications

DeepInfra has published a SOC 2 Type 1 report (a point-in-time attestation, not the ongoing Type II) and is ISO 27001 certified. HIPAA and GDPR are framed as technical and organisational measures rather than a formal attestation or BAA, so HIPAA/BAA is treated as unconfirmed. The ISO 27001 certification plus GDPR measures meet the mid anchor, but the Type-1-only SOC 2 and unattested HIPAA hold compliance at 3.

## 4. Residency & sovereignty

DeepInfra runs US-based data centres, and no EU data-residency option was surfaced; region pinning is unconfirmed. This single-region, US-only posture places residency near the floor at 1.

**CLOUD Act disclosure:** As a US-headquartered provider, DeepInfra is subject to US jurisdiction including the CLOUD Act. With no EU residency option, all data is under US jurisdiction. This is disclosed as standing context.

## 5. Reliability & lock-in

No incidents surfaced, but no public uptime SLA or failover documentation was independently verified, holding reliability at 3. Lock-in is low for open models - an OpenAI-compatible API and portable open-weight checkpoints run elsewhere or self-hosted - but the re-sold closed models are not portable and carry different data terms, adding some routing opacity.

## 6. Choosing this provider - the practical guideline

DeepInfra is a strong choice when cost is the driving constraint and your data is low-to-moderate sensitivity on open models. Do not treat it as EU-resident, and do not assume its zero-retention applies when you route to Claude or Google models - those calls follow the third-party vendor's terms. Avoid PHI absent a signed BAA, and prefer its own open-model endpoints if the zero-retention guarantee matters to you.

## 7. Sources & evidence

See [`data.yaml`](data.yaml): data and data-privacy docs including the third-party routing note (publisher), the compliance trust centre (third_party), and pricing/catalogue (third_party, approximate).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
