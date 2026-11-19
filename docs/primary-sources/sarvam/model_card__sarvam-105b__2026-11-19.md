# model_card / sarvam-105b

source_url: https://huggingface.co/sarvamai/sarvam-105b (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## Front matter
```
---
language:
  - en
  - hi
  - bn
  - ta
  - te
  - mr
  - gu
  - kn
  - ml
  - pa
  - or
  - as
  - ur
  - sa
  - ne
  - sd
  - kok
  - mai
  - doi
  - mni
  - sat
  - ks
  - bo
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
---
```
NOTE: the front matter lists 22 language codes plus en. They are hi bn ta te mr gu kn ml pa or as ur sa ne sd kok mai doi mni sat ks bo. The code bo is Tibetan, which is not a scheduled language of India, and brx (Bodo) is absent, so the tag list is not exactly the 22 scheduled languages.

## Introduction and architecture
```
## Introduction

**Sarvam-105B** is an advanced Mixture-of-Experts (MoE) model with 10.3B active parameters, designed for superior performance across a wide range of complex tasks. It is highly optimized for complex reasoning, with particular strength in agentic tasks, mathematics, and coding.

Sarvam-105B is a top-tier performer, consistently matching or surpassing several major closed-source models and staying within a narrow margin of frontier models across diverse reasoning and agentic benchmarks. It demonstrates exceptional agentic and reasoning capabilities in real-world applications such as web search and technical troubleshooting.

A major focus during training was the Indian context and languages, resulting in **state-of-the-art performance across 22 Indian languages** for its model size.

Sarvam-105B is open-sourced under the **Apache License**. For more details, see our [blog](https://www.sarvam.ai/blogs/sarvam-30b-105b).

## Architecture

The 105B model adopts an MLA-style attention stack with decoupled QK head dimensions (`q_head_dim=192` split into RoPE and noPE components, `v_head_dim=128`) and a large head_dim of 576, enabling higher representational bandwidth per head while keeping the hidden size at 4096. This approach improves attention expressivity and long-context extrapolation (via YaRN scaling with a factor of 40 and 128K context). It has an `intermediate_size` (16384) and `moe_intermediate_size` (2048), combined with top-8 routing over 128 experts, which increases per-token active capacity while keeping activation cost manageable. The model has one shared expert, a routed scaling factor of 2.5, and auxiliary-loss-free router balancing.


```

## Benchmarks (publisher-run)
```
<details>
  <summary>Knowledge & Coding</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| Math500 | 98.6 | 97.2 | 97.0 | 98.2 |
| Live Code Bench v6 | 71.7 | 59.5 | 72.3 | 68.7 |
| MMLU | 90.6 | 87.3 | 90.0 | 90.0 |
| MMLU Pro | 81.7 | 81.4 | 80.8 | 82.7 |
| Writing Bench | 80.5 | 83.8 | 86.5 | 84.6 |
| Arena Hard v2 | 71.0 | 68.1 | 88.5 | 68.2 |
| IF Eval | 84.8 | 83.5 | 85.4 | 88.9 |

</details>

<details>
  <summary>Reasoning & Math</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| GPQA Diamond | 78.7 | 75.0 | 80.1 | 77.2 |
| AIME 25 (w/ Tools) | 88.3 (96.7) | 83.3 | 90.0 | 87.8 |
| Beyond AIME | 69.1 | 61.5 | 51.0 | 68.0 |
| HMMT (Feb 25) | 85.8 | 69.2 | 90.0 | 73.9 |
| HMMT (Nov 25) | 85.8 | 75.0 | 90.0 | 80.0 |

</details>

<details>
  <summary>Agentic</summary>

| Benchmark | Sarvam-105B | GLM-4.5-Air | GPT-OSS-120B | Qwen3-Next-80B-A3B-Thinking |
|---|---|---|---|---|
| BrowseComp | 49.5 | 21.3 | - | 38.0 |
| SWE Bench Verified (SWE-Agent Harness) | 45.0 | 57.6 | 50.6 | 60.9 |
| τ² Bench (avg.) | 68.3 | 53.2 | 65.8 | 55.0 |

> See footnote for evaluation details.

</details>

```

## Footnote and citation
```
## Footnote

* **General settings**: All benchmarks are evaluated with a maximum context length of 65,536 tokens.
* **Reasoning & Math benchmarks** (Math500, MMLU, MMLU Pro, GPQA Diamond, AIME 25, Beyond AIME, HMMT): Evaluated with `temperature=1.0, top_p=1.0, max_new_tokens=65536`.
* **Coding & Knowledge benchmarks** (Live Code Bench v6, Arena Hard v2, IF Eval):
  Evaluated with `temperature=1.0, top_p=1.0, max_new_tokens=65536`.
* **Writing Bench**:
  Responses generated using official Writing-Bench parameters:
  `temperature=0.7, top_p=0.8, top_k=20, max_length=16000`.
  Scoring performed using the official Writing-Bench critic model with:
  `temperature=1.0, top_p=0.95, max_length=2048`.
* **Agentic benchmarks** (BrowseComp, SWE Bench Verified, τ² Bench): Evaluated with `temperature=0.5, top_p=1.0, max_new_tokens=32768`.

## Citation
```
@misc{sarvam_sovereign_models,
  title        = {Introducing Sarvam's Sovereign Models},
  author       = {{Sarvam Foundation Models Team}},
  year         = {2026},
  howpublished = {\url{https://www.sarvam.ai/blogs/sarvam-30b-105b}},
  note         = {Accessed: 2026-03-03}
}
```
```

NOTE: the card has no section on training data, training code, safety, intended use, limitations or risks. It states no per-language Indian-language result. vLLM support is described as a custom fork or a hot-patch script (hotpatch_vllm.py), and every inference example sets trust_remote_code=True.
