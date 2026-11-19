# Use - Nebius (Token Factory)

_What can it do and how do we use it? The served model catalogue, inference features and context
limits live here._

<!-- item: models-served -->
## Models served

Nebius' catalogue (tokenfactory.nebius.com/models/catalog, rendered in a browser on 2026-11-19)
lists **133 models**, including:

- **DeepSeek V4.1 Flash** and V4.1 Flash 1017, **DeepSeek-V4-Pro-0813**, DeepSeek-R1-0528
- **Kimi-K3** and **Kimi-K3.1-Pro**, Kimi-K2.5/K2.6/K2.7-Code
- **GLM-5.1 to GLM-5.3** and GLM-5.3-Flash, **MiniMax-M3**
- **Qwen3.x** families including Qwen3.8-27B and Qwen3-Coder-480B-A35B
- **gpt-oss-120b / gpt-oss-20b**, **Muse Spark Open**, Reflection Beam 1.0
- **NVIDIA Nemotron-3-Ultra**, Nemotron 3.5 Super VL and 3.5-Lightning
- Llama 3.x, Gemma 4, Hermes-4, embedding models

The catalogue's platform column shows the same tags on every row, so the per-model page decides
whether a **public endpoint** exists. It does for gpt-oss-120b, DeepSeek-V4-Pro-0813, GLM-5.3 and
MiniMax-M3; it does **not** for DeepSeek-V4-Pro, Llama-3.3-70B-Instruct and Kimi-K2-Instruct,
which are dedicated-only (the first two follow Serverless removal notices dated 2026-11-09 and
2026-08-31). The September note that Llama-3.3-70B-Instruct was publicly priced could not be
reproduced. The serverless catalogue changes every few weeks, so check the model page before
building on it.

<!-- item: features -->
## Inference features

Endpoints are **OpenAI-compatible chat/completions**. Per-model tool-calling and
structured-output support follows each served model's own capabilities and was not individually
verified on Nebius' endpoints - confirm per model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

A fine-tuning feature is documented (supervised fine-tuning, custom speculator training and a
data lab), and the Legal Quick Guide states fine-tuning artifacts are **stored exclusively in EU
data centres** with no regional selection - but the specific workflow (supported methods, base
models) was not read in full this pass.

<!-- item: context-limits -->
## Context & token limits

The catalogue lists a context window per model, for example 131K tokens for gpt-oss-120b, 979K for
DeepSeek-V4-Pro-0813, 1,024K for GLM-5.3 and Kimi-K3 and 128K for Llama-3.3-70B-Instruct. About a
fifth of the rows show no value.
