# Implement - Mistral (research / non-production licence)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `mistralai` organisation on Hugging Face and serve
with vLLM, transformers, llama.cpp, or Ollama - **for research / non-production use only**. Pin
the exact revision and verify checksums, and confirm the per-model licence tier (MRL vs MNPL).

<!-- item: hardware -->
## Hardware & VRAM requirements

A wide range: Ministral 8B and Codestral 22B run on one or two GPUs; Mistral Large 2 (123B) and
Pixtral Large (124B) need serious multi-GPU infrastructure or aggressive quantization. Any
production deployment is licence-barred without a commercial agreement.

<!-- item: serving -->
## Serving stacks

**vLLM**, **transformers**, **llama.cpp**, and **Ollama** - strong mechanics, but production
serving is licence-barred without a commercial agreement.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** First, **do not deploy in production or commercially
without a negotiated Mistral licence** - the MRL/MNPL bar it. Then: supply your own input/output
guardrails and a guard/classifier model (historically lighter safety tuning, no first-party
guard), add prompt-injection defences, and treat images as untrusted input for Pixtral Large.

<!-- item: quantization -->
## Available quantizations

Community GGUF / AWQ / FP8 builds circulate, but their use remains bound by the **MRL/MNPL
non-commercial terms** - a quant confers no commercial rights.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning for research is permitted, but derivatives **inherit the non-commercial bar** -
commercial/production use of a derivative needs a negotiated Mistral licence. Training data and
code are closed, so there is no from-scratch reproduction.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM's OpenAI-compatible endpoint for research. Mistral also offers these models on
its own commercial API/platform, which is the **licensed commercial path** for production use.
