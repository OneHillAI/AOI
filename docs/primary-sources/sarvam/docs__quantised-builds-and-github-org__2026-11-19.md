# docs / Official FP8 and GGUF builds, GitHub organisation, Token Factory and Prism posts

source_url: https://huggingface.co/sarvamai/sarvam-30b-fp8 ; https://huggingface.co/sarvamai/sarvam-30b-gguf ; https://github.com/sarvamai ; https://www.sarvam.ai/blogs/sarvam-token-factory ; https://www.sarvam.ai/blogs/sarvam-prism
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## FP8 card (sarvam-30b-fp8)
```
This repository provides **FP8 quantized weights** for Sarvam-30B, enabling efficient deployment with reduced memory footprint and faster inference while preserving model quality. The weights are quantized using FP8 (E4M3) format via NVIDIA's ModelOpt toolkit.
```

## GGUF cards
sarvam-30b-gguf and sarvam-105b-gguf (created 2026-03-20 and 2026-03-23): Q4_K_M files only (30B 19.6 GB in six shards, 105B 64.2 GB in nine shards), license apache-2.0, llama.cpp build-and-run instructions, hub scan not completed. The cards repeat the 22-language claim and the benchmark tables.

## GitHub organisation github.com/sarvamai (repository listing)
Repositories: Gym, amazon-sagemaker-examples, dynamo, harbor, indic-numtowords, indic_nlp_library, indic_nlp_library_rdt, lhotse-asr, llm_intent_entity, llm_wer, mlx, mlx-examples, mlx-lm, model-deployments, n8n-sarvam-node, olmOCR-bench-sarvam-api, sarvam-ai-cookbook, sarvam-ai-sdk, sarvam-mcp, sec-insights, sglang, skills, torchtune, vllm.
NOTE: the list holds forks (vllm, sglang, torchtune, mlx, dynamo) and SDK or cookbook repositories. It holds no pre-training, post-training or data-curation code for Sarvam-30B or Sarvam-105B.

## Token Factory blog (16 Nov 2026)
```
Today, we are launching Sarvam Token Factory for everyone. Token Factory is our inference stack to serve our own models and leading open-weight models from GPU clusters located in India. On most of the models we serve, we match or beat the leading inference providers globally on both speed and cost. Along with Sarvam 105B, we serve GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash 1017, DeepSeek V4 Pro, Kimi K3.1 Pro and Gemma 4 31B through one OpenAI-compatible API. See the full

With Sarvam 105B, we control both the weights and the inference engine, so we can optimise them together for the workloads we serve. Most traffic comes from agents with long system prompts, growing context from tool results and short replies. Moving from BF16 to MXFP8 weights with DSpark speculative decoding increased output throughput by about 2.2× while reducing each replica from two B200s to one. We also fixed a vLLM bug that skipped CUDA graphs after warm-cache restarts, leaving GPU utilisation at 38%. Four kernel and precision changes added another 30% output per GPU on agent workloads. These included 4-bit NVFP4 experts calibrated on real MoE inputs and a custom Triton kernel for 105B’s 64 attention heads, replacing a FlashInfer kernel that assumed 128. When agent sessions exceeded GPU cache capacity, G3 increased throughput by 2.21× and cut the share of prompt tokens needing recomputation from 56.8% to 17.6%. None of these changes reduced accuracy.
```

## Prism blog (3 Nov 2026)
```
Today we are releasing Sarvam Prism, a System One decision model built on Sarvam 105B. Prism is a LoRA fine-tune of Sarvam 105B. It takes the state, question and options as input and processes them in a single forward pass. A small scoring head returns a probability for each option, with no token-by-token generation.
```
NOTE: the hosted Sarvam 105B is served in MXFP8 with DSpark speculative decoding, the same combination described on the 105B-1711 cards. The post does not name the 1711 build.
