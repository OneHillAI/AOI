# Use - Baseten

_What can it do and how do we use it? The served model catalogue, inference features and context
limits live here._

<!-- item: models-served -->
## Models served

Baseten's **Model APIs** list (docs table and pricing page, re-read 2026-11-19) currently carries:

- **DeepSeek V4.1 Flash** (with 1017 and Fast variants), **DeepSeek V4 Pro 0813**, **DeepSeek V4 Flash 0731**
- **GLM-5.2**, **GLM-5.3**, **GLM-5.3 Fast** and **GLM-5.3 Flash**
- **Kimi K3** and **Kimi K3.1 Pro**
- **NVIDIA Nemotron 3 Ultra** and **Nemotron 3.5 Super VL**
- **GPT OSS 120B**, **Muse Spark Open**, **Beam**
- The Base Labs decision models mammoth-1, elephant-1 and joey-1 (priced per token)

The wider **Model Library** (baseten.co/library) also lists transcription (Whisper Large V3, Qwen 3
ASR), text to speech, image generation (Flux.2 [dev], Qwen Image), embedding and reranker models
(EmbeddingGemma, BGE, Qwen3 8B) and some Qwen 3 and Cogito language models. Llama 3.3 70B and
Qwen3.5 35B-A3B, listed in September, are not on the Model APIs list and were not seen on the
library landing page. Beyond the library, Baseten is equally a **bring-your-own-model deploy
platform**: any open-source, fine-tuned or custom model can be deployed on dedicated GPUs.

<!-- item: features -->
## Inference features

Hosted Model APIs support the **OpenAI Chat Completions**, **OpenAI Responses** and **Anthropic
Messages** APIs, and a System One API serves the Base Labs decision models. Per-model tool-calling
and structured-output support follows each served model's own capabilities and was not
individually verified on Baseten's endpoints - confirm per model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

**Training Jobs and Loops** are documented as a platform pathway alongside Model APIs and custom
dedicated-GPU deploys (docs.baseten.co overview), but the specific fine-tuning workflow was not
read in full this pass - confirm supported methods and base models before planning a custom-model
workflow.

<!-- item: context-limits -->
## Context & token limits

The Model APIs docs publish a per-model table of context and maximum output. Most models offer
1048k tokens of context; **Kimi K3.1 Pro** is 1000k in and 1048k out, **Nemotron 3 Ultra** 202k and
**GPT OSS 120B** 128k. Output caps run from 131k to 1048k. The page warns that these limits can
differ from the Hugging Face model card, so use the table. It covers Model APIs only, not
dedicated deployments.
