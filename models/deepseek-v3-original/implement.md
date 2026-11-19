# Implement - DeepSeek-V3 (original, DeepSeek License)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and serve
with vLLM, SGLang, llama.cpp or Ollama. Pin the exact revision and verify checksums. Deploy the
Chat variant for assistant use; the Base variant is an un-tuned completion model. The weight
licence is the DeepSeek License Agreement, not MIT.

<!-- item: hardware -->
## Hardware & VRAM requirements

This is a 671B-total / 37B-active MoE. Even quantized the weights are large, so full-fidelity
deployment is a multi-GPU or multi-node exercise. The community quantization ecosystem (GGUF
and lower-bit) makes reduced-precision serving tractable, at the usual quality trade-off. The
128K context adds KV-cache pressure at long inputs.

<!-- item: serving -->
## Serving stacks

First-class support across vLLM, SGLang, llama.cpp and Ollama.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (conditional). Honour the DeepSeek License use restrictions; they are a
binding condition of the grant, not optional guidance.

Supply your own input/output guardrails and a guard model. Add prompt-injection defences and
treat retrieved and tool content as untrusted for agentic use. Account for China-aligned topic
filtering. Never deploy the Base variant unwrapped.

<!-- item: quantization -->
## Available quantizations

An extensive community quantization ecosystem circulates. Redistribution of these derivatives
must carry the DeepSeek License field-of-use restrictions (not MIT terms). Verify provenance
and prefer hosts you already trust.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The licence permits fine-tuning and derivatives, but they carry the field-of-use restrictions.
Training data and code are closed, so from-scratch reproduction is not possible. Adapting the
released weights is possible within the licence's limits.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve the Chat variant behind vLLM's or SGLang's OpenAI-compatible endpoint and point the
existing client at it. The Chat variant exposes a standard instruct interface.
