# Use - Infercom

_Served model catalogue, inference features and context limits._

<!-- item: models-served -->
## Models served

The Inference API roster is small and changes. It serves EU-hosted gpt-oss-120b,
gemma-4-31B-it, E5-Mistral-7B-Instruct (embeddings) and Whisper-Large-v3 (speech-to-text),
plus one Global-catalog model, MiniMax-M3.1-Flash, processed outside the EU.

Llama 3.3 70B (retired 2026-11-17), DeepSeek V3.1 and V3.2 (2026-11-03) and MiniMax-M2.7
(2026-09-30) have been retired. A wider list (GLM-5.3, MiniMax-M3, gpt-oss-20b, gemma-3,
DeepSeek-V3.2 and others) is available only on Dedicated Capacity or on-premises and depends
on the platform release.

<!-- item: features -->
## Inference features

The docs list OpenAI-compatible chat/completions, a Responses API, Anthropic-SDK compatibility,
vision, audio (Whisper) and embeddings. Tool calling and structured output depend on the
served model and are unverified per model, so per-feature support is inherited from the model
and should be confirmed per model. The Trust Centre says the models served today use no prompt
cache.

<!-- item: context-limits -->
## Context & token limits

Published context lengths: gpt-oss-120b and Gemma 4 31B 128K, E5-Mistral 4K, MiniMax M3.1 Flash
1M tokens. The dedicated list shows up to 1M. Maximum output tokens and per-request token
limits are not documented, so confirm them before sizing long-output workloads.
