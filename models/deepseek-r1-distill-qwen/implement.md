# Implement - DeepSeek-R1-Distill (Qwen base)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with Ollama, llama.cpp, vLLM, or SGLang. The small sizes run on a single consumer GPU.
Pin the exact revision and verify checksums.

<!-- item: hardware -->
## Hardware & VRAM requirements

Small dense models: 1.5B-7B on consumer GPUs or CPU; 14B/32B on a single data-centre GPU, or
high-end consumer hardware when quantized. 128K context (inherited from the Qwen2.5 bases).
The easiest DeepSeek reasoning weights to deploy.

<!-- item: serving -->
## Serving stacks

First-class support across **vLLM**, **SGLang**, **llama.cpp**, and **Ollama** - small enough
for edge / on-device.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** These have **no safety tuning of their own**, so
supply your own input/output guardrails and a guard/classifier model, add prompt-injection
defences and treat retrieved/tool content as untrusted for agentic use, and account for the
China-aligned filtering inherited from R1.

<!-- item: quantization -->
## Available quantizations

The most extensively quantized DeepSeek artifacts - GGUF and lower-bit across all sizes.
Apache-2.0 permits redistribution of these derivatives; still, verify provenance per mirror.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Apache-2.0 permits unrestricted fine-tuning and further distillation, and the small sizes
make it cheap. The distillation data and code are closed, so there is no from-scratch
reproduction of the distillation itself.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind an OpenAI-compatible endpoint (vLLM / SGLang / Ollama) and point your client at
it; handle the reasoning / think-tag output format at the client.
