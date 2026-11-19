# Use - Sakura Internet AI Engine

_What can it do and how do we use it? Catalogue, features and limits live here._

<!-- item: models-served -->
## Models served

Prices and the live list are in the console. Listed on 2026-11-19 with Sakura's stated licences: gpt-oss-120b and
llm-jp-3.1-8x13b-instruct4 (Apache-2.0, not preview); Qwen3.6-35B-A3B, Qwen3-VL-30B-A3B-Instruct, Qwen3-0.6B, Gemma 4
31B it and Weblab-MedLLM-gpt-oss-120b (Apache-2.0, preview); Phi-4-mini-instruct (MIT, CPU, preview); Kimi-K2.7-Code
(Modified MIT, preview); GLM-5.3-Flash and DeepSeek-V4.1-Flash-1017 (MIT, preview, added 2026-11-18); Whisper
large-v3-turbo, multilingual-e5-large and Qwen3-Embedding-4B; VOICEVOX voices for speech. Closed models by application:
PLaMo 3.0 Prime (Preferred Networks) and cotomi v3 (NEC), under proprietary terms. Licences are Sakura's statements and
were not checked against each model's repository. A model asked for its own name may answer wrongly (manual).

<!-- item: features -->
## Inference features

Streaming, JSON response format, tool calling (not on llm-jp, Phi-4-mini, Qwen3-0.6B, Qwen3-VL), vision on most preview
models (three images per request on Qwen3-VL), and per-model reasoning control (gpt-oss-120b cannot disable reasoning; on
Kimi-K2.7-Code do not disable it or reasoning leaks into the answer). Embeddings, Whisper transcription (30 minutes or
30 MB per file), speech synthesis (about 1,000 characters), and a hosted RAG vector store with two embedding models and
cosine or L2 search. Models whose names start with `preview/` can change or be withdrawn without notice.

Use restrictions that come with the terms: no military use except for Japan's defence (AI Engine terms article 12(1)(vi)),
no disinformation or discrimination uses, no use by export-listed parties.

<!-- item: context-limits -->
## Context and token limits

Context length per Sakura's table: gpt-oss-120b 131,072 tokens; Gemma 4, Qwen3-VL, Qwen3.6, Kimi-K2.7-Code 262,144;
GLM-5.3-Flash and DeepSeek-V4.1-Flash-1017 1,048,575; Qwen3-0.6B 40,960; llm-jp-3.1 and Phi-4-mini 4,096. Maximum output is
32,000 tokens on most models, and a request is cut off after about 5 minutes, so slow models (Gemma 4, Kimi-K2.7-Code)
may stop before the token cap.

<!-- item: fine-tuning -->
## Fine-tuning and custom models

The shared service has no fine-tuning. Private Edition hosts a model you own or have the right to use on a GPU platform
dedicated to you, with Sakura running, monitoring and patching it. Training, retraining, fine-tuning, RAG build, prompt
tuning, guardrail design and closed-network connection are excluded unless written into the order form (article 2(4)),
and you are responsible for the model's safety, legality and guardrails (article 13). It is open to corporations
established under Japanese law only (article 3). PLaMo forbids fine-tuning outright.
