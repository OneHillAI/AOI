# model_card / sarvam-30b

source_url: https://huggingface.co/sarvamai/sarvam-30b (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE: front matter is identical to the 105B card (license: apache-2.0, the same 22 language codes plus en, library_name transformers). Only the differing sections are extracted.

## Introduction and architecture
```
## Introduction

**Sarvam-30B** is an advanced Mixture-of-Experts (MoE) model with 2.4B non-embedding active parameters, designed primarily for practical deployment. It combines strong reasoning, reliable coding ability, and best-in-class conversational quality across Indian languages. Sarvam-30B is built to run reliably in resource-constrained environments and can handle multilingual voice calls while performing tool calls.

A major focus during training was the Indian context and languages, resulting in **state-of-the-art performance across 22 Indian languages** for its model size.

Sarvam-30B is open-sourced under the **Apache License**. For more details, see our [blog](https://www.sarvam.ai/blogs/sarvam-30b-105b).

## Architecture

The 30B MoE model is designed for throughput and memory efficiency. It uses 19 layers, a dense FFN `intermediate_size` of 8192, `moe_intermediate_size` of 1024, top-6 routing, grouped KV heads (`num_key_value_heads=4`), and an extremely high rope_theta (`8e6`) for long-context stability without RoPE scaling. It has 128 experts with a shared expert, a routed scaling factor of 2.5, and auxiliary-loss-free router balancing. The 30B model focuses on throughput and memory efficiency through fewer layers, grouped KV attention, and smaller experts.


```

## Benchmarks (publisher-run)
```
<details>
  <summary>Knowledge & Coding</summary>

| Benchmark | Sarvam-30B | Gemma 27B It | Mistral-3.2-24B | OLMo 3.1 32B Think | Nemotron-3-Nano-30B-A3B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|---|---|---|
| Math500 | 97.0 | 87.4 | 69.4 | 96.2 | 98.0 | 97.6 | 97.0 | 94.2 |
| HumanEval | 92.1 | 88.4 | 92.9 | 95.1 | 97.6 | 95.7 | 96.3 | 95.7 |
| MBPP | 92.7 | 81.8 | 78.3 | 58.7 | 91.9 | 94.3 | 91.8 | 95.3 |
| Live Code Bench v6 | 70.0 | 28.0 | 26.0 | 73.0 | 68.3 | 66.0 | 64.0 | 61.0 |
| MMLU | 85.1 | 81.2 | 80.5 | 86.4 | 84.0 | 88.4 | 86.9 | 85.3 |
| MMLU Pro | 80.0 | 68.1 | 69.1 | 72.0 | 78.3 | 80.9 | 73.6 | 75.0 |
| MILU | 76.8 | 69.2 | 67.9 | 69.9 | 64.8 | 82.6 | 75.6 | 73.7 |
| Arena Hard v2 | 49.0 | 50.1 | 43.1 | 42.0 | 67.7 | 72.1 | 58.1 | 62.9 |
| Writing Bench | 78.7 | 71.4 | 70.3 | 75.7 | 83.7 | 85.0 | 79.2 | 79.1 |

</details>

<details>
  <summary>Reasoning & Math</summary>

| Benchmark | Sarvam-30B | OLMo 3.1 32B | Nemotron-3-Nano-30B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|---|
| GPQA Diamond | 66.5 | 57.5 | 73.0 | 73.4 | 75.2 | 71.5 |
| AIME 25 (w/ Tools) | 88.3 (96.7) | 78.1 (81.7) | 89.1 (99.2) | 85.0 (-) | 91.6 (-) | 91.7 (98.7) |
| HMMT (Feb 25) | 73.3 | 51.7 | 85.0 | 71.4 | 85.0 | 76.7 |
| HMMT (Nov 25) | 74.2 | 58.3 | 75.0 | 73.3 | 81.7 | 68.3 |
| Beyond AIME | 58.3 | 48.5 | 64.0 | 61.0 | 60.0 | 46.0 |

</details>

<details>
  <summary>Agentic</summary>

| Benchmark | Sarvam-30B | Nemotron-3-Nano-30B | Qwen3-30B-Thinking-2507 | GLM 4.7 Flash | GPT-OSS-20B |
|---|---|---|---|---|---|
| BrowseComp | 35.5 | 23.8 | 2.9 | 42.8 | 28.3 |
| SWE Bench Verified | 34.0 | 38.8 | 22.0 | 59.2 | 34.0 |
| τ² Bench (avg.) | 45.7 | 49.0 | 47.7 | 79.5 | 48.7 |

> See footnote for evaluation details.

</details>

```

NOTE: the 30B card's AIME 25 (w/ Tools) cell for Sarvam-30B reads 88.3 (96.7). The publisher blog table for the same cell reads 80.0 (96.7) (see marketing__sarvam-30b-105b-blog). The two publisher documents disagree. As with the 105B card there is no safety, limitations or training-data section. The card gives 65,536 tokens as the evaluation length and config.json sets max_position_embeddings 131072.
