# Implement - GLM-4-9B-Chat (original, glm-4 licence)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `THUDM` organisation on Hugging Face and serve with
transformers, vLLM, llama.cpp, or Ollama; it runs on a single consumer GPU. **Complete the
glm-4 commercial registration first** if your use is commercial. Pin the exact revision and
verify checksums.

<!-- item: hardware -->
## Hardware & VRAM requirements

A 9B dense model: a single consumer GPU, or CPU when quantized. The GLM-4-9B-Chat-1M variant
advertises a 1M-token context, which is memory-intensive in practice; the standard Chat is
128K.

<!-- item: serving -->
## Serving stacks

**vLLM**, **transformers**, **llama.cpp**, and **Ollama** - broad support for a small 2024
model, though the tooling is older than the current GLM line.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** First, **complete the commercial registration** and
honour the glm-4 naming and field-of-use terms - these are binding licence conditions - and
**account for the revocable grant** in your risk assessment. Then: supply your own input/output
guardrails and a guard/classifier model (China-aligned alignment, no first-party guard), and
add prompt-injection defences for agentic use.

<!-- item: quantization -->
## Available quantizations

Widely quantized (GGUF and lower-bit) as a small model. Redistribution of these derivatives
must carry the **glm-4 licence** and the name rules - verify provenance per mirror.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning is permitted, but derivatives **inherit the revocable, registration-gated licence**
and the mandatory "glm-4" name prefix. The training data and code are closed, so there is no
from-scratch reproduction.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM's OpenAI-compatible endpoint. The 2024-era chat template and tool-call
conventions are older than the current GLM line - confirm behaviour per serving stack.
