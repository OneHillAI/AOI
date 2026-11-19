# Fireworks AI - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: United States (Delaware) · EU residency: yes (sales-gated pinning) · Trains on inputs: never (contract)
> Last verified: 2026-11-19
>
> _Re-read 2026-11-19: the Terms of Service and DPA are readable (both URLs redirect to text PDFs), which resolves the 2026-09-21 finding that they were unreachable. Confidentiality is functional_only; the sub-processor list is still unread (JavaScript-only trust centre)._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Fireworks AI serves a broad, fast-moving open-weight catalogue - Kimi K3 and K3.1 Pro, DeepSeek
V4.1-generation, GLM-5.3, Qwen 3.8, MiniMax M3.1, Llama 3.x and 4, Mistral, NVIDIA Nemotron,
gpt-oss 120B, plus embeddings and FLUX image models - over per-token serverless and per-GPU-second
dedicated deployments.

## 2. Data governance - where your prompts go

The binding Terms (Last Updated 2026-07-10, read 2026-11-19) say Fireworks "will not use your
Content to train our own models or to improve the Service" and runs **Zero Data Retention** for
inference: no logging for human review and no retention beyond generating and delivering Output
(Sec 3.6). You own your Content (Sec 3.2) and the licence to Fireworks is limited to providing the
Service (Sec 3.4). Named exceptions: the **Response API** (stores by default, 30-day auto-delete,
`store=false` opts out), prompt caching, the Batch API, and training, fine-tuning and agent
features. The Confidential Information clause (Sec 8) protects Fireworks' information only, so
there is no express confidentiality duty over your Content (functional_only). The Privacy Notice's
"without your explicit opt-in" wording is looser than the contract and is not itself a contract.

## 3. Compliance & certifications

SOC 2 Type II (2023-10-27), triple ISO (27001/27701/42001, 2025-11-19) and HIPAA compliance are
announced on Fireworks' blog, docs, pricing page and in DPA Schedule 2. No auditor or certificate
date was read, and the Trust Center is a JavaScript-only page that rendered nothing. The DPA does
carry SCCs (Module Two, Irish law) and a UK Addendum.

## 4. Residency & sovereignty

On-demand deployments default to GLOBAL; US, Canada, Europe or APAC pinning needs a quota granted
by Fireworks (and costs 1.5x). Fireworks Sovereign and the Virtual Cloud option run the engine in
the customer's own cluster (enterprise, by contract). DPA 6.1 lets Covered Data be processed
wherever sub-processors have facilities, so serverless is not region-pinned.

## 5. Reliability & lock-in

The public status page shows 22 of 23 endpoints at 100% and the lowest at 99.50% over 90 days,
with no listed incidents. The standard Terms carry no SLA; enterprise Reserved Throughput
advertises 99.9% uptime terms that are not public. An OpenAI-compatible API (Chat Completions and
Completions) over open-weight models keeps workloads portable, and DPA Sec 11.2 gives a 30-day
return then deletion.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list, and
[`docs/primary-sources/fireworks-ai/browser-verified/`](../../docs/primary-sources/fireworks-ai/browser-verified/)
for the 2026-09-20 browser verification pass, and the dated `2026-11-19` files in
[`docs/primary-sources/fireworks-ai/`](../../docs/primary-sources/fireworks-ai/) for the Terms and
DPA clause extracts.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
