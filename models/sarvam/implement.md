# Implement - Sarvam-30B, Sarvam-105B and Sarvam-105B-1711

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Use Transformers with `trust_remote_code=True`, SGLang or vLLM (`ev-card-105b`). The repos ship `configuration_sarvam_moe.py` and `modeling_sarvam_moe.py`, which run on your machine.

For the March builds, vLLM needs the Sarvam fork or `hotpatch_vllm.py`. The script installs vLLM 0.15.0, adds two registry entries and downloads model executors. Review it first.

The 1711 cards give `vllm serve` commands for vLLM 0.33.0 with `--trust-remote-code`, `--tool-call-parser glm45` and `--reasoning-parser glm45` (`ev-card-1711`). An optional `dspark/` draft model enables speculative decoding.

Pin the revision with `revision="<commit-sha>"`. The weights are ungated and need no login (`ev-hub`).

<!-- item: hardware -->
## Hardware & VRAM requirements

No minimum is stated for the March builds. File sizes give a floor (`ev-hub`, `ev-quant-code`, `ev-card-1711`).

| Build | Size on disk |
|---|---|
| sarvam-105b (float32) | 424.2 GB |
| sarvam-105b-fp8 | 112.6 GB |
| sarvam-105b-gguf (Q4_K_M) | 64.2 GB |
| sarvam-105b-1711-bf16 | 218.3 GB |
| sarvam-105b-1711 (NVFP4, MXFP8) | 70.2 GB |
| sarvam-30b (float32) | 128.6 GB |
| sarvam-30b-fp8 | 38.7 GB |
| sarvam-30b-gguf (Q4_K_M) | 19.6 GB |

The card examples use tensor parallelism of 4 (SGLang) to 8 (vLLM) for the 105B and 2 for the 30B. The 1711 card reports throughput on one B200 (128K context) and on one 96 GB RTX PRO 6000 Blackwell (50K context).

<!-- item: serving -->
## Serving stacks

Transformers, SGLang and vLLM are documented. vLLM needs the fork or hot-patch for the March builds, and a native pull request was open at release (`ev-card-105b`). The 1711 cards test vLLM 0.33.0 (`ev-card-1711`). The GGUF cards give llama.cpp build and run commands (`ev-quant-code`).

Ollama and MLX are undocumented. A request for MLX support is open (`ev-discussions`).

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling T1, conditional. Use it for internal tasks with a human reading every output.

Before any step up, add your own guard classifier, safety and jailbreak tests, a reviewed copy of the custom Python files and sandboxed tool execution. Sarvam publishes no safety evaluation and no guard model (`ev-blog`, `ev-card-1711`).

<!-- item: quantization -->
## Available quantizations

Sarvam publishes FP8 builds of both models, Q4_K_M GGUF builds of both, and a mixed NVFP4 and MXFP8 build of 105B-1711. The FP8 cards say the weights were quantised with NVIDIA ModelOpt (`ev-quant-code`, `ev-hub`).

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Apache-2.0 weights allow fine-tuning, and Prism is a Sarvam LoRA fine-tune of the 105B (`ev-token-factory`). A merged staff pull request restores differentiable single-rank MoE dispatch for training and fails on expert-parallel training (`ev-discussions`).

No recipe, dataset or post-training code is published. Check the Terms and EULA position on derivatives before you ship one (`ev-tos`, `ev-eula`).

<!-- item: integration -->
## API / OpenAI-compatible integration

Self-hosted vLLM exposes an OpenAI-compatible `/v1/chat/completions` endpoint. Thinking is on by default and is turned off with `chat_template_kwargs` (`ev-card-1711`).

Sarvam's hosted API is also OpenAI-compatible and carries its own terms, covered in the support page (`ev-api-docs`).
