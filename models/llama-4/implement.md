# Implement - Meta Llama 4 (multimodal)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Accept the licence on the gated `meta-llama` organisation, download the safetensors and serve
with vLLM, transformers or a major cloud endpoint. EU-domiciled entities must confirm they are
licensed before use, because the multimodal licence is not granted to them. Pin the exact
revision and verify checksums.

<!-- item: hardware -->
## Hardware & VRAM requirements

These are mixture-of-experts multimodal models. Scout (109B total / 17B active) fits a
high-memory node or aggressive quantization. Maverick (400B/17B) needs multi-GPU infrastructure.
Behemoth (~2T / 288B active) is data-centre scale. Scout advertises up to 10M tokens of context,
which is memory-intensive.

<!-- item: serving -->
## Serving stacks

vLLM, transformers and every major cloud (Bedrock, Vertex, Together, Groq). The toolchain is the
broadest of any open family.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T3 (conditional). EU-domiciled entities must not use the Llama 4 multimodal
weights, because the licence is not granted to them. All users must check the 700M-MAU
commercial trigger and honour the "Built with Llama" naming and the AUP.

Pair the model with Llama Guard and Prompt Guard, add input/output guardrails and
prompt-injection defences, and treat input images and tool content as untrusted.

<!-- item: quantization -->
## Available quantizations

Extensive community GGUF and quantized builds exist. Use stays bound by the Llama 4 licence,
including the EU carve-out; a quant confers no additional rights.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

SFT and LoRA are supported for licensed (non-EU-domiciled) users. Derivatives carry the Llama
conditions and naming. Training data and code are closed, so from-scratch reproduction is not
possible.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind an OpenAI-compatible endpoint or a cloud API. Handle the Llama 4 chat template,
special tokens and multimodal (image) inputs at the client.
