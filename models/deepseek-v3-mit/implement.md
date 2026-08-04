# Implement - DeepSeek-V3 (MIT)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face
(V3-0324 or V3.1) and serve with vLLM, SGLang, llama.cpp, or Ollama. Pin the exact revision
and verify checksums before loading. Confirm you are on a V3-0324-or-later checkpoint for
the MIT grant.

<!-- item: hardware -->
## Hardware & VRAM requirements

A 671B-total / 37B-active MoE: even quantized the weights are large, so a full-fidelity
deployment is a multi-GPU / multi-node exercise. The extensive community quantization
ecosystem (GGUF and lower-bit) makes reduced-precision serving tractable on smaller
footprints, at the usual quality trade-off. 128K context adds KV-cache pressure at long
inputs.

<!-- item: serving -->
## Serving stacks

First-class support across **vLLM**, **SGLang**, **llama.cpp**, and **Ollama**, with wide
third-party hosting shortly after release.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** No first-party guard model ships and safety tuning
is lighter than at Western frontier labs, so supply your own input/output guardrails and a
guard/classifier model, add prompt-injection defences and treat retrieved/tool content as
untrusted for agentic use, and account for China-aligned topic filtering on sensitive
prompts. With those controls in place it is deployable for general-purpose assistant use;
without them it is not customer-safe.

<!-- item: quantization -->
## Available quantizations

An extensive community quantization ecosystem (GGUF and lower-bit variants) circulates. MIT
permits redistribution of these derivatives, but each is a separate artifact whose trust
equals its uploader - verify provenance and prefer hosts you already trust.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

MIT permits unrestricted fine-tuning and distillation of the released weights. The training
data and code are closed, so there is no from-scratch reproduction, but adaptation of the
V3-0324 / V3.1 weights is unrestricted.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM's or SGLang's OpenAI-compatible endpoint and point your existing client at
it. V3.1 exposes a hybrid reasoning mode - handle its output convention at the client,
separating any reasoning segment from the final answer.
