# Use - Fireworks AI

_What can it do and how do we use it? The served model catalogue and inference features live
here; fine-tuning and context limits are documented gaps below._

<!-- item: models-served -->
## Models served

Fireworks' model catalogue (fireworks.ai/models, read directly) is broad and fast-moving:

- **Kimi K3 / K2.7 (Code) / K2.6**
- **DeepSeek V4.1 Flash / V4 Pro / V4 Flash** (incl. Vision Exp)
- **GLM-5.3** (Flash/Fast/US variants) / GLM-5.2 / GLM-4.5V (vision)
- **Qwen3.8 Max/Flash**, Qwen3 VL, Qwen3 Embedding/Reranker
- **Llama 3.3 70B**, 3.2 (incl. Vision), 3.1 family
- **Mistral Large 3** / Ministral 3 / Nemo
- **NVIDIA Nemotron 3 Ultra** / 3.5 Lightning
- **gpt-oss 120B**
- Embeddings (BGE-M3, Voyage 4) and image (FLUX.1 schnell/dev + ControlNet)

Recheck this list periodically - the catalogue moves generations quickly, as it did between the
prior and current passes on peer providers in this library.

<!-- item: features -->
## Inference features

Endpoints are **OpenAI-compatible chat/completions**, plus an OpenAI-compatible **Responses API
with MCP support**. Per-model tool-calling and structured-output support follows each served
model's own capabilities and was not individually verified on Fireworks' endpoints - confirm per
model.

<!-- item: fine-tuning -->
## Fine-tuning / custom models

Fireworks documents **on-demand dedicated deployment** of custom and fine-tuned models, but the
specific fine-tuning workflow - supported methods, dataset formats, base models - was not read in
full this pass. Confirm the current scope in the Fireworks docs before planning a custom-model
workflow.

<!-- item: context-limits -->
## Context & token limits

Fireworks does not publish a single per-model context-limit table in the sources read; limits
track each served model's native window and should be confirmed on the model's own catalogue
page.
