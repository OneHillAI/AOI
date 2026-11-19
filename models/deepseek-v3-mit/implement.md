# Implement - DeepSeek-V3 (MIT)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face (V3-0324 or V3.1) and serve with vLLM, SGLang, llama.cpp or Ollama. Pin the exact revision and verify checksums before loading. Use a V3-0324-or-later checkpoint for the MIT grant.

<!-- item: hardware -->
## Hardware & VRAM requirements

The model is a 671B-total / 37B-active MoE. Even quantized the weights are large, so full-fidelity deployment needs multiple GPUs or nodes. Community quantizations (GGUF and lower-bit) make reduced-precision serving tractable on smaller footprints, at the usual quality cost. The 128K context adds KV-cache pressure on long inputs.

<!-- item: serving -->
## Serving stacks

vLLM, SGLang, llama.cpp and Ollama all support the model, and third-party hosting was wide shortly after release.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (conditional). No first-party guard model ships and safety tuning is lighter than at Western frontier labs. Supply input/output guardrails and a guard or classifier model, add prompt-injection defences, and treat retrieved and tool content as untrusted in agentic use. Account for China-aligned topic filtering on sensitive prompts. With these controls the model is deployable for general-purpose assistant use. Without them it is not customer-safe.

<!-- item: quantization -->
## Available quantizations

Community quantizations (GGUF and lower-bit) are widely available. MIT permits redistribution of these derivatives. Each is a separate artifact whose trust equals its uploader, so verify provenance and prefer hosts already trusted.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

MIT permits unrestricted fine-tuning and distillation of the released V3-0324 and V3.1 weights. Training data and code are closed, so the model cannot be reproduced from scratch.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind the OpenAI-compatible endpoint of vLLM or SGLang and point the existing client at it. V3.1 exposes a hybrid reasoning mode, so the client must separate any reasoning segment from the final answer.
