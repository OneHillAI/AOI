# Gemma 4 model overview page: sizes, memory requirements, official QAT checkpoints

source_url: https://gemma.ai/models/gemma-4/
retrieval_date: 2026-11-19
doc_type: docs
retrieved: true


Two Google documentation pages: the Gemma 4 model card page (https://gemma.ai/models/gemma-4/model-card/, header "License : Apache 2.0 | Authors : Google DeepMind", same content as the Hugging Face card) and the Gemma 4 model overview (https://gemma.ai/models/gemma-4/, redirected from https://ai.google.dev/gemma/docs/core). Extracts verbatim.

## Overview: wording left over from earlier Gemma pages

```
Gemma is a family of generative artificial intelligence models and you can
use them in a wide variety of generation tasks, including question answering,
summarization, and reasoning. Gemma models are provided with open weights and
permit responsible
commercial use,
allowing you to tune and deploy them in your own projects and applications.
```

Reading note by OneHill: "permit responsible commercial use" is carried-over wording from the Gemma Terms era. It is not a clause and does not limit the Apache-2.0 grant; it is recorded because it is a marketing-versus-binding mismatch in the opposite (cautious) direction.

## Overview: sizes, MTP drafters, memory table, QAT release routing

```
Gemma 4 models are available in 5 parameter sizes: E2B, E4B, 12B, 31B and 26B
A4B. The models can be used with their default precision (16-bit) or with a
lower precision using quantization. The different sizes and precisions represent
a set of trade-offs for your AI application. Models with higher parameters and
bit counts (higher precision) are generally more capable, but are more expensive
to run in terms of processing cycles, memory cost and power consumption. Models
with lower parameters and bit counts (lower precision) have less capabilities,
but may be sufficient for your AI task.
Gemma 4 Inference Memory Requirements¶
The following table details the approximate GPU or TPU memory requirements for
running inference with each size of the Gemma 4 model versions.
Note
These numbers may change based on your specific inference tool and environment.
Parameters
BF16 (16-bit)
SFP8 (8-bit)
Q4_0 (4-bit)
Mobile
Mobile (Text-only)
Gemma 4 E2B
11.4 GB
5.7 GB
2.9 GB
1.1 GB
0.84 GB
Gemma 4 E4B
17.9 GB
8.9 GB
4.5 GB
2.5 GB
2.2 GB
Gemma 4 12B
26.7 GB
13.4 GB
6.7 GB
Gemma 4 26B A4B
57.7 GB
28.8 GB
14.4 GB
Gemma 4 31B
69.9 GB
34.9 GB
17.5 GB
Table 1. Approximate GPU or TPU memory required to load Gemma 4 models based
on parameter count, quantization level and 20% overhead of loading additional
things. Mobile versions use LiteRT-LM.
Key Considerations for Memory Planning¶
- Efficient Architecture (E2B and E4B): The "E" stands for "effective" parameters. The smaller models incorporate Per-Layer Embeddings (PLE) to maximize parameter efficiency in on-device deployments. Rather than adding more layers to the model, PLE gives each decoder layer its own small embedding for every token. These embedding tables are large but only used for quick lookups, which is why the total memory required to load static weights is higher than the effective parameter count suggests.
- The MoE Architecture (26B A4B): The 26B is a Mixture of Experts model. While it only activates 4 billion parameters per token during generation, all 26 billion parameters must be loaded into memory to maintain fast routing and inference speeds. This is why its baseline memory requirement is much closer to a dense 26B model than a 4B model.
- Base Weights Only: The estimates in the preceding table only account for the memory required to load the static model weights. They don't include the additional VRAM needed for supporting software or the context window.
- Context Window (KV Cache): Memory consumption will increase dynamically based on the total number of tokens in your prompt and the generated response. Larger context windows require significantly more VRAM on top of the base model weights.
- Fine-Tuning Overhead: Memory requirements for fine-tuning Gemma models are drastically higher than for standard inference. Your exact footprint will depend heavily on the development framework, batch size, and whether you are using full-precision tuning versus a Parameter-Efficient Fine-Tuning (PEFT) method like Low-Rank Adaptation (LoRA).
Quantization-Aware Training (QAT)¶
For deployments requiring maximum efficiency with minimal quality compromise,
Gemma offers official Quantization-Aware Training (QAT) models.
Unlike standard Post-Training Quantization (PTQ), which compresses a fully
trained model and can lead to quality degradation, QAT integrates quantization
simulation into the training process itself. This allows the model to learn to
compensate for the precision loss, resulting in smaller models that perform
nearly identically to their high-precision baselines.
Quick Routing Table¶
Target Deployment Engine
Download Suffix
Primary Use Case
llama.cpp / LM Studio (Local)
{model-name}-qat-q4_0-gguf
Zero-setup local deployment on CPU, Apple Silicon, or consumer GPUs.
vLLM / SGLang
SERVER: {model-name}-qat-w4a16-ct MOBILE: {model-name}-qat-mobile-ct
High-throughput inference utilizing 4-bit weights with 16-bit activations.
Speculative Decoding
MODEL: {model-name}-qat-q4_0-unquantized DRAFTER: {model-name}-qat-q4_0-unquantized-assistant
Running a primary model alongside its matching MTP draft model to drastically accelerate token generation. The model must be quantized.
Other formats
{model-name}-qat-q4_0-unquantized
Unquantized weights for converting to other formats (e.g. MLX)
Mobile Deployment (Transformers)
{model-name}-qat-mobile-transformers
Edge weights optimized for mobile use cases. They serve as reference for other formats.
Official QAT collections on Hugging Face
- collections/google/gemma-4-qat-q4-0
- Unquantized QAT Checkpoints (-unquantized / -assistant): Half-precision weights extracted directly from the QAT pipeline. These are ideal for custom downstream compilation, research, or running speculative decoding using the assistant draft models. Available for Gemma 4 E2B, E4B, 12B, 26B A4B, and 31B.
- GGUF (-gguf): Checkpoints available for immediate drop-in compatibility across the local LLM ecosystem. Available for Gemma 4 E2B, E4B, 12B, 26B A4B, and 31B.
- Compressed Tensors (-w4a16-ct): Serialized natively in the compressed-tensors standard for optimized, high-concurrency cloud serving. Available for Gemma 4 E2B, E4B, 12B, and 31B.
- collections/google/gemma-4-qat-mobile
- Mobile-Optimized (-mobile-transformers / -mobile-ct): Built on a custom wNa8o8 schema engineered specifically for mobile hardware limits. It utilizes targeted 2-bit decoding layers, optimized KV caches, and static activations to maximize on-device RAM savings without choking edge processors. Available for Gemma 4 E2B and E4B.
All official Gemma 4 QAT checkpoints can also be accessed directly from
Kaggle.
```

Header row of the memory table as rendered: Parameters | BF16 (16-bit) | SFP8 (8-bit) | Q4_0 (4-bit) | Mobile | Mobile (Text-only). Row values (GB) in the order printed: E2B 11.4, 5.7, 2.9, 1.1, 0.84; E4B 17.9, 8.9, 4.5, 2.5, 2.2; 12B 26.7, 13.4, 6.7; 26B A4B 57.7, 28.8, 14.4; 31B 69.9, 34.9, 17.5 (rendered with the three non-mobile columns for 12B, 26B A4B and 31B).
