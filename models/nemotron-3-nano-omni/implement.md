# Implement - NVIDIA Nemotron 3 Nano Omni (multimodal)

_How do we deploy it? Install, hardware, serving, safe-deployment controls, quantization,
fine-tuning, and integration live here._

<!-- item: install -->
## Install & run

Download the ungated safetensors from the verified `nvidia` org on Hugging Face - note the repo id has
**no "NVIDIA-" prefix** (`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`) - and serve with vLLM,
SGLang or NVIDIA NIM; a TensorRT-LLM deploy cookbook is linked on the card. Pin the exact revision and
verify checksums before loading.

<!-- item: hardware -->
## Hardware & VRAM requirements

Small and portable: **31B total / ~3B active** runs on modest single-GPU hardware, and an official BF16
variant is published. Budget additionally for the multimodal input pipeline (image/audio/video
preprocessing). Exact per-GPU VRAM is not restated here.

<!-- item: serving -->
## Serving stacks

**vLLM, SGLang** and NVIDIA's own **NIM** self-hosted microservices, plus a linked **TensorRT-LLM**
deploy cookbook. NIM runs on your own infrastructure, so data stays in your enclave. The multimodal
serving path is less mature than the text-only members of the family.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Deployment Ceiling: T2 (bounded), conditional.** The multimodal input surface widens the misuse path
and there is no model-level safety evaluation, so the controls are your responsibility: the
multimodal-capable **Nemotron-3-Content-Safety** guard classifier (text and images), the **NeMo
Guardrails** toolkit, and the **garak** red-team scanner. Red-team the video/audio/image input path for
your own use case before any autonomous use. The irrevocable licence imposes no field-of-use
restriction. Complete the pre-deployment gate in the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md).

<!-- item: quantization -->
## Available quantizations

An official NVIDIA **BF16** variant is published. A broader official FP8/NVFP4 program like the text
models' was not confirmed for Nano Omni this pass, so treat lower-precision paths as community or
runtime options until verified.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

A training recipe exists in the NeMo repo (`docs/nemotron/omni3`, SFT then RL), so adaptation is
realistic. Reproduction is not: the recipe surfaces only the public subset of the alignment corpus (the
full upstream corpus of 20 RL datasets / 25 environments / ~2.3M rollouts is not open). Adapt from the
released checkpoint rather than expecting a full re-run.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM/SGLang or NVIDIA NIM for OpenAI-compatible endpoints; the multimodal input path may
need the documented preprocessing. A hosted `build.nvidia.com` preview API exists for evaluation only:
it reserves use of content "to improve NVIDIA products and services, including AI models".
