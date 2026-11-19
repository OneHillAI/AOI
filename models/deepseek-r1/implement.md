# Implement - DeepSeek-R1

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Download the safetensors from the verified `deepseek-ai` organisation on Hugging Face and serve with vLLM, SGLang, llama.cpp or Ollama. Pin the exact revision and verify checksums before loading. R1 emits explicit reasoning (think-tag) output, so budget for parsing it at the client.

<!-- item: hardware -->
## Hardware & VRAM requirements

R1 is a 671B-total / 37B-active MoE. Even quantised the weights are large, so a full-fidelity deployment needs multiple GPUs or nodes.

The community quantisation ecosystem (GGUF and lower-bit) makes reduced-precision serving tractable on smaller footprints, at the usual quality cost. The 128K context adds KV-cache pressure on long inputs.

<!-- item: serving -->
## Serving stacks

First-class support covers vLLM, SGLang, llama.cpp and Ollama, with wide third-party hosting shortly after release. The mainstream inference engines support the MoE architecture well.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T2 (conditional). No first-party guard model ships and safety tuning is lighter than at Western frontier labs, so the deployer must supply input/output guardrails and a guard or classifier model.

Add prompt-injection defences and treat retrieved and tool content as untrusted for agentic use. Account for China-aligned topic filtering on sensitive prompts. With these controls R1 is deployable for general-purpose reasoning; without them it is not customer-safe.

<!-- item: quantization -->
## Available quantizations

An extensive community quantisation ecosystem (GGUF and lower-bit variants) circulates. MIT permits redistribution of these derivatives, but each is a separate artifact whose trust equals that of its uploader. Verify provenance and prefer hosts you already trust.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

MIT expressly permits fine-tuning and distillation, and distilling R1 into smaller task-specific models is a stated DeepSeek use case. The training data and code are closed, so from-scratch reproduction is impossible, but adaptation and distillation of the released weights are unrestricted.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve behind the OpenAI-compatible endpoint of vLLM or SGLang and point the existing client at it. Handle R1's reasoning / think-tag output at the client by separating the reasoning segment from the final answer before returning it.
