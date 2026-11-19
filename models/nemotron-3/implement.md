# Implement - NVIDIA Nemotron 3 (Super + Nano)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the ungated safetensors from the verified `nvidia` org on Hugging Face and serve with vLLM, SGLang, Ollama, llama.cpp or NVIDIA NIM. Pick the variant to fit your hardware (Nano or Super), pin the exact revision, and verify checksums before loading.

<!-- item: hardware -->
## Hardware & VRAM requirements

Nano (30B / 3.5B active) runs on modest single-GPU hardware, and Super (120B / 12B) is a mid-tier multi-GPU target. Official BF16, FP8 and NVFP4 quantizations are published for each. Size against the specific variant; exact per-GPU VRAM is not stated.

<!-- item: serving -->
## Serving stacks

Broad support: vLLM, SGLang, Ollama, llama.cpp and NVIDIA's own NIM self-hosted microservices. NIM runs on your own infrastructure, so data stays in your enclave. It is deployment tooling and not a hosted provider.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T3 (bounded autonomous), conditional. No model-level safety evaluation is published, so the deployer assembles the controls. NVIDIA ships the pieces at the family level: a downloadable guard classifier (Nemotron-3-Content-Safety), the NeMo Guardrails toolkit for input, output and action rails, and the garak red-team scanner.

Reaching T2 needs the guard classifier plus input/output rails. T3 additionally needs deterministic action limits, a kill switch and red-team sign-off. Run garak (or equivalent) for your own use case, and note that the guard-classifier scores are NVIDIA self-reported. The irrevocable licence carries no field-of-use restriction. Complete the pre-deployment gate in the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md).

<!-- item: quantization -->
## Available quantizations

NVIDIA publishes official BF16, FP8 and NVFP4 variants for both models alongside the base safetensors, so the low-precision path is first-party.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Runnable training and fine-tuning recipes are released on GitHub (Pretrain -> SFT -> RL), and the post-training data is CC-BY-4.0, so adaptation is accessible. The recipes "train exclusively on the open-sourced subset of training data", so results differ from the tech-report benchmarks that used additional proprietary data.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind vLLM/SGLang or NVIDIA NIM for OpenAI-compatible endpoints. A hosted `build.nvidia.com` preview API exists for evaluation only: it does not store content at session end, yet reserves use of content "to improve NVIDIA products and services, including AI models".
