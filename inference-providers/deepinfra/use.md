# Use - DeepInfra

_What can it do and how do we use it? The served model catalogue and inference features live
here; context limits and fine-tuning are documented gaps below._

<!-- item: models-served -->
## Models served

DeepInfra serves a **broad open catalogue of ~77-90+ models** rather than a single family:

- **Llama 3.x / 4.x**
- **DeepSeek V3 / V3.2 / V4** variants
- **Qwen3**
- **Kimi K2**
- **GLM-5**
- **gpt-oss-120B**
- **MiniMax-M2**
- **Nemotron**
- **Gemma**

It **also re-sells some closed models** (Anthropic Claude, Google) - useful for reach, but
these are not portable and route your data under those vendors' terms, so treat them as a
separate governance category from the open catalogue.

<!-- item: features -->
## Inference features

The endpoints are **OpenAI-compatible** chat/completions across the catalogue, with **per-hour
dedicated GPU instances** available for reserved throughput. Higher-level behaviours such as
**tool/function calling** and **structured (JSON) output** depend on each served model's own
capabilities - see the model's entry in this library - and were not individually re-verified
on DeepInfra's endpoints, so treat per-feature support as "inherited from the
model, confirm per model."
