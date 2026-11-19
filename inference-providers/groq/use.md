# Use - Groq

_Served model catalogue, inference features and context limits._

<!-- item: models-served -->
## Models served

Groq's supported-models docs list a curated, fast-changing catalogue, narrower than the general-purpose GPU providers.

- Production, self-serve: gpt-oss 120B and 20B; Whisper large v3 and v3 turbo (speech to text).
- Preview: gpt-oss-safeguard 20B, Qwen3.8-27B, Orpheus TTS and Llama Prompt Guard 2.
- Enterprise contract only: Llama 3.1 8B Instant and Llama 3.3 70B Versatile, retired for free and developer tiers on 2026-08-16.
- Preview, contact sales: Muse Spark Open and MiniMax M2.7.

Qwen3-32B, Gemma, Mixtral, the DeepSeek R1 distill and Llama 4 models are retired. The catalogue is small by design, and each model runs on LPU hardware for latency. If a workload needs full DeepSeek / GLM / Mistral or arbitrary fine-tunes, confirm coverage before committing.

<!-- item: features -->
## Inference features

The endpoints are OpenAI-compatible chat/completions on low-latency LPU hardware, though the docs note that some advanced OpenAI features are not yet supported. Tool/function calling and structured (JSON) output depend on the served model's own capabilities (see each model's entry in this library). Groq's endpoints are not individually verified for them, so confirm per-feature support for each model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

Groq exposes a fine-tuning feature. Its data handling is documented in the your-data docs and the Services Agreement: it retains weights and datasets until the customer deletes them, stored in US GCP buckets. The supported methods, dataset formats and tunable base models are not documented, so confirm those before planning a custom-model workflow.
