# Use - Baseten

_What can it do and how do we use it? The served model catalogue and inference features live
here; context limits are a documented gap below._

<!-- item: models-served -->
## Models served

Baseten's curated **Model Library** (baseten.co/library, read directly) currently features:

- **DeepSeek V4.1 Flash** (552B MoE, multimodal, 1M-token context)
- **GLM-5 / GLM-5.3 / GLM-5.3 Fast**
- **Kimi K3**
- **Llama 3.3 70B Instruct**
- **Qwen3.5 35B-A3B**, Qwen3 TTS, Qwen3 8B Reranker/Embedding, Qwen Image
- **Whisper Large V3** (transcription)
- **Flux.2 [dev]** (image generation)
- Embeddings: EmbeddingGemma, Nomic Embed Code, BGE Embedding ICL

Beyond the curated library, Baseten is equally a **bring-your-own-model deploy platform**: any
open-source, fine-tuned, or fully custom model can be deployed on dedicated GPUs.

<!-- item: features -->
## Inference features

Hosted Model APIs support the **OpenAI Chat Completions API** and a **beta Anthropic Messages
API**. Per-model tool-calling and structured-output support follows each served model's own
capabilities and was not individually verified on Baseten's endpoints - confirm per model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

**Training Jobs/Loops** are documented as a platform pathway alongside Model APIs and custom
dedicated-GPU deploys (docs.baseten.co/overview), but the specific fine-tuning workflow was not
read in full this pass - confirm supported methods and base models before planning a custom-model
workflow.

<!-- item: context-limits -->
## Context & token limits

Baseten does not publish a single per-model context-limit table in the sources read; limits track
each served model's native window (DeepSeek V4.1 Flash's 1M-token context is noted on its own
model page) and should be confirmed per model.
