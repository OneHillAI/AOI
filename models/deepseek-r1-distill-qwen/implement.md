# Implement - DeepSeek-R1-Distill (Qwen base)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with Ollama, llama.cpp, vLLM or SGLang. The small sizes run on a single consumer GPU.
Pin the exact revision and verify checksums.

<!-- item: hardware -->
## Hardware & VRAM requirements

The 1.5B-7B models run on consumer GPUs or CPU. The 14B and 32B run on a single data-centre
GPU, or on high-end consumer hardware when quantized. Context is 128K, from the Qwen2.5 bases.
These are the easiest DeepSeek reasoning weights to deploy.

<!-- item: serving -->
## Serving stacks

vLLM, SGLang, llama.cpp and Ollama all support these models first-class. They are small enough
for edge and on-device use.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (conditional). The models have no safety tuning of their own, so supply
input/output guardrails and a guard or classifier model. Add prompt-injection defences, treat
retrieved and tool content as untrusted in agentic use, and allow for the China-aligned
filtering carried over from R1.

<!-- item: quantization -->
## Available quantizations

These are the most extensively quantized DeepSeek artifacts, in GGUF and lower-bit formats
across all sizes. The MIT licence permits redistribution of the derivatives. Verify provenance per
mirror.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The MIT licence permits unrestricted fine-tuning and further distillation, and the small sizes make
it cheap. The distillation data and code are closed, so the distillation itself cannot be
reproduced from scratch.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve the model behind an OpenAI-compatible endpoint (vLLM, SGLang or Ollama) and point the
client at it. Handle the reasoning (think-tag) output format in the client.
