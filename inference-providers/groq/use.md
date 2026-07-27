# Use - Groq

_What can it do and how do we use it? The served model catalogue, inference features and
fine-tuning live here; context limits are a documented gap below._

<!-- item: models-served -->
## Models served

Groq's **supported-models docs** list a **curated open-weight catalogue**, narrower than the
general-purpose GPU providers:

- **Llama 3.1 8B Instant**
- **Llama 3.3 70B Versatile**
- **gpt-oss 20B / 120B** (plus gpt-oss-safeguard)
- **Qwen3**
- **Gemma**
- **Mixtral**
- **DeepSeek R1 Distill Llama 70B**
- **Whisper** (speech-to-text)

The trade is deliberate: fewer models, but each run on LPU hardware for latency. If your workload
needs full DeepSeek / GLM / Mistral or arbitrary fine-tunes, confirm coverage before committing.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible chat/completions** on low-latency LPU hardware, though the
docs note **some advanced OpenAI features are not yet supported**. Higher-level behaviours such as
**tool/function calling** and **structured (JSON) output** depend on the specific served model's
own capabilities - see each model's entry in this library - and are not individually verified
on Groq's endpoints, so treat per-feature support as "inherited from the model,
confirm per model."

<!-- item: fine-tuning -->
## Fine-tuning / custom models

Groq exposes a **fine-tuning feature**, and its data-handling terms are documented in the
**your-data docs** and **Services Agreement**: it **retains weights and datasets until the customer
deletes them**, stored in US GCP buckets. The feature's
scope - the supported methods, dataset formats, and which base models can be tuned - is not
documented, so confirm those specifics before planning a custom-model workflow.
