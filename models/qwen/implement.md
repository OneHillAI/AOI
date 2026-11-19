# Implement - Qwen (Qwen3 family)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Qwen3 checkpoints load with standard tooling: `from_pretrained` on the safetensors weights, `ollama pull` for quantised local use, vLLM for serving, or llama.cpp on a GGUF quant. They are also available on Alibaba's ModelScope.

Pin the exact revision and verify checksums on whichever hub is used, ideally cross-checking that they match between Hugging Face and ModelScope.

<!-- item: hardware -->
## Hardware & VRAM requirements

Dense 0.6B-32B models run from a laptop to a single modern GPU. The 235B MoE and 480B-Coder need multi-GPU infrastructure, or aggressive quantisation for latency-sensitive serving.

<!-- item: serving -->
## Serving stacks

Serving support is broad: vLLM, llama.cpp, Ollama, TGI, MLX and transformers. No custom runtime is required, and day-0 availability across the stack is reliable.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T3 (conditional). Supply your own input/output guardrails and a guard or classifier model, and do not rely on built-in alignment.

Add prompt-injection defences for agentic and coding use. Verify checksums across Hugging Face and ModelScope and pin the revision. For the systemic-risk large variants, close the EU Article 55 gap yourself or avoid EU high-stakes use.

<!-- item: quantization -->
## Available quantizations

Abundant community GGUF and AWQ quants (via Ollama and others) cover the size range. No single official quantisation programme exists, so validate the specific quant before adopting it.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The Apache-2.0 safetensors checkpoints support standard SFT and LoRA via transformers and TRL. The wide size ladder and the strong coder base make Qwen a good target for domain specialisation and distillation.

Training data and code are not released, so continued pre-training from scratch is not possible and only the released weights can be adapted.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Qwen behind vLLM's OpenAI-compatible `/v1` server (or TGI/Ollama endpoints) for drop-in client integration. Parse Qwen3's thinking and non-thinking output modes: the thinking-mode format is the main behaviour to handle when substituting Qwen for another model.
