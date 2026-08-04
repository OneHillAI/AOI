# Implement - DeepSeek-R1-Distill (Llama base)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and
serve with Ollama, llama.cpp, vLLM, or SGLang. The 8B runs on a single consumer GPU. Pin the
exact revision and verify checksums. Note the weight licence is the Llama Community Licence.

<!-- item: hardware -->
## Hardware & VRAM requirements

8B on a single consumer GPU; 70B on a single data-centre GPU, or high-end consumer hardware
when quantized. 128K context. The Llama base gives the broadest hardware and toolchain support
of any distil base.

<!-- item: serving -->
## Serving stacks

First-class support across **vLLM**, **SGLang**, **llama.cpp**, and **Ollama** - the Llama
base has the widest toolchain coverage in the ecosystem.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (conditional).** First, **honour the Llama Community Licence** - the
Acceptable Use Policy, the 700M-MAU clause, and the "Built with Llama" naming/attribution are
binding conditions. Then: supply your own input/output guardrails and a guard model (these
have no safety tuning of their own), add prompt-injection defences and treat retrieved/tool
content as untrusted for agentic use, and account for the China-aligned filtering inherited
from R1.

<!-- item: quantization -->
## Available quantizations

Extensively quantized (GGUF and lower-bit) via the Llama ecosystem. Redistribution of these
derivatives must carry the **Llama licence and AUP** - verify provenance per mirror.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tuning and derivatives are permitted but **inherit the Llama restrictions** (AUP,
700M-MAU, and "Llama" naming/attribution). The distillation data and code are closed, so there
is no from-scratch reproduction of the distillation.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind an OpenAI-compatible endpoint (vLLM / SGLang / Ollama) and point your client at
it; handle the reasoning / think-tag output format at the client.
