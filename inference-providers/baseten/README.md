# Baseten - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: United States · EU residency: no published managed region (self-hosted only) · Trains on inputs: never
> Last verified: 2026-09-21
>
> _An independent Cowork browser pass (2026-09-21) confirmed the MUTUAL confidentiality clause on two separate fetches and found a real 99.9% SLA - but retracted an earlier ISO 27001 claim that turned out to have no basis anywhere._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Baseten combines a curated serverless **Model Library** (DeepSeek V4.1 Flash, GLM-5.3, Kimi K3,
Llama 3.3 70B, Qwen3.5, Whisper, Flux.2, embeddings) with a bring-your-own-model deploy platform
on dedicated GPUs. Pricing is per-token for Model APIs and per-GPU-minute for dedicated
deployments, both published directly.

## 2. Data governance - where your prompts go

Zero Data Retention is the default for Model APIs and Dedicated Inference (per the Security
Practices page); Async Inference queues inputs for 72 hours. Terms & Conditions bar training on
Customer Content and impose a MUTUAL confidentiality duty over it - independently confirmed on
two separate live fetches.

## 3. Compliance & certifications

SOC 2 Type II (named audit firm), HIPAA, and a GDPR DPA are all confirmed directly. **Correction:**
a prior ISO 27001 claim is retracted - no trace of it was found anywhere; PCI/FedRAMP/CSA STAR
claims remain unconfirmed behind a fully JS-gated Trust Center portal.

## 4. Residency & sovereignty

No published, named EU region exists for the managed service; the practical EU-residency path is
the enterprise **Self-Hosted** tier (workload plane inside the customer's own VPC).

## 5. Reliability & lock-in

**Correction:** a real, committed SLA exists (99.9% uptime, credits capped at 40%, 24h claim
window) - a prior draft had located none. The status page confirms all systems operational with
three brief incidents in the current window, all resolved same/next-day. An
OpenAI/Anthropic-compatible API over an open-weight Model Library, with a documented 30-day
export window and deletion right.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list, and
[`docs/primary-sources/baseten/browser-verified/`](../../docs/primary-sources/baseten/browser-verified/)
for the independent Cowork verification pass this dossier is now grounded on.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
