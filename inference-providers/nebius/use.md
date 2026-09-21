# Use - Nebius (Token Factory)

_What can it do and how do we use it? The served model catalogue and inference features live
here; context limits are a documented gap below._

<!-- item: models-served -->
## Models served

Nebius' live catalogue (tokenfactory.nebius.com/models/catalog, browsed directly) runs to roughly
**90 model variants**, including:

- **DeepSeek-V4-Pro**, DeepSeek-V4-Flash, DeepSeek-R1-0528, DeepSeek-V3-0324
- **Kimi-K2-Instruct**, Kimi-K2-Thinking, Kimi-K3
- **Qwen3-235B-A22B**, Qwen3-Coder-480B-A35B
- **Llama-3.3-70B-Instruct**, Llama-3.1-8B-Instruct, Llama-Guard-3-8B
- **gpt-oss-120b / gpt-oss-20b**
- **GLM-4.5 / GLM-5.1 / GLM-5.2 / GLM-5.3**
- **NVIDIA Nemotron-3-Ultra-550B-A55B**, Nemotron-3-Nano-30B-A3B
- **MiniMax-M2 / M3**

**Correction (2026-09-21):** an earlier check found several of the models above -
Kimi-K2-Instruct, Llama-3.3-70B-Instruct, and GLM-4.5 - showing **"Public endpoint: Not
available."** An independent re-check found this NOT to mean dedicated-only access: those
specific named versions have simply been **superseded** by newer catalogue entries (e.g.
Kimi-K2.7-Code, GLM-5.x) - ordinary catalogue churn. Open models are confirmed publicly served
per-token (DeepSeek-V4-Pro, gpt-oss-120b, and Llama-3.3-70B-Instruct at $0.13/$0.40 per 1M
tokens, all independently confirmed). The catalogue moves quickly - confirm current
public-endpoint availability on the model's own page.

<!-- item: features -->
## Inference features

Endpoints are **OpenAI-compatible chat/completions**. Per-model tool-calling and
structured-output support follows each served model's own capabilities and was not individually
verified on Nebius' endpoints - confirm per model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

A fine-tuning feature is referenced in the Legal Quick Guide, which states fine-tuning artifacts
are **stored exclusively in EU data centres** - but the specific workflow (supported methods,
base models) was not read in full this pass.

<!-- item: context-limits -->
## Context & token limits

Nebius does not publish a single per-model context-limit table in the sources read; limits track
each served model's native window and should be confirmed on the model's own catalogue page.
