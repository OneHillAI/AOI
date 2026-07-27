# Use - Together AI

_What can it do and how do we use it? The served model catalogue and inference features live
here._

<!-- item: models-served -->
## Models served

Together serves a **broad open-weight catalogue** rather than a single family:

- **Llama 3.x / Llama 4** (Meta)
- **DeepSeek V3 / R1**
- **Qwen3**, including the 235B
- **Mistral / Mixtral**
- **gpt-oss 20B / 120B**
- plus **embedding and image** models

For adopters this is the point of the provider: the pricing page and independent third-party
provider analysis both show one OpenAI-compatible endpoint fronting most of the models
documented elsewhere in this library, so you can A/B a workload across families without
changing integration code.

<!-- item: features -->
## Inference features

Together's **OpenAI-compatibility docs** describe **OpenAI-compatible
chat/completions with streaming, tool use and structured outputs**, plus **embeddings** and
**image** generation. How fully each higher-level behaviour works still depends on the
specific served model's own capabilities - see each model's entry in this library - and was
not individually re-verified on Together's endpoints, so treat per-feature support
as "documented at the API, inherited from the model, confirm per model."
