# Implement - DeepSeek-V3 (original, DeepSeek License)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with vLLM, SGLang, llama.cpp, or Ollama. Pin the exact revision and verify checksums.
Deploy the **Chat** variant for assistant use - the **Base** variant is an un-tuned
completion model. Note the weight licence is the DeepSeek License Agreement, not MIT.

<!-- item: hardware -->
## Hardware & VRAM requirements

A 671B-total / 37B-active MoE: even quantized the weights are large, so a full-fidelity
deployment is a multi-GPU / multi-node exercise. The community quantization ecosystem (GGUF
and lower-bit) makes reduced-precision serving tractable, at the usual quality trade-off.
128K context adds KV-cache pressure at long inputs.

<!-- item: serving -->
## Serving stacks

First-class support across **vLLM**, **SGLang**, **llama.cpp**, and **Ollama**.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** First, **honour the DeepSeek License use
restrictions** - they are a binding condition of the grant, not optional guidance. Then, as
with the rest of the family: supply your own input/output guardrails and a guard model, add
prompt-injection defences and treat retrieved/tool content as untrusted for agentic use, and
account for China-aligned topic filtering. Never deploy the Base variant unwrapped.

<!-- item: quantization -->
## Available quantizations

An extensive community quantization ecosystem circulates. Redistribution of these derivatives
must carry the **DeepSeek License** field-of-use restrictions (not MIT terms) - verify
provenance and prefer hosts you already trust.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The licence permits fine-tuning and derivatives, but they **inherit the field-of-use
restrictions**. The training data and code are closed, so there is no from-scratch
reproduction - adaptation of the released weights is possible within the licence's limits.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve the Chat variant behind vLLM's or SGLang's OpenAI-compatible endpoint and point your
existing client at it - a standard instruct interface.
