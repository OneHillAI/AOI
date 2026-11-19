# Use - Together AI

_Served model catalogue, inference features and context limits._

<!-- item: models-served -->
## Models served

The serverless chat catalogue (24 models) is led by **DeepSeek V4 Pro 0813, V4.1
Flash and V4.1 Flash 1017; GLM-5.2, 5.3 and 5.3 Flash; Kimi K3 and K3.1 Pro; MiniMax M3.1 Flash;
Qwen3.5 9B, 3.6 Plus, 3.7 Max and Plus, 3.8 Flash and Qwen4 Max; gpt-oss-120B**; Meta Muse Glimmer
30B and Muse Spark Open 816B; Reflection Beam 1.0; Thinking Machines Inkling 2 Small; NVIDIA
Nemotron 3.5 Super VL; and a few smaller or free models. Vision, image, video and audio models are
also served, including wrapped third-party APIs. **Not on serverless chat:** Llama 3.3 70B,
Gemma 4 31B, Cogito v2.1, MiniMax M3 and M2.7, Qwen3-235B (Llama, Gemma 4 and Mixtral are
fine-tuning base models only). **There are no serverless embedding, rerank or moderation models.**
The list turns over quickly, so check the live table before relying on a model.

<!-- item: features -->
## Inference features

The docs list OpenAI-compatible chat, completions, vision, image generation, text-to-speech and
speech-to-text, plus a Messages API and a Responses API. The catalogue table marks **function
calling and structured outputs as supported** for nearly every chat model. It also states the
quantisation of each model (FP4, FP8, NVFP4, MXFP4), which contradicts the docs claim that models
are hosted at full precision.

<!-- item: context-limits -->
## Context & token limits

The catalogue table publishes context per model: gpt-oss-120B 131,072; Qwen3.5 9B 262,144; DeepSeek
V4 Pro 0813 and Kimi K3 about 1.05 million; DeepSeek V4.1 Flash 1,000,000; GLM-5.3 1,048,575; Meta
Muse Glimmer 30B 131,072; Together Tev1 4B 32,768. Maximum output tokens are not listed there.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

Fine-tuning and post-training are sold and priced on the pricing page. LoRA and full fine-tuning
are billed per 1M training tokens (from $0.34 for Qwen3.5 0.8B to $40 for GLM-5.1 and 5.2, with
minimum charges of $4 to $60) over Llama, Qwen, DeepSeek, Gemma, gpt-oss, Kimi and GLM base
models, and GPU-hour post-training is also offered. Methods, data formats and the hosting terms
for tuned models are not stated.
