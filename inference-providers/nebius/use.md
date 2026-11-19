# Use - Nebius (Token Factory)

_Served model catalogue, inference features and context limits._

<!-- item: models-served -->
## Models served

The catalogue (tokenfactory.nebius.com/models/catalog, rendered in a browser) lists 133 models,
including DeepSeek V4.1 Flash and V4.1 Flash 1017, DeepSeek-V4-Pro-0813 and DeepSeek-R1-0528;
Kimi-K3, Kimi-K3.1-Pro and Kimi-K2.5/K2.6/K2.7-Code; GLM-5.1 to GLM-5.3, GLM-5.3-Flash and
MiniMax-M3; Qwen3.x families including Qwen3.8-27B and Qwen3-Coder-480B-A35B; gpt-oss-120b and
gpt-oss-20b, Muse Spark Open and Reflection Beam 1.0; NVIDIA Nemotron-3-Ultra, Nemotron 3.5 Super
VL and 3.5-Lightning; and Llama 3.x, Gemma 4, Hermes-4 and embedding models.

The platform column shows the same tags on every row, so the per-model page decides whether a
public endpoint exists. It does for gpt-oss-120b, DeepSeek-V4-Pro-0813, GLM-5.3 and MiniMax-M3.
DeepSeek-V4-Pro, Llama-3.3-70B-Instruct and Kimi-K2-Instruct are dedicated-only. The first two
follow Serverless removal notices dated 2026-11-09 and 2026-08-31. The serverless catalogue
changes every few weeks, so check the model page before building on it.

<!-- item: features -->
## Inference features

Endpoints are OpenAI-compatible chat/completions. Per-model tool-calling and structured-output
support follows each served model's own capabilities and is unverified on Nebius' endpoints, so
confirm per model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

A fine-tuning feature is documented (supervised fine-tuning, custom speculator training and a data
lab). The Legal Quick Guide states fine-tuning artifacts are stored exclusively in EU data centres
with no regional selection. Supported methods and base models are not stated.

<!-- item: context-limits -->
## Context & token limits

The catalogue lists a context window per model, for example 131K tokens for gpt-oss-120b, 979K for
DeepSeek-V4-Pro-0813, 1,024K for GLM-5.3 and Kimi-K3 and 128K for Llama-3.3-70B-Instruct. About a
fifth of the rows show no value.
