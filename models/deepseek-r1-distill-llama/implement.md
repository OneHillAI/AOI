# Implement - DeepSeek-R1-Distill (Llama base)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with Ollama, llama.cpp, vLLM or SGLang. The 8B runs on a single consumer GPU. Pin the
exact revision and verify checksums. The weight licence is the Llama Community Licence.

<!-- item: hardware -->
## Hardware & VRAM requirements

The 8B runs on a single consumer GPU. The 70B runs on a single data-centre GPU, or on
high-end consumer hardware when quantized. Context is 128K. The Llama base gives the
broadest hardware and toolchain support of any distil base.

<!-- item: serving -->
## Serving stacks

vLLM, SGLang, llama.cpp and Ollama all support these models first-class. The Llama base has
the widest toolchain coverage in the ecosystem.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (conditional). Honour the Llama Community Licence first: the
Acceptable Use Policy, the 700M-MAU clause and the "Built with Llama" naming and attribution
are binding conditions.

Supply your own input/output guardrails and a guard model, because the models have no safety
tuning of their own. Add prompt-injection defences and treat retrieved and tool content as
untrusted in agentic use. Account for the China-aligned filtering carried over from R1.

<!-- item: quantization -->
## Available quantizations

The models are extensively quantized (GGUF and lower-bit) via the Llama ecosystem.
Redistribution of these derivatives must carry the Llama licence and AUP. Verify provenance
per mirror.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning and derivatives are permitted and carry the Llama restrictions (AUP, 700M-MAU and
"Llama" naming and attribution). The distillation data and code are closed, so the
distillation cannot be reproduced from scratch.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind an OpenAI-compatible endpoint (vLLM, SGLang or Ollama) and point the client at
it. Handle the reasoning / think-tag output format at the client.
