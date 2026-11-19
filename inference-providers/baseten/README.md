# Baseten - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: United States · EU residency: an `eu` region for dedicated model deployments (Model APIs need a support-enabled policy) · Trains on inputs: never
> Last verified: 2026-11-19
>
> _Terms, DPA and SLA are current as of 2026-11-19. The Security Practices were last updated on 2026-11-12. The Trust Center labels ISO 27001 (vendor claim, certificate access-gated)._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Baseten combines serverless **Model APIs** (DeepSeek V4.1 Flash and V4 Pro, GLM-5.2 and 5.3,
Kimi K3 and K3.1 Pro, Nemotron 3 Ultra, GPT OSS 120B, Muse Spark Open) and a wider **Model
Library** (Whisper, Flux.2, embeddings) with a bring-your-own-model deploy platform on dedicated
GPUs. Pricing is per-token for Model APIs and per-GPU-minute for dedicated deployments. Both are
published, with default rate limits and a 30-day deprecation notice in the docs.

## 2. Data governance - where your prompts go

The Security Practices (2026-11-12) commit Model APIs and Dedicated Inference to a Zero Data
Retention posture. They carry no explicit "ZDR is the default" sentence and add a
customer-controlled-factors carve-out. Async Inference queues inputs for up to 72 hours. The Terms
& Conditions bar training on Customer Content and impose a mutual confidentiality duty over it.

## 3. Compliance & certifications

SOC 2 Type II, HIPAA and a GDPR DPA are confirmed. The Trust Center also labels ISO 27001:2022
(announced 2026-08-24) and PCI DSS SAQ D. The certificate, SOC reports and PCI attestation are
access-gated, so they are vendor claims and the score is 4.

## 4. Residency & sovereignty

An `eu` region is published in the Regional deployments docs and is selectable per dedicated GPU
model deployment. Model APIs residency needs a support-enabled compliance policy, and the
Self-Hosted tier is the stronger path. US headquarters carries standing CLOUD Act exposure.

## 5. Reliability & lock-in

The SLA is a committed 99.9% ("commercially reasonable measures") with credits capped at 40% and a
24-hour claim window. The status page shows all systems operational and logs 7 major or critical
incidents between 2026-09-20 and 2026-11-18, including a 21-minute outage of all Model APIs on
2026-11-11. The API is OpenAI-, Responses- and Anthropic-compatible over a mostly open-weight
catalogue, with a 30-day export window and a deletion right.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list and
[`docs/primary-sources/baseten/`](../../docs/primary-sources/baseten/) for the extracts.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
