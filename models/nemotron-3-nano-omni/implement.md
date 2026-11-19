# Implement - NVIDIA Nemotron 3 Nano Omni (multimodal)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the ungated safetensors from the verified `nvidia` org on Hugging Face. The repo id has
no "NVIDIA-" prefix (`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`). Serve with vLLM,
SGLang or NVIDIA NIM; a TensorRT-LLM deploy cookbook is linked on the card. Pin the exact
revision and verify checksums before loading.

<!-- item: hardware -->
## Hardware & VRAM requirements

Small and portable: 31B total / ~3B active runs on modest single-GPU hardware. Official BF16
(62 GB), FP8 (33 GB) and NVFP4 (21 GB) variants are published, and the card gives minimum GPUs
per precision: one H100 80GB for BF16, one L40S 48GB for FP8, one RTX 5090 32GB (or DGX Spark,
Jetson Thor) for NVFP4. Budget additionally for the multimodal input pipeline (image, audio and
video preprocessing).

<!-- item: serving -->
## Serving stacks

vLLM, SGLang and NVIDIA's own NIM self-hosted microservices, plus a linked TensorRT-LLM deploy
cookbook. NIM runs on your own infrastructure, so data stays in your enclave. The multimodal
serving path is less mature than the text-only members of the family.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (bounded), conditional. The multimodal input surface widens the misuse
path and there is no model-level safety evaluation, so the controls are the deployer's
responsibility. They are the multimodal-capable Nemotron-3-Content-Safety guard classifier (text
and images), the NeMo Guardrails toolkit and the garak red-team scanner.

Red-team the video/audio/image input path for the specific use case before any autonomous use.
The irrevocable licence imposes no field-of-use restriction. Complete the pre-deployment gate in
the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md).

<!-- item: quantization -->
## Available quantizations

Official NVIDIA BF16 (62 GB), FP8 (33 GB) and NVFP4 (21 GB) variants are published; the FP8 and
NVFP4 repos date from 2026-04-24. Check engine support per precision. The card's SGLang section
covers the BF16 variant only ("NVFP4 and FP8 support to come"), while its vLLM examples use the
NVFP4 and FP8 repos.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

A training recipe exists in the NeMo repo (`docs/nemotron/omni3`, SFT then RL), so adaptation is
realistic. Reproduction is not: the recipe surfaces only the public subset of the alignment
corpus, and the full upstream corpus of 20 RL datasets / 25 environments / ~2.3M rollouts is not
open. Adapt from the released checkpoint and do not expect a full re-run.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM/SGLang or NVIDIA NIM for OpenAI-compatible endpoints; the multimodal input path
may need the documented preprocessing. A hosted `build.nvidia.com` preview API exists for
evaluation only. It reserves use of content "to improve NVIDIA products and services, including
AI models".
