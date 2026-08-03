# Implement - NVIDIA Nemotron 3 Ultra (550B)

_How do we deploy it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the ungated safetensors from the verified `nvidia` org on Hugging Face and serve with vLLM,
SGLang or NVIDIA NIM on a multi-node cluster. Pin the exact revision and verify checksums before
loading.

<!-- item: hardware -->
## Hardware & VRAM requirements

Ultra is frontier-scale: **550B total / 55B active** needs a multi-GPU / multi-node cluster. Official
BF16 and NVFP4 quantizations reduce the footprint but do not remove the multi-node requirement. Plan
sharding topology and memory before load; exact per-GPU VRAM is not restated here.

<!-- item: serving -->
## Serving stacks

**vLLM, SGLang** and NVIDIA's own **NIM** self-hosted microservices. NIM runs on your own
infrastructure, so data stays in your enclave. Ecosystem breadth is narrower than the smaller Nemotron 3
text models, which is part of why operational sits at 3.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T3 (bounded autonomous), conditional.** Because there is no model-level safety
evaluation, the controls are your responsibility to assemble: a downloadable guard classifier
(**Nemotron-3-Content-Safety**), the **NeMo Guardrails** toolkit for input, output and action rails, and
the **garak** red-team scanner. The conditions: run garak (or equivalent) for your own use case, and for
EU high-stakes use treat systemic-risk status as unresolved (training compute undisclosed). The OpenMDW
licence imposes no field-of-use restriction. Complete the pre-deployment gate in the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md).

<!-- item: quantization -->
## Available quantizations

NVIDIA publishes official **BF16 and NVFP4** variants of Ultra alongside the base safetensors, so a
low-precision path is first-party rather than community-only.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

A representative training recipe (Pretrain -> SFT -> MOPD -> Quant) is released with CC-BY post-training
data, so adaptation is realistic. Reproduction is not: the intermediate checkpoints the recipe depends
on are not open-sourced, and the 1M-context phase is excluded because its data is not open. Adapt from
the released checkpoint rather than expecting a full re-run.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM/SGLang or NVIDIA NIM for OpenAI-compatible endpoints. A hosted `build.nvidia.com`
preview API exists for evaluation, but treat it as an evaluation surface only: it does not store content
at session end, yet reserves use of content "to improve NVIDIA products and services, including AI
models".
