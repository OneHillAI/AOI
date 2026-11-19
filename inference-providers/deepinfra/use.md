# Use - DeepInfra

_What can it do and how do we use it? The served model catalogue, features and context limits
live here; fine-tuning is a documented gap below._

<!-- item: models-served -->
## Models served

The live listing (2026-11-19) has 411 entries, of which **232 are public and not deprecated**: 93
text-generation, plus image, video, speech, embedding and reranker models. Open-weight text families
include:

- **DeepSeek V4 and V4.1** (Flash, Pro) and V3.x
- **Kimi K3 and K3.1 Pro**
- **GLM-5.x**
- **Qwen3.5**
- **gpt-oss-120B and 20B**
- **Gemma 4**, **Nemotron 3**, **MiMo V2.6** and **Llama 3.x**

**94 of the 232 are flagged partner models**, including nine Anthropic Claude entries and thirteen
Google entries. They run on the partner's infrastructure under the partner's data policy, so treat
them as a separate governance category from the hosted open catalogue.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible** chat/completions across the catalogue, plus embeddings,
reranking, speech and media generation. Extras include per-request service tiers (Priority and
Flex), prompt cache retention for 5 minutes or 1 hour on some models, and **dedicated GPU
instances**. The model listing tags each model with capabilities such as tools and reasoning;
support for tool calling and structured output follows each model and was not individually
verified, so confirm per model.

<!-- item: context-limits -->
## Context & token limits

The pricing page shows a **context column** per model - for example the DeepSeek V4 family 1024k,
DeepSeek V3.2 160k, Llama 3.3 70B Turbo 128k and Gemma 4 31B 256k - and the model listing carries
a `max_tokens` field. Limits on dedicated deployments were not read; confirm them on the model's
page before relying on a long-context workload.
