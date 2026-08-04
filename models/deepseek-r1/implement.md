# Implement - DeepSeek-R1

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with vLLM, SGLang, llama.cpp, or Ollama. Pin the exact revision and verify checksums
before loading. R1 emits explicit reasoning (think-tag) output - budget for parsing it at
the client.

<!-- item: hardware -->
## Hardware & VRAM requirements

R1 is a 671B-total / 37B-active MoE: even quantized the weights are large, so a full-fidelity
deployment is a multi-GPU / multi-node exercise. The extensive community quantization
ecosystem (GGUF and lower-bit) makes reduced-precision serving tractable on smaller
footprints, at the usual quality trade-off. 128K context adds KV-cache pressure at long
inputs.

<!-- item: serving -->
## Serving stacks

First-class support across **vLLM**, **SGLang**, **llama.cpp**, and **Ollama**, with wide
third-party hosting shortly after release. The MoE architecture is well-supported by the
mainstream inference engines.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** No first-party guard model ships and safety tuning
is lighter than at Western frontier labs, so you must supply your own input/output
guardrails and a guard/classifier model, add prompt-injection defences and treat
retrieved/tool content as untrusted for agentic use, and account for China-aligned topic
filtering on sensitive prompts. With those controls in place R1 is deployable for
general-purpose reasoning; without them it is not customer-safe.

<!-- item: quantization -->
## Available quantizations

An extensive community quantization ecosystem (GGUF and lower-bit variants) circulates. MIT
permits redistribution of these derivatives, but each is a separate artifact whose trust
equals its uploader - verify provenance and prefer hosts you already trust.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

MIT **expressly permits** fine-tuning and distillation - distilling R1 into smaller
task-specific models is a stated DeepSeek use case. The training data and code are closed,
so there is no from-scratch reproduction, but adaptation and distillation of the released
weights are unrestricted.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM's or SGLang's OpenAI-compatible endpoint and point your existing client at
it. Handle R1's reasoning / think-tag output format at the client - separate the reasoning
segment from the final answer before returning it.
