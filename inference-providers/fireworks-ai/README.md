# Fireworks AI - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: United States (Delaware) · EU residency: yes (sales-gated beyond default) · Trains on inputs: opt-in only
> Last verified: 2026-09-21
>
> _An independent Cowork browser pass (2026-09-21) found Fireworks' Terms of Service and DPA to be unreachable (noindexed, ROBOTS_DISALLOWED) - a real correction to an earlier draft that claimed to have read them. Confidentiality is now coded unknown, not functional_only; sub-processor disclosure is unconfirmed._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Fireworks AI serves a broad, fast-moving open-weight catalogue - Kimi K3, DeepSeek V4-generation,
GLM-5.3, Qwen3.8, Llama 3.x, Mistral, NVIDIA Nemotron, gpt-oss 120B, plus embeddings and FLUX
image models - over per-token serverless and per-GPU-second dedicated deployments.

## 2. Data governance - where your prompts go

**Correction:** the Terms of Service and DPA - the two documents that would settle the exact ZDR
clause, the confidentiality direction, and the sub-processor list - are both page-level noindexed
and unreachable to a real browser. What IS independently confirmed via readable docs: Zero Data
Retention for serverless/dedicated inference (the Response API is the one exception - stores by
default, 30-day auto-delete, `store=false` opts out), and via the Privacy Policy, no training
without the customer's explicit opt-in.

## 3. Compliance & certifications

SOC 2 Type II (2023-10-27), triple ISO (27001/27701/42001, 2025-11-19), and HIPAA compliance are
all announced on Fireworks' own blog/docs (independently confirmed, no auditor named, no
certificate dates); the Trust Center portal itself is fully JS-gated and was not independently
read.

## 4. Residency & sovereignty

Europe/APAC region pinning exists for on-demand deployments (sales-gated quota); a BYOC/Virtual
Cloud option runs entirely in the customer's own VPC (enterprise-negotiated).

## 5. Reliability & lock-in

A public status page shows strong recent uptime (~99.67-100% across 28 endpoints); no SLA/credit
clause was found in the standard Terms. An OpenAI-compatible API (Chat Completions + Completions,
independently confirmed) over open-weight models keeps workloads portable; a prior claim of a
Responses API with MCP support, and of a documented 30-day DPA data-return right, are both
unconfirmed and have been removed.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list, and
[`docs/primary-sources/fireworks-ai/browser-verified/`](../../docs/primary-sources/fireworks-ai/browser-verified/)
for the independent Cowork verification pass this dossier is now grounded on.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
