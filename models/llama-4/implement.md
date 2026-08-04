# Implement - Meta Llama 4 (multimodal)

_How do we run it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Accept the licence on the gated `meta-llama` organisation, download the safetensors, and serve
with vLLM / transformers or a major cloud endpoint. **EU-domiciled entities: confirm you are
licensed before use** - the multimodal licence is not granted to you. Pin the exact revision and
verify checksums.

<!-- item: hardware -->
## Hardware & VRAM requirements

Mixture-of-experts multimodal models: Scout (109B total / 17B active) fits a high-memory node or
aggressive quantization; Maverick (400B/17B) needs serious multi-GPU infrastructure; Behemoth
(~2T / 288B active) is data-centre-scale. Very long context (Scout advertises up to 10M tokens)
is memory-intensive in practice.

<!-- item: serving -->
## Serving stacks

**vLLM**, **transformers**, and every major cloud (**Bedrock**, **Vertex**, **Together**,
**Groq**) - the broadest toolchain of any open family.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T3 (conditional).** First: **EU-domiciled entities must not use the Llama
4 multimodal weights** (the licence is not granted to you), and all users must check the
**700M-MAU** commercial trigger and honour the "Built with Llama" naming and the AUP. Then: pair
with Meta's **Llama Guard** and **Prompt Guard**, add your own input/output guardrails, add
prompt-injection defences, and treat input images and tool content as untrusted.

<!-- item: quantization -->
## Available quantizations

Extensive community GGUF / quantized builds. Use remains bound by the **Llama 4 licence
including the EU carve-out** - a quant confers no additional rights.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

SFT / LoRA are supported for licensed (non-EU-domiciled) users; derivatives inherit the Llama
conditions and naming. Training data and code are closed, so there is no from-scratch
reproduction.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind an OpenAI-compatible endpoint or a cloud API; handle the Llama-4 chat template,
special tokens, and multimodal (image) inputs at the client.
